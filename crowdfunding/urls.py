from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'crowdfunding.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^auth/$', TemplateView.as_view(template_name="login.html")),
    url(r'^auth/register$', 'auth.views.register'),
    url(r'^auth/create_user$', 'auth.views.create_user'),
    url(r'^auth/login$', 'auth.views.__login'),
    url(r'^auth/logout$', 'auth.views._logout'),
    url(r'^auth/_login$', 'auth.views._login'),
    url(r'^project/$', 'project.views.show_project'),
    url(r'^project/show/(?P<id>[0-9]+)/$', 'project.views.show_project_page', name='show_project_page'),    
    url(r'^project/create$', 'project.views.create_project'),
    url(r'^project/update$', 'project.views.update_project'),
    url(r'^project/get_update_content$', 'project.views.get_update_content'),
    url(r'^project/save_project_update$', 'project.views.save_project_update'),
    url(r'^project/save_project$', 'project.views.save_project'),
    url(r'^project/pledge$', 'project.views.pledge'),
    url(r'^project/save_pledge$', 'project.views._pledge'),
    url(r'^project/update_pledge$', 'project.views.update_pledge'),
    url(r'^profile/(?P<uid>[0-9]+)$', 'auth.views.profile',name='profile'),
    url(r'', include('social_auth.urls')),
)

from django.conf import settings
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
        }),
)

