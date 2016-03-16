from django.conf.urls import url
from .views import create_container, index

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^create-container/', create_container, name='create-container')
]
