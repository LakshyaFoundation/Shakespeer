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
    url(r'^auth/$', TemplateView.as_view(template_name="backup.html")),
    url(r'^auth/register$', 'auth.views.register'),
    url(r'^auth/create_user$', 'auth.views.create_user'),
    url(r'^auth/login$', 'auth.views.login'),
    url(r'^auth/_login$', 'auth.views._login')
)
