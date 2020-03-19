from django.conf.urls import re_path, url

from adv_cbv import views

app_name = 'adv_cbv'

urlpatterns = [
    re_path(r'^$', view=views.SchoolListView.as_view(), name='list'),
    re_path(r'^(?P<pk>\d+)/$', view=views.SchoolDetailView.as_view(), name='detail'),
    re_path(r'^create/$', view=views.SchoolCreateView.as_view(), name='create'),
    re_path(r'^update/(?P<pk>\d+)/$', view=views.SchoolUpdateView.as_view(), name='update'),
    re_path(r'^delete/(?P<pk>\d+)/$', view=views.SchoolDeleteView.as_view(), name='delete'),
]