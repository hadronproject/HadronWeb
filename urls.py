from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from settings import MEDIA_ROOT
admin.autodiscover()

urlpatterns = patterns('',
    # reader urls:
    url(r'^$', 'apps.frontend.views.index', name='index'),
    url(r'^news/(?P<slug>[^\.]+)', 'apps.frontend.views.news_detail', name='news_detail'),
    url(r'^news/', 'apps.frontend.views.news_list', name='news_list'),
    url(r'^page/(?P<slug>[^\.]+)', 'apps.frontend.views.page_detail', name='page_detail'),
    url(r'^developers/', 'apps.frontend.views.developers', name='developers'),
    # for images
    url(r'^media/images/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT+'/images/'}),

    # documents urls:
    url(r'^docs/(?P<slug>[^\.]+)', 'apps.documents.views.document_detail', name='document_detail'),
    url(r'^docs/', 'apps.documents.views.index', name='index'),

    # url(r'^hadronweb/', include('hadronweb.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
