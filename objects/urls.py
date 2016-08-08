from django.conf.urls import url
from objects import views

urlpatterns = [
    url(r'^objects/$', views.object_list),
    url(r'^objects/(?P<pk>[0-9]+)/$', views.object_detail),
]
