from django.shortcuts import render

from django.shortcuts import render
from rest_framework import viewsets

from blog.serializers import PostSerializer
from blog.models import Post

class PostViewSet(viewsets.ModelViewSet):
  queryset = Post.objects.all()
  serializer_class = PostSerializer

def post_list(request):
    return render(request, 'blog/post_list.html', {})
