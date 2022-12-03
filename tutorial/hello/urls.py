from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("maciej", views.maciej, name="maciej"),
    path("<str:name>", views.greet, name="greet")
]