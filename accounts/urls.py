from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from accounts import views
from accounts.views import UserView, auth_register

app_name = 'accounts'

urlpatterns = [
    url(r'^register/$', views.auth_register, name='register'),
    url(r'^profile/', views.auth_profile, name='profile'),
    url(r'^login/', views.auth_login, name='login'),
    url(r'^logout/', views.auth_logout, name='logout'),
    url(r'^test/', views.test, name='test'),
    url(r'^register_api/$',UserView.as_view()), # provide email and password
    #   JWT based on the username(email) and password
    url(r'^api-token-auth/$',obtain_jwt_token)  # provide email and password
]
