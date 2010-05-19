from optparse import make_option

from django.core.management.base import AppCommand


class Command(AppCommand):
    help = "Generate sphinx documentation skeleton for given apps."
    option_list = AppCommand.option_list + (
            make_option('--locale', '-l', default=None, dest='locale',
                help='Use given locale'),
        )    
    
    def handle_app(self, app, **options):
        # check if simpleadmindoc directory is setup
        locale = options.get('locale', None)
        if locale:
            from django.utils import translation
            translation.activate(locale)
            
        from django.db import models
        from simpleadmindoc.generate import generate_model_doc, generate_app_doc, generate_index_doc,\
                                            generate_apps_doc
        generate_index_doc()
        generate_apps_doc()
        generate_app_doc(app)
        for model in models.get_models(app):
            generate_model_doc(model)
        
