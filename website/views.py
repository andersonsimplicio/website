from django.shortcuts import render, HttpResponse
from .models import Post
# Create your views here.

def hello_blog(request):
    list_posts = Post.objects.all()
    lista = ['Python','Django','Html','Banco de Dados']
    data = {'name': 'Curso Django 3',
            'lista_tech':lista,
            'posts':list_posts,
            }
    return render(request,'index.html',data)

def post_detail(request,id):
    post = Post.objects.get(id=id)
    return render(request,'post_detail.html',{'post':post})