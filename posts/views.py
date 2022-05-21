from django.shortcuts import redirect, render

from posts.models import Post

# Create your views here.


def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})


def posts(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})


def create_post(request):
    if(request.POST):
        title = request.POST['title']
        body = request.POST['body']
        # post = Post.objects.add_post(title=title, body=body)
        post = Post.objects.create(title=title, body=body)
        post.save()
        return redirect('posts')
    else:
        return render(request, 'new_post.html')


def post(request, slug):
    post = Post.objects.get(id=slug)
    return render(request, 'post.html', {'post': post})
