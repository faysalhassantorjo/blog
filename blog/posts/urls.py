from django.urls import path
from .import views
urlpatterns=[
    path('',views.index,name='views'),
    path('post/<str:pk>',views.post,name='post')
]