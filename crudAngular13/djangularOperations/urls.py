from django.urls import re_path as url
from djangularOperations import views

urlpatterns = [
    url(r'^articles$', views.article_list),
    url(r'^articles/(?P<pk>[0-9]+)$', views.article_detail),
    url(r'^articles/published$', views.article_list_published)
]
