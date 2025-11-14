from rest_framework import generics, filters
from .models import Employee, Task
from .serializers import EmployeeSerializer, TaskSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


# ---------------------------
# EMPLOYEES LIST + CREATE
# ---------------------------
class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    # BONUS FEATURES
    search_fields = ['name', 'email']
    ordering_fields = ['created_at']
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
    ]


# ---------------------------
# EMPLOYEE DETAIL (GET/PUT/DELETE)
# ---------------------------
class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


# ---------------------------
# TASKS LIST + CREATE
# ---------------------------
class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    # BONUS FEATURES
    filterset_fields = ['status', 'employee']
    search_fields = ['title', 'description']
    ordering_fields = ['created_at', 'due_date']
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
    ]


# ---------------------------
# TASK DETAIL (GET/PUT/DELETE)
# ---------------------------
class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class DashboardStatsView(APIView):
    """
    Dashboard analytics for employees and tasks.
    """
    def get(self, request):
        total_employees = Employee.objects.count()
        total_tasks = Task.objects.count()

        completed_tasks = Task.objects.filter(status='completed').count()
        pending_tasks = Task.objects.filter(status='pending').count()
        in_progress_tasks = Task.objects.filter(status='in_progress').count()

        data = {
            "total_employees": total_employees,
            "total_tasks": total_tasks,
            "completed_tasks": completed_tasks,
            "pending_tasks": pending_tasks,
            "in_progress_tasks": in_progress_tasks,
        }

        return Response(data)
