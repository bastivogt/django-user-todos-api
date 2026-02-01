from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth import get_user_model

from sevo_core.models import BaseTimeStampMixin


User = get_user_model()


class Category(BaseTimeStampMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("user"))
    name = models.CharField(max_length=100, verbose_name=_("name"))

    def __str__(self):
        return f"{self.name} ({self.user.username})"

    class Meta:
        ordering = [
            "updated_at"
        ]
        verbose_name_plural = "Categories"



class Todo(BaseTimeStampMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("user"))
    categories = models.ManyToManyField(Category, blank=True, related_name="todos", verbose_name=_("categories"))
    title = models.CharField(max_length=255, verbose_name=_("title"))
    content = models.TextField(verbose_name="content")
    done = models.BooleanField(default=False, verbose_name=_("done"))

    def __str__(self):
        return f"{self.title} ({self.user.username})"

    class Meta:
        ordering = [
            "updated_at"
        ]

