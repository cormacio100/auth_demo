from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from entertainer import views
from accounts.views import UserView

app_name = 'entertainer'


urlpatterns = [
    url(r'^create_profile/$', views.create_profile, name='create_profile'),
]
