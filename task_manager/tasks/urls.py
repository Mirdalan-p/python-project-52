from django.urls import path, include
from task_manager.tasks import views

urlpatterns = [
    path('', views.TaskListView.as_view(), name='tasks_list'),
    path('create/', views.TaskCreateView.as_view(), name='create_task'),
    path('<int:pk>/delete/', views.TaskDeleteView.as_view(), name='task_delete'),
    path('<int:pk>/update/', views.TaskUpdateView.as_view(), name='task_update'),
    path('<int:pk>/', views.TaskView.as_view(), name='task_view'),
]
