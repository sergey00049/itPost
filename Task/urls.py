from django.urls import path
from . import views

urlpatterns = [
    path('', views.TaskListView.as_view(), name='home'),
    path('tasks/add', views.TaskCreateView.as_view(), name='add'),
    path('tasks/<int:pk>/update', views.TaskUpdateView.as_view(), name='update'),
    path('tasks/<int:pk>/', views.TaskDetailView.as_view(), name='detail'),
    path('tasks/<int:pk>/delete', views.TaskDeleteView.as_view(), name='delete')
]
