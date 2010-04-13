from optparse import make_option

from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Create rest document for given model."
    args = "app_label,model_name"
    label = 'file'
    option_list = BaseCommand.option_list + (
    #     make_option('--root', action="store", type="string", dest="root_id",
    #         help='Append structure to Page with primary key of ROOT_ID'),
    #     make_option('--delete_all', action="store_true", dest="delete_all",
    #         help='Remove all pages before importing'),
    # )

    def handle(self, *filenames, **options):
        # f = open(filenames[0])
        # root_id = options.get('root_id')
        # if options.get('delete_all'):
        #     from feincms.module.page.models import Page
        #     Page.objects.all().delete()
        # from feincmsext.util.structure import import_structure
        # import_structure(f, root_id)
        return

                    
