from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.conf import settings


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'crowdfunding.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^index$', TemplateView.as_view(template_name="index.html")),
)
