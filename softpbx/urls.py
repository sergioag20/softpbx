# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'softpbx.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'softpbx.views.index'),
    url(r'^user_login', 'softpbx.views.user_login'),
    url(r'^user_logout', 'softpbx.views.user_logout'),
    # url(r'^add_user', 'cdr.views.add_user'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


urlpatterns += patterns('spw_extension.views',
    url(r'^add-extension', 'add_extension'),
)