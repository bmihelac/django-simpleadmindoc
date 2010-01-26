from django.conf.urls.defaults import *

import views


urlpatterns = patterns('',
    url('^$',
        views.doc_index,
        name='simpleadmindoc-index'
    ),
    url('^models/(?P<app_label>[^\.]+)\.(?P<model_name>[^/]+)/$',
        views.model_detail,
        name='simpleadmindoc-model-details'
    ),
)
