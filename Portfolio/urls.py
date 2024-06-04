from django.urls import path
from . import views

app_name = "portfolio"
urlpatterns = [
    path('', views.index, name='index'),
    path('gallery', views.gallery, name='gallery'),
    path('blog', views.blog, name='blog'),
    path('contact', views.contact, name='contact'),
    path('blogpage/<int:id>', views.blog_page, name='blogpage')
    
]