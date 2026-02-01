from django.urls import path

from todo_app.api import views

app_name = "todo_app"
urlpatterns = [
    path("", views.index),
    path("category/list/", views.CategoryListView.as_view(), name="category-list"),
    path("category/<int:pk>/", views.CategoryDetailView.as_view(), name="category-detail"),
    path("category/<int:pk>/todos/", views.CategorieTodosView.as_view(), name="category-todos"),



    path("todo/list/", views.TodoListView.as_view(), name="todo-list"),
    path("todo/<int:pk>/", views.TodoDetailView.as_view(), name="todo-detail"),

    # "todo/<int:pk>/category/list/"
    path("todo/<int:pk>/categories/", views.TodoCategoriesView.as_view(), name="todo-categories"),
]