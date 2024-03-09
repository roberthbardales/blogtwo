#
from django.urls import path
from . import views


app_name = "core_app"

urlpatterns = [
    path('',views.home,name='home'),
    path('post/',views.post,name='post'),
    path('category/',views.post,name='category'),
    path('author/',views.post,name='author'),
    path('dates/',views.post,name='dates'),



]