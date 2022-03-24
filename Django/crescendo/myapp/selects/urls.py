from django.urls import path
from . import views

app_name = "selects"

urlpatterns = [
    path("", views.selects, name="selects"),
]