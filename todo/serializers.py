from rest_framework import serializers
from todo.models import Todo

class TodoSerializer(serializers.ModelSerializer):
    """
    Todo Serializer.

    We are choosing to serialize to JSON
    the Todo model and the following fields
    -   id
    -   title
    -   description
    -   status
    -   updated
    """
    class Meta:
        model = Todo
        fields = ('id','title','description','status','updated')