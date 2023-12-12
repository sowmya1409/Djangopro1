"""
URL configuration for PI_Proj1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, re_path, include  # 3.1 re_path is regular expression path it is used to match the text
from Hello import views                         # 3.2 from Hello app we have imported views
# include is imported to

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$',views.index,name="index"),  #3.3 from views call the function index by name(anything) it will match the func index and call the index func in views
    re_path(r'^Hello/',include('Hello.urls')),  #3.4
]
#r raw character means dont consider the character as special character