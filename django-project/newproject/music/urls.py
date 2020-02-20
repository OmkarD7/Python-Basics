from django.urls import path
from . import views
urlpatterns = [
    path("", views.home),
    path("<int:album_id>", views.detail)
]