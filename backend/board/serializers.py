from rest_framework import serializers
from .models import PostVO as post

class BoardSerializer(serializers.Serializer):
    # id = serializers.CharField(primary_key=True)
    title = serializers.CharField()
    content = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    class Meta:
        model = post
        fields = '__all__'

    def create(self, validated_data):
        return post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # id, created_at, updated_at은 read only 필드이므로 update method에서는 제외함
        # 'author'에 새로 들어오는 데이터가 없으면 이미 가지고 있는 instance.author를 사용함 (즉, 기존 데이터 유지)
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)

        return instance