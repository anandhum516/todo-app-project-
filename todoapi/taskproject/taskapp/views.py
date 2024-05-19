from django.shortcuts import render
from  rest_framework import viewsets
from taskapp.serializers import TaskSerializer, UserSerializer
from taskapp.models import Task
from django.contrib.auth.models import User

# Create your views here.
class AllTasks(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class NotcompletedTasks(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        qs=self.queryset
        queryset=qs.filter(completed=False)

        return queryset


class CompletedTasks(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        qs = self.queryset
        queryset = qs.filter(completed=False)

        return queryset

class CreateUser(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
