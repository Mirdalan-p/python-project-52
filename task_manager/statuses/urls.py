from django.urls import path, include
from task_manager.statuses import views

urlpatterns = [
    path('', views.StatusesListView.as_view(), name='statuses_list'),
    path('create/', views.StatusCreateView.as_view(), name='create_status'),
    #path('<int:pk>/delete/', views.UserDeleteView.as_view(), name='user_delete'),
    #path('<int:pk>/update/', views.UserUpdateView.as_view(), name='user_update'),
]
