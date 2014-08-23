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
    url(r'^auth/$', TemplateView.as_view(template_name="auth/login.html")),
    url(r'^$', TemplateView.as_view(template_name="index.html")),
)
