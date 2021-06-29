from rest_framework import serializers
from .models import Post

class BoardSerializer(serializers.Serializer):
    # id = serializers.CharField(primary_key=True)
    title = serializers.CharField(max_length=30)
    content = serializers.CharField()
    created_at = serializers.DateTimeField(auto_now=True)
    updated_at = serializers.DateTimeField(auto_now=True)

    def create(self, validated_data):
        return Post.objects.create(**validated_data) #딕셔너리
