from rest_framework import generics
from .models import Employee, Task
from .serializers import EmployeeSerializer, TaskSerializer


# Employee CRUD Views
class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all().order_by('-id')
    serializer_class = EmployeeSerializer


class EmployeeRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


# Task CRUD Views
class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all().order_by('-id')
    serializer_class = TaskSerializer


class TaskRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
