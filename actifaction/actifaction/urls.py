from django.conf.urls import patterns, include, url
from django.contrib import admin

from actifaction import settings

admin.autodiscover()

urlpatterns = patterns('',
	# WEB
	(r'', include('web.urls')),

	# ADMIN
    url(r'^admin/', include(admin.site.urls)),

	# STATIC CONTENT
	url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)
