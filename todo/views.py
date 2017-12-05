# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
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
    def get(self, request):
        '''
        Retrieve a complete list of 'todo' items from the Todo model
        , serialize them to JSON and return the serialized todo items
        :param request:
        :return: serialized data
        '''

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

