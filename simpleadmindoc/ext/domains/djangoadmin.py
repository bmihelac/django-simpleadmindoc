# -*- coding: utf-8 -*-
from docutils import nodes
from docutils.parsers.rst import Parser, directives
from docutils.utils import new_document

from sphinx import addnodes
from sphinx.roles import XRefRole
from sphinx.locale import l_
from sphinx.domains import Domain, ObjType
from sphinx.directives import ObjectDescription
from sphinx.util.nodes import make_refnode
from sphinx.util.compat import Directive
from django.utils.translation import ugettext as _

from simpleadmindoc.util import (model_attribute_name, model_name,
                                 model_attributes)


class DjangoAdminCurrentModel(Directive):
    has_content = False
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {}

    def run(self):
        env = self.state.document.settings.env
        model = self.arguments[0].strip()
        if model == 'None':
            env.temp_data['djangoadmin:model'] = None
        else:
            env.temp_data['djangoadmin:model'] = model
        return []


class DjangoAdminObject(ObjectDescription):

    def get_verbose_name(self, sig):
        raise ValueError

    def handle_signature(self, sig, signode):
        signode += addnodes.desc_name(sig, self.get_verbose_name(sig))
        return sig

    def add_target_and_index(self, name, sig, signode):
        targetname = '%s-%s' % (self.objtype, name)
        if name not in self.state.document.ids:
            signode['names'].append(name)
            signode['ids'].append(targetname)
            signode['first'] = not self.names
            self.state.document.note_explicit_target(signode)
        self.env.domaindata['djangoadmin']['objects'][name] = (
            self.env.docname,
            self.objtype, name)
        return name


class DjangoAdminModelAttribute(DjangoAdminObject):

    def get_verbose_name(self, sig):
        return model_attribute_name(*sig.split('.'))


class DjangoAdminModel(DjangoAdminObject):

    optional_arguments = 1
    option_spec = {
        'exclude': directives.unchanged,
        'noautodoc': directives.flag,
    }

    def get_verbose_name(self, sig):
        return model_name(*sig.split('.'))

    def run(self):
        indexnode, node = super(DjangoAdminModel, self).run()
        sig = self.arguments[0]
        lst = []

        if not 'noautodoc' in self.options:
            exclude = [
                a.strip() for a in self.options.get('exclude', '').split(',')
            ]
            app_label, model_name = sig.split('.')
            for name, opts in model_attributes(app_label, model_name).items():
                if name in exclude:
                    continue
                lst.append(".. djangoadmin:attribute:: %s.%s" % (sig, name))
                lst.append('')
                lst.append("   %s" % unicode(opts['description']))
                lst.append('')
            text = '\n'.join(lst)
            new_doc = new_document('temp-string', self.state.document.settings)
            parser = Parser()
            parser.parse(text, new_doc)
            container = nodes.container()
            container.extend(new_doc.children)
            node[1].extend(container)

        return [indexnode, node]


class DjangoAdminXRefRole(XRefRole):

    def get_verbose_name(self, sig):
        raise ValueError

    def process_link(self, env, refnode, has_explicit_title, title, target):
        current_model = env.temp_data.get('djangoadmin:model', None)
        if current_model:
            target = '%s.%s' % (current_model, target)
        title, target = super(DjangoAdminXRefRole, self).process_link(
            env,
            refnode, has_explicit_title, title, target)
        if not has_explicit_title:
            if current_model:
                title = "%s.%s" % (current_model, title)
            title = self.get_verbose_name(title)
        return title, target


class DjangoAdminModelRole(DjangoAdminXRefRole):

    def get_verbose_name(self, sig):
        return model_name(*sig.split('.'))


class DjangoAdminModelAttributeRole(DjangoAdminXRefRole):

    def get_verbose_name(self, sig):
        return model_attribute_name(*sig.split('.'))


class DjangoUnicodeRole(DjangoAdminXRefRole):

    def get_verbose_name(self, sig):
        return _(sig)


class DjangoAdminDomain(Domain):
    """DjangoAdmin domain."""
    name = 'djangoadmin'
    label = 'DjangoAdmin'
    object_types = {
        'model': ObjType(l_('Django model'), 'model'),
        'attribute': ObjType(l_('Django model attribute'),   'attribute'),
    }

    directives = {
        'model': DjangoAdminModel,
        'attribute':   DjangoAdminModelAttribute,
        'currentmodel': DjangoAdminCurrentModel,
    }
    roles = {
        'model':  DjangoAdminModelRole(),
        'attribute': DjangoAdminModelAttributeRole(),
        'unicode': DjangoUnicodeRole(),
    }
    initial_data = {
        'objects': {},  # fullname -> docname, objtype
    }

    def clear_doc(self, docname):
        for fullname, (fn, _, verbose_name) in self.data['objects'].items():
            if fn == docname:
                del self.data['objects'][fullname]

    def resolve_xref(self, env, fromdocname, builder,
                     typ, target, node, contnode):
        if target not in self.data['objects']:
            return None
        obj = self.data['objects'][target]
        title = obj[2]
        target = '%s-%s' % (obj[1], target)
        if not contnode.children:
            contnode.children = [nodes.Text(title)]
        return make_refnode(builder, fromdocname, obj[0], target,
                            contnode, obj[2])

    def get_objects(self):
        items = self.data['objects'].iteritems()
        for refname, (docname, type, verbose_name) in items:
            yield (refname, refname, type, docname, refname, 1)
