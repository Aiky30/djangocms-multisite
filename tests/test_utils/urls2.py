# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from cms.utils.conf import get_cms_setting
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.i18n import javascript_catalog
from django.views.static import serve
from djangocms_multisite.urlresolvers import cms_multisite_url

admin.autodiscover()

urlpatterns = [
    url(r'^media/(?P<path>.*)$', serve,
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'^media/cms/(?P<path>.*)$', serve,
        {'document_root': get_cms_setting('MEDIA_ROOT'), 'show_indexes': True}),
    url(r'^jsi18n/(?P<packages>\S+?)/$', javascript_catalog),
]

try:
    import taggit_autosuggest
    urlpatterns.append(url(r'^taggit_autosuggest/', include('taggit_autosuggest.urls')))
except ImportError:
    pass

urlpatterns += staticfiles_urlpatterns()

urlpatterns += i18n_patterns(
    url(r'^admin/', include(admin.site.urls)),
    cms_multisite_url(r'^subpath/', include('cms.urls'), name='cms-urls'),
)
