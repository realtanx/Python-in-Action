from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("<int:qs_id>/", views.detail),
    path("<int:qs_id>/results/", views.results),
    path("<int:qs_id>/vote/", views.vote),
]