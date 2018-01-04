"""auth_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from accounts import views as accounts_views
from hello import views as hello_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^$', hello_views.get_index, name='index'),
    url(r'^form/',hello_views.test_form,name='test_form'),
    url(r'^todo/', include('todo.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^entertainer/', include('entertainer.urls')),
    url(r'^blog/', include('blog.urls')),
    #url(r'', include('blog.urls'))
]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)