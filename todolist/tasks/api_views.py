#api

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Todo1
from .serializers import Todo1Serializer

class TodoAPI(APIView):
    #get
    def get(self,request):
        todos = Todo1.objects.all()
        serializer = Todo1Serializer(todos,many=True)
        return Response({
            'success':True,
            'messages':'All todo data retrieved successfully',
            'data':serializer.data
        },status=status.HTTP_200_OK)
    #post
    def post(self,request):
        serializer = Todo1Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'success':True,
                'message':'Task added successfully',
                'data':serializer.data,
            },status=status.HTTP_201_CREATED)
        return Response({
            'success':False,
            'message':'Invalid task data',
            'errors':serializer.errors
        },status=status.HTTP_400_BAD_REQUEST)
class TodoDetailAPI(APIView):
    def get_object(self,id):
        try:
            return Todo1.objects.get(id=id)
        except Todo1.DoesNotExist:
            return None
    #put
    def put(self,request,id):
        todo = self.get_object(id)
        if todo is None:
            return Response({
                'success':False,
                'message':'Task not found',
            },status=status.HTTP_404_NOT_FOUND)
        serializer = Todo1Serializer(todo,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'success':True,
                'message':'Task put updated successfully',
                'data':serializer.data,
            },status=status.HTTP_200_OK)
        return Response({
            'success':False,
            'message':'Invalid Task data',
            'errors':serializer.errors
        },status=status.HTTP_400_BAD_REQUEST)
    #patch
    def path(self,request,id):
        todo = self.get_object(id)
        if todo is None:
            return self.response({
                'success':False,
                'message':'task not found',
            },status=status.HTTP_404_NOT_FOUND)
        serializer = Todo1Serializer(todo,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'success':True,
                'message':'Task patch updated successfully',
                'data':serializer.data,
            },status=status.HTTP_200_OK)
        return Response({
            'success':False,
            'message':'Invalid Task data',
            'errors':serializer.errors
        },status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        todo = self.get_object(id)
        if todo is None:
            return Response({
                'success':False,
                'message':'Task not found',
            },status=status.HTTP_404_NOT_FOUND)
        todo.delete()
        return Response({
            'success':True,
            'message':'Task deleted successfully',
        },status=status.HTTP_200_OK)
        

        

