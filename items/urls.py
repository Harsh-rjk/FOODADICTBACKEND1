from . import views
from django.urls import path
urlpatterns = [
  path('', views.items),
  path('get/', views.get_items),
    path('post/', views.create_item)
]

