from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.level_list, name='level_list'),
]