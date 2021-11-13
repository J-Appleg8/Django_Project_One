from django.urls import path
from . import views

urlpatterns = [
    # Homepage view
    path("", views.index, name="index"),
]
