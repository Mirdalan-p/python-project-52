from django.urls import path
from task_manager.labels import views

urlpatterns = [
    path('', views.LabelsListView.as_view(), name='labels_list'),
    path('create/', views.LabelsCreateView.as_view(), name='create_label'),
    path('<int:pk>/delete/', views.LabelsDeleteView.as_view(),
         name='label_delete'),
    path('<int:pk>/update/', views.LabelsUpdateView.as_view(),
         name='label_update'),
]
