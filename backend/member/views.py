from django.shortcuts import render
from django.urls import path
from . import views
# Create your views here.

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from member.models import Member
from member.serializers import MemberSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from icecream import ic
class Auth(APIView):
    def get(self, request):
        ic(request)
        # data = JSONParser().parse(request)
        print('########### 저장 1 ##################')
        serializer = MemberSerializer(data=request)
        if serializer.is_valid():
            print('########### 저장 2 ##################')
            serializer.save()
        return Response({'result':'WELCOME'})


@csrf_exempt
def member_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':

        serializer = MemberSerializer()
        if serializer.is_valid():

            serializer.save()
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MemberSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)