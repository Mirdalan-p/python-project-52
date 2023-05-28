from django.urls import path
from task_manager.users import views

urlpatterns = [
    path('', views.UsersListView.as_view(), name='users_list'),
    path('create/', views.UserCreateView.as_view(),
         name='create_user'),
    path('<int:pk>/delete/', views.UserDeleteView.as_view(),
         name='user_delete'),
    path('<int:pk>/update/', views.UserUpdateView.as_view(),
         name='user_update'),
]
