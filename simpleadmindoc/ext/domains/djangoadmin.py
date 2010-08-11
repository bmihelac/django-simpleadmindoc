# -*- coding: utf-8 -*-
import re
import string

from docutils import nodes

from sphinx import addnodes
from sphinx.roles import XRefRole
from sphinx.locale import l_, _
from sphinx.domains import Domain, ObjType
from sphinx.directives import ObjectDescription
from sphinx.util.nodes import make_refnode
from sphinx.util.docfields import Field, TypedField


def parse_directive(d):
    """
    Parses a directive signature. Returns (directive, verbose_name) string tuple.
    """
    return d.split(' ', 1)


class DjangoAdminObject(ObjectDescription):
    def handle_signature(self, sig, signode):
        name, verbose_name = parse_directive(sig)
        signode += addnodes.desc_name(name, verbose_name)
        return name

    def add_target_and_index(self, name, sig, signode):
        verbose_name = parse_directive(sig)[1]
        targetname = '%s-%s' % (self.objtype, name)
        if name not in self.state.document.ids:
            signode['names'].append(name)
            signode['ids'].append(targetname)
            signode['first'] = not self.names
            self.state.document.note_explicit_target(signode)
            objects = self.env.domaindata['djangoadmin']['objects']
        self.env.domaindata['djangoadmin']['objects'][name] = (self.env.docname, self.objtype, verbose_name)
        return name


class DjangoAdminXRefRole(XRefRole):
    def process_link(self, env, refnode, has_explicit_title, title, target):
        title, target = super(DjangoAdminXRefRole, self).process_link(env, refnode, has_explicit_title, title, target)
        if not has_explicit_title:
            title = ""
        return title, target



class DjangoAdminDomain(Domain):
    """DjangoAdmin domain."""
    name = 'djangoadmin'
    label = 'DjangoAdmin'
    object_types = {
        'app': ObjType(l_('Django app'), 'app'),
        'class': ObjType(l_('Django model class'), 'class'),
        'attribute': ObjType(l_('Django model attribute'),   'attribute'),
    }

    directives = {
        'app': DjangoAdminObject,
        'class': DjangoAdminObject,
        'attribute':   DjangoAdminObject,
    }
    roles = {
        'app' :  DjangoAdminXRefRole(fix_parens=False),
        'class' :  DjangoAdminXRefRole(fix_parens=False),
        'attribute': DjangoAdminXRefRole(),
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
        for refname, (docname, type, verbose_name) in self.data['objects'].iteritems():
            yield (refname, refname, type, docname, refname, 1)
