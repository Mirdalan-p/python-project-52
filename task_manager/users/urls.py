from django.contrib import admin
from django.urls import path, include
from task_manager.users import views

urlpatterns = [
    path('', views.UsersListView.as_view(), name='users_list'),
    path('create/', views.UserCreateView.as_view(), name='create_user'),
]
