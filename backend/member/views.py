from django.shortcuts import render
from django.urls import path
from . import views
# Create your views here.

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from member.serializers import MemberSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from icecream import ic
from django.http import Http404
from member.models import MemberVO as member


class Members(APIView):
    def post(self, request):
        data = request.data['body']
        ic(data)
        serializer = MemberSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'result': f'Welcome, {serializer.data.get("name")}'}, status=201)
        ic(serializer.errors)
        return Response(serializer.errors, status=400)

class Member(APIView):
    def post(self, request):
        data = request.data['body']
        pk = data['username']
        user_input_password = data['password']
        member = self.get_object(pk)
        if user_input_password == member.password:
            return Response({'result': 'you are logged in'}, status=201)
        return HttpResponse(status=104)

    @staticmethod
    def get_object(pk):
        try:
            return member.objects.get(pk=pk)
        except member.DoesNotExist:
            ic('으아아')
            raise Http404


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