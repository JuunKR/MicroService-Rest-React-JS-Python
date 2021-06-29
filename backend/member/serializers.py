from rest_framework import serializers
from .models import Member
from icecream import ic

class MemberSerializer(serializers.Serializer):
    # pk인 id는 99퍼센트 수정 안 할 것이므로 read_only
    username = serializers.models.CharField()
    password = serializers.CharField()
    name = serializers.CharField()
    email = serializers.EmailField()
    class Meta:
        model = Member
        fields = ['username', 'password', 'name', 'email']

    def create(self, validated_data):
        return Member.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # id, created_at, updated_at은 read only 필드이므로 update method에서는 제외함
        # 'author'에 새로 들어오는 데이터가 없으면 이미 가지고 있는 instance.author를 사용함 (즉, 기존 데이터 유지)
        instance.username = validated_data.get('username', instance.username)
        instance.password = validated_data.get('password', instance.password)
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        return instance