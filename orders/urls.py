from . import views
from django.urls import path
urlpatterns = [
  path('', views.orders),
  path("get/", views.get),
  path("post/", views.post)
]