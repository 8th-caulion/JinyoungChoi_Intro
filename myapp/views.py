from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.utils import timezone

# Create your views here.
def main(request):
    return render(request, 'main.html')

def profile(request):
    return render(request, 'profile.html')

# 여기부터 블로그
def profile(request):
    blogs = Blog.objects
    return render(request, 'profile.html', {'blogs': blogs})

def detail(request, blog_id):
    details = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'detail.html', {'details': details})

def new(request):
    return render(request, 'new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title'] #new.html의 name="title"
    blog.name = request.GET['name']
    blog.location = request.GET['location']
    blog.body = request.GET['body'] #new.html의 name="body"
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('profile')

def edit(request, blog_id):
    blog = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'edit.html', {'blog' : blog})
    
def update(request, blog_id):
    blog = get_object_or_404(Blog, pk = blog_id)
    blog.title = request.GET['title']
    blog.name = request.GET['name']
    blog.location = request.GET['location']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('profile')
    
def delete(request, blog_id):
    blog = get_object_or_404(Blog, pk = blog_id)
    blog.delete()
    return redirect('profile')