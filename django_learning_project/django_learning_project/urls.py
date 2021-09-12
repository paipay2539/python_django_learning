"""django_learning_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, re_path
from app_01 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello1, name='hello1'),
    path('hello/<int:id>/abc-def/', views.hello2_1, name='hello2_1'),
    re_path(r'hello/(?P<year>[0-9]{4})/(?P<slug>[\w-]+)/$', views.hello2_2, name='hello2_2'),
    re_path(r'hello/(?P<year>[0-9]{4})/(?P<slug>[\w-]+)', views.hello3, name='hello3'),

    # + : free, {4} : only 4 char
    # pattern : (?P<variable_name> )
    # [0-9] : digit, [\w-] : word that join by '-'
    # http://localhost:8000/hello_re/1234/abc-def
    # last / is effect
    # if same condition it will use first match condition path(..) on this file
    # 2_1 is same condition with 2_2 it will use 2_1
    # re_path ..) : endurl, ..)/$ : endurl/
    # path <int:id> : 123, <int:id>/ : 123/
]
