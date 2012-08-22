from optparse import make_option

from django.core.management.base import LabelCommand


class Command(LabelCommand):
    help = "Generate Sphinx documentation skeleton for given models."
    option_list = LabelCommand.option_list + (
            make_option('--locale', '-l', default=None, dest='locale',
                help='Activate given locale, verbose names for models and' +
                'attributes will be in given locale. '),
        )

    def handle_label(self, label, **options):
        locale = options.get('locale', None)
        if locale:
            from django.utils import translation
            translation.activate(locale)

        from django.db import models
        from simpleadmindoc.util import get_model
        from simpleadmindoc.generate import model_doc

        print model_doc(get_model(*label.split('.')))

