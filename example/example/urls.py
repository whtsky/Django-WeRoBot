from django.conf.urls import patterns, url
from django_werobot import make_view

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from wechat_robot.robot import robot

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'example.views.home', name='home'),
    url(r'^robot/', make_view(robot)),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
