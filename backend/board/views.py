from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from board.serializers import BoardSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from icecream import ic


class Boards(APIView):
    def post(self, request):
        data = request.data['body']
        ic(data)
        serializer = BoardSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'result': f'Welcome, {serializer.data.get("title")}'}, status=201)
        ic(serializer.errors)
        return Response(serializer.errors, status=400)

class Board(APIView):
    def get(self, request):
        pass


@csrf_exempt
def board_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':

        serializer = BoardSerializer()
        if serializer.is_valid():

            serializer.save()
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BoardSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)