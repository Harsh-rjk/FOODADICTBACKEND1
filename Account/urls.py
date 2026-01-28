from . import views
from django.urls import path
urlpatterns = [
  path('', views.account),
  path('get/',  views.get),
    path('post/',  views.post)
 
]