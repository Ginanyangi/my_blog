from django.shortcuts import render, redirect
from .models import Blog,Subscriber
from django.contrib import messages
# Create your views here.

def index(request):
    blogs = [
        {'title': 'Learning  Django', 'content': 'Django is an awesome open source framework for building APIs using Django REST framework', 'author':'John Doe', 'date': '04.06.2024'},
         {'title': 'Learning  Django', 'content': 'Django is an awesome open source framework for building APIs using Django REST framework', 'author':'John Doe', 'date': '04.06.2024'},
    ]

    context ={'blogs': blogs}
    return render(request, 'index.html',context)

def about(request):

    return render(request,'about.html')

def contact(request):

    return render(request,'contact.html')

def blog_list(request):
    blogs = Blog.objects.all()
    context = {'blogs' : blogs}
    return render(request,'blog_list.html', context)

def subscribe(request):
    if request.method == 'POST':
        email = request.POST['email']
        if Subscriber.objects.filter(email=email).exists():
            messages.error(request,'You are alread subscribed.')
        else:
            subscriber = Subscriber(email=email)
            subscriber.save()
            messages.success(request,'Thank you for subscribing!')
            return redirect('subscribe')
        return render(request,'subscribe.html')
        