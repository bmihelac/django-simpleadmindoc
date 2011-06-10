from optparse import make_option

from django.core.management.base import AppCommand


class Command(AppCommand):
    help = "Generate sphinx documentation skeleton for given apps."
    option_list = AppCommand.option_list + (
            make_option('--locale', '-l', default=None, dest='locale',
                help='Activate given locale, verbose names for models and' +
                'attributes will be in given locale. '),
            make_option('--exclude-from', default=None, dest='exclude_filename',
                help='Exclude patterns for models that you do not want'+
                'documentation to be generated for.', metavar="FILE"),
            make_option('--path', default='docs', dest='path',
                help="Specify path where to save skeleton documentation." +
                "All existing files would be overwritten."),
        )

    def handle_app(self, app, **options):
        # check if simpleadmindoc directory is setup
        locale = options.get('locale', None)
        if locale:
            from django.utils import translation
            translation.activate(locale)
        excludes = []
        exclude_filename = options.get('exclude_filename', None)
        if exclude_filename:
            f = open(exclude_filename)
            for line in f:
                excludes.append(line.strip())

        from django.db import models
        from simpleadmindoc.generate import (generate_model_doc,
                generate_app_doc)

        path = options.get('path')
        generate_app_doc(app)
        for model in models.get_models(app):
            if "%s.%s" % (model._meta.app_label, model.__name__) not in excludes:
                generate_model_doc(model, path)

