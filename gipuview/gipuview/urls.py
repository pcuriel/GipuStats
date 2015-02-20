from django.conf.urls import patterns, include, url
from django.contrib import admin
from townsnapshot.views import MunicipioDetailView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gipuview.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^city/(?P<pk>[-_\w]+)/$', MunicipioDetailView.as_view(), name='detail'),
    url(r'^admin/', include(admin.site.urls)),
)
