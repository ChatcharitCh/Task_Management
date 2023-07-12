#import part

from django.urls import path
from taskapp import views

urlpatterns = [path('',views.index)]