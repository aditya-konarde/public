from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
# $ is the default/home view
]
