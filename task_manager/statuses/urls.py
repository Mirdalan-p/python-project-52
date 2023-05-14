from django.urls import path, include
from task_manager.statuses import views

urlpatterns = [
    path('', views.StatusesListView.as_view(), name='statuses_list'),
    path('create/', views.StatusCreateView.as_view(), name='create_status'),
    path('<int:pk>/delete/', views.StatusDeleteView.as_view(), name='status_delete'),
    path('<int:pk>/update/', views.StatusUpdateView.as_view(), name='status_update'),
]
