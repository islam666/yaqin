from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import csv
import os
from django.conf import settings
# Create your views here.
def index(request):
    return render(request, "portfolio/index.html")

def blog(request):
    blogs = Post.objects.all()
    
    return render(request, "portfolio/blog.html", {
        "blogs" : blogs
    })

def contact(request):
    return render(request, "portfolio/contact.html")

def gallery(request):
    imgs_path = []
    media_dir = settings.MEDIA_ROOT

    if not os.path.exists(media_dir):
        print("Media directory does not exist:", media_dir)  
        return render(request, "portfolio/gallery.html", {
            "imgs_path": imgs_path
        })

    for root, dirs, files in os.walk(media_dir):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff')):
                file_path = os.path.join(root, file)
                imgs_path.append(file_path)

    return render(request, "portfolio/gallery.html", {
        "imgs_path" : imgs_path, "MEDIA_URL":settings.MEDIA_URL,
        "basename": os.path.basename
    })

def blog_page(request, id):
    blog = get_object_or_404(Post, id=id)
    return render(request, "portfolio/blogpage.html", {
        "blog" : blog
    })
