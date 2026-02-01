from django.contrib import admin
from todo_app import models

class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "user"
    ]

    list_display_links = [
        "id",
        "name"
    ]

    list_filter = [
        "user",
        "created_at",
        "updated_at"
    ]


class TodoAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "done",
        "user",
        "created_at",
        "updated_at"
    ]

    list_display_links = [
        "id",
        "title"
    ]

    list_filter = [
        "done",
        "created_at",
        "updated_at"
    ]

    

    search_fields = [
        "title",
        "content"
    ]

admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Todo, TodoAdmin)
