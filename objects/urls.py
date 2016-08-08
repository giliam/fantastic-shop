from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from objects import views

urlpatterns = [
    url(r'^objects/$', views.ObjectList.as_view()),
    url(r'^objects/(?P<pk>[0-9]+)/$', views.ObjectDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)