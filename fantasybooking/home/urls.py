from .views import error, ExampleFormView

from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from fantasybooking.home.views import wrestlers, create_stable

from django.views.generic.base import TemplateView


urlpatterns = [
    url(r'^error/', error, name='error'),
    url(r'^$', TemplateView.as_view(template_name="index.jinja"), name="home"),
    url(r'^form/', ExampleFormView.as_view(), name="Example Form"),
    url(r'^wrestlers/', wrestlers, name='wrestlers'),
    url(r'^create_stable/', create_stable, name='create stable'),
    url(r'^match/', match, name='match'),
]
