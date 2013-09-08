from django.conf.urls import include
from django.conf.urls import patterns
from django.conf.urls import url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'video_manager.views.index', name='index'),
    url(r'^vote/', 'video_manager.views.vote', name='vote'),

    # User Login
    url(r'^google/login/$', 'django_openid_auth.views.login_begin', name='openid-login'),
    url(r'^google/login-complete/$', 'django_openid_auth.views.login_complete', name='openid-complete'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/',}, name='logout'),

    # Administration
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)
