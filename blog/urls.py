from django.conf.urls import url
import views

app_name = 'blog'

urlpatterns = [
    url(r'^list/$', views.post_list, name="list"),
]
