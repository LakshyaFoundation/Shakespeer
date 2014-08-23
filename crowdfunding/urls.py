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
    url(r'^auth/register$', TemplateView.as_view(template_name="register.html")),
    url(r'^auth/login$', TemplateView.as_view(template_name="login.html")),
    url(r'^project/$', TemplateView.as_view(template_name="project.html")),
)
