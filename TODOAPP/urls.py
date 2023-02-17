from django.urls import path

from . views import *
from . import views

urlpatterns = [

    path('register/',Register.as_view()),
    path('Todo/',TodoAPIView.as_view()),
    path('Todo/<str:pk>/',TodoAPIView.as_view()),
    path('mail/',views.sendmail)

]
