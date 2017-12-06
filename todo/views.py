# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from todo.serializers import TodoSerializer
from todo.models import Todo

#   using a CLASS BASED VIEW
class TodoView(APIView):
    """
    TodoView used to handle the incoming requests relating to
    'todo' items
    """

    #   When we make a GET request to the server, it will auto
    #   invoke the get() method
    def get(self, request,pk=None):
        '''
        Retrieve a complete list of 'todo' items from the Todo model
        , serialize them to JSON and return the serialized todo items
        :param request:
        :return: serialized data
        '''

        if pk is None:
            #   Retrieve the items
            todo_items = Todo.objects.all()
            #   Serialize the data retrieved from the DB and serialize them
            #   using the 'TodoSerialize'
            serializer = TodoSerializer(todo_items, many=True)
            #   Store the serialized_data 'serialized_data'
            #   in the .data property of the object "serialized_data"
            #   e.g. JSON is at serialized_data.data
            serialized_data = serializer.data
            #   return the data in an instance of the Response object
            return Response(serialized_data)
        else:
            #   Retrieve the item
            todo = Todo.objects.get(id=pk)
            #   Serialize the data retrieved from the DB and serialize them
            #   using the 'TodoSerialize'
            serializer = TodoSerializer(todo)
            #   Store the serialized_data 'serialized_data'
            #   in the .data property of the object "serialized_data"
            #   e.g. JSON is at serialized_data.data
            serialized_data = serializer.data
            #   return the data in an instance of the Response object
            return Response(serialized_data)


    def post(self, request):
        """
        HANDLE the POST request for the 'todo' endpoint

        This view will take the 'data' property from the 'request' object
        and deserialize it into a Todo object and store it in the DB

        Returns a 201 (Successfully created)
        if the item is successfully
        created, otherwise returns a 400 (bad request)
        :param request:
        :return:
        """
        serializer = TodoSerializer(data=request.data)

        #   Check to see if the data in the request is valid
        #   If it cannot be desrialized into a Todo object then
        #   a bad request response will be returned containing the error
        #   Else, save the data and return the data successfully
        #   created status
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


    def put(self,request, pk):
        """
        Handle PUT request for the '/todo/' endpoint

        Retrieve a todo object based on the priimary key contained
        in the URL. Then takes the 'data' property from the 'request' object
        to update the relevant 'todo' instance

        Returns the updated object if the update was successful,
        otherwise 400 (bad request) is returned
        :param request:
        :param pk:
        :return: todo object or 400 response
        """
        todo = Todo.objects.get(id=pk)
        serializer = TodoSerializer(todo,data=request.data)

        #   Check to see if the data in the 'request' is valid
        #   If it cannot be deserialized into a Todo object then
        #   a bad request response will be returned containing the
        #   error. Else, save and return the data
        if not serializer.is_valid():
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer.save()
            return Response(serializer.data)


    def delete(self,request,pk):
        """
        Handle DELETE request for the '/todo/' endpoint.

        Retrieves a 'todo' instance based on the primary key contained
        in the URL and then deletes teh relevant instance.

        Returns a 204 (no content) status to indicate that the
        item was deleted
        :param request:
        :param pk:
        :return:
        """
        todo = Todo.objects.get(id=pk)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def todo_api_render(request):
    return render(request, 'todos/todo_api_render.html')