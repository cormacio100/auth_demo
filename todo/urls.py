from django.conf.urls import url
from todo.views import TodoView

# specific app URL pointable from template
app_name = 'todo'

urlpatterns = [
    #   we need to invoke the as_view method on the TodoView class
    #   Any view that inherits from the base View object will have the as_view method
    #   This will allow Django to use the class-based view as a standard function-based view.
    url(r'^$',TodoView.as_view())
]