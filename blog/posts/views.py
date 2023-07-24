from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

# Create your views here.
def index(request):
    posts=Project.objects.all()
    return render(request,'index.html',{'posts':posts})
def post(request,pk):
    posts=Project.objects.get(id=pk)
    return render(request,'post.html',{'post':posts})