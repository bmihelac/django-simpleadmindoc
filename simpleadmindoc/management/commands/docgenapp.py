from django.core.management.base import AppCommand


class Command(AppCommand):
    help = "Generate sphinx documentation for given apps."
    
    def handle_app(self, app, **options):
        # check if simpleadmindoc directory is setup
        from django.db import models
        from simpleadmindoc.generate import generate_model_doc, generate_app_doc, generate_index_doc
        generate_index_doc()
        generate_app_doc(app)
        for model in models.get_models(app):
            generate_model_doc(model)
        
