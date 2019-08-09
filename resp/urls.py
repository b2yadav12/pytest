from django.urls import path

from . import views

app_name='resp'

urlpatterns = [
    path('html', views.html, name="html"),
    path('json', views.json, name="json"),
]