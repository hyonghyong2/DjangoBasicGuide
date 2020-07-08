"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from community.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('write/', write, name='write'),
    path('list/', list, name='list'),
    path('view/<int:num>/',view), #url과 path의 차이: #https://stackoverflow.com/questions/47947673/is-it-better-to-use-path-or-url-in-urls-py-for-django-2-0
]

