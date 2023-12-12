from django.contrib import admin
from django.urls import path, re_path   #4.0
from Hello import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$',views.Hello,name="Hello"),
    re_path(r'^List/',views.list_view, name='list_view'),  # this is from views with list_view
]

