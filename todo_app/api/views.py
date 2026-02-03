from django.http import HttpResponse
from rest_framework import generics
from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework.permissions import IsAuthenticated

from todo_app.api import serializers
from todo_app import models


# Category
class CategoryListView(generics.ListCreateAPIView):
    # queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        current_user = self.request.user
        qs = models.Category.objects.filter(user=current_user)
        return qs
    
    # cleverer
    def perform_create(self, serializer):
        current_user = self.request.user
        serializer.save(user=current_user)

    # def get_serializer_context(self):
    #     context = super().get_serializer_context()
        
    #     # Add the request object to the context dictionary
    #     context["request"] = self.request
    #     return context

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    # queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        current_user = self.request.user
        qs = models.Category.objects.filter(user=current_user)
        return qs



class CategorieTodosView(generics.ListAPIView):
    serializer_class = serializers.TodoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        current_user = self.request.user
        pk = self.kwargs.get("pk")
        item = models.Category.objects.get(pk=pk, user=current_user)

        return item.todos.all()




class TodoListView(generics.ListCreateAPIView):
    serializer_class = serializers.TodoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        current_user = self.request.user
        qs = models.Todo.objects.filter(user=current_user)
        return qs
    
    # cleverer
    def perform_create(self, serializer):
        current_user = self.request.user
        serializer.save(user=current_user)


    # def get_serializer_context(self):
    #     context = super().get_serializer_context()
        
    #     # Add the request object to the context dictionary
    #     context["request"] = self.request
    #     return context
    

class TodoDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.TodoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        current_user = self.request.user
        qs = models.Todo.objects.filter(user=current_user)
        return qs
    

class TodoCategoriesView(generics.ListAPIView):
    serializer_class = serializers.CategorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        pk = self.kwargs.get("pk")
        current_user = self.request.user
        item = models.Todo.objects.get(pk=pk, user=current_user)
        return item.categories.filter(user=current_user)






def index(request):
    return HttpResponse("Hello Todos")