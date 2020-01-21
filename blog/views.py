from django.shortcuts import render

def hello_world(request):
    context ={'curso':'Django 3'}
    return render(request,'indexgeral.html',context)

