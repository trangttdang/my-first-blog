from django.shortcuts import render

from rest_framework import viewsets

from blog.serializers import PostSerializer
from blog.models import Post

from django.utils import timezone

class PostViewSet(viewsets.ModelViewSet):
  queryset = Post.objects.all()
  serializer_class = PostSerializer

# def post_list(request):
#     posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
#     return render(request, 'blog/post_list.html', {'posts': posts})

def post_list(request):
  return render(request, 'blog/post_list.html', {'posts': PostViewSet.queryset}) 