from django.urls import path

from SketchApp import views

urlpatterns=[
    path('',views.homepage,name='homepage'),
    path('portrait_page',views.portrait_page,name='portrait_page'),

]