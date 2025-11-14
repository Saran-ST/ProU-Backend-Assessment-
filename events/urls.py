from django.urls import path
from .views import DashboardStatsView

from .views import (
    EmployeeListCreateView,
    EmployeeDetailView,
    TaskListCreateView,
    TaskDetailView,
)

urlpatterns = [
    path('employees/', EmployeeListCreateView.as_view(), name='employee-list'),
    path('employees/<int:pk>/', EmployeeDetailView.as_view(), name='employee-detail'),
    path('dashboard/', DashboardStatsView.as_view(), name='dashboard-stats'),
    path('tasks/', TaskListCreateView.as_view(), name='task-list'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
]
