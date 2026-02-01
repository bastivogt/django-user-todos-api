from rest_framework import serializers

from todo_app import models


class CategorySerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")

    def create(self, validated_data):
        request = self.context.get("request")
        item = models.Category.objects.create(user=request.user, **validated_data)
        return item

    
    class Meta:
        model = models.Category
        fields = "__all__"


class TodoSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")
    

    def create(self, validated_data):
        request = self.context.get("request")
        categories = validated_data.pop("categories")
        item = models.Todo.objects.create(user=request.user, **validated_data)
        item.categories.set(categories)
        item.save()
        return item
        

    class Meta:
        model = models.Todo
        fields = "__all__"