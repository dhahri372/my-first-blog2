from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.all()  # Récupère tous les articles de la base de données
    return render(request, 'blog/post_list.html', {'posts': posts})
