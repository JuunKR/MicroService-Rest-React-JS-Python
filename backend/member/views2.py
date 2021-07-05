from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework import status
from member.models import MemberVO
from member.serializers import MemberSerializer
from rest_framework.decorators import api_view, parser_classes
from icecream import ic
from rest_framework.response import Response
from rest_framework import serializers
from django.http import HttpResponse, JsonResponse, Http404


@api_view(['GET', 'POST', 'DELETE'])
@parser_classes([JSONParser])
def members(request):
    print('=== 여기까지는 왔다 !! ')
    if request.method == 'GET':
        all_members = MemberVO.objects.all()
        serializer = MemberSerializer(all_members, many=True)
        return JsonResponse(data=serializer.data, safe=False)

    elif request.method == 'POST':
        new_member = request.data['body']
        ic(new_member)
        serializer = MemberSerializer(data=new_member)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        serializer = MemberSerializer()
        return JsonResponse(serializer.data, safe=False)

@api_view(['GET', 'PUT', 'DELETE'])
def member(request, pk):
    if request.method == 'GET':
        serializer = MemberSerializer()
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'PUT':
        serializer = MemberSerializer()
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'DELETE':
        serializer = MemberSerializer()
        return JsonResponse(serializer.data, safe=False)


@api_view(['Post'])
def login(request):
    data = request.data['body']
    pk = data['username']
    user_input_password = data['password']
    member = get_object(pk)
    if user_input_password == member.password:
        return Response({'result': 'you are logged in'}, status=201)
    return HttpResponse(status=104)
    # print(type(member)): when pk is correct, <class 'member.models.MemberVO'>
    # print(member.pk) = print(member.username)

def get_object(pk):
    try:
        return MemberVO.objects.get(pk=pk)
    except MemberVO.DoesNotExist:
        raise Http404