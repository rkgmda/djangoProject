from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('userlist/', views.userlist, name="userlist"),
]