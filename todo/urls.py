from django.conf.urls import url
from todo.views import TodoView
from . import views

# specific app URL pointable from template
app_name = 'todo'

urlpatterns = [
    #   we need to invoke the as_view method on the TodoView class
    #   Any view that inherits from the base View object will have the as_view method
    #   This will allow Django to use the class-based view as a standard function-based view.
    url(r'^$',TodoView.as_view(), name='todo_all'),
    url(r'^todo_api_render/', views.todo_api_render, name='todo_api_render'),
    url(r'^(?P<pk>[0-9]+)/$',TodoView.as_view())
]


'''
    1 click link in base template to link to view
    2 view loads template containing the JSON REQUEST
    3 template renders the data
'''