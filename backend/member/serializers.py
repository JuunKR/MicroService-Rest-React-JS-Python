from rest_framework import serializers
from .models import MemberVO as member
from icecream import ic

class MemberSerializer(serializers.Serializer):
    # pk인 id는 99퍼센트 수정 안 할 것이므로 read_only
    username = serializers.CharField()
    password = serializers.CharField()
    name = serializers.CharField()
    email = serializers.EmailField()
    class Meta:
        model = member
        fields = '__all__'

    def create(self, validated_data):
        return member.objects.create(**validated_data)

    # 책에 있던거 더이상 안먹음
    # def update2(self, instance, validated_data):
    #     # id, created_at, updated_at은 read only 필드이므로 update method에서는 제외함
    #     # 'author'에 새로 들어오는 데이터가 없으면 이미 가지고 있는 instance.author를 사용함 (즉, 기존 데이터 유지)
    #     instance.username = validated_data.get('username', instance.username)
    #     instance.password = validated_data.get('password', instance.password)
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.email = validated_data.get('email', instance.email)
    #     return instance

    def update(self, instance, validated_data):
        # demo = member.objects.get(pk=instance.username)
        member.objects.filter(pk=instance.username) \
            .update(**validated_data)
        return member