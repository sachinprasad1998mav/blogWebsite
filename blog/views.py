from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse
from blog.models import Category, Post,Comment
from .forms import CommentForm
from django.http import HttpResponseRedirect
# Create your views here.
def home(request):
    posts = Post.objects.all()[:11]
    cats = Category.objects.all()
    data = {
        'posts' : posts,
        'cats' : cats
    }
    return render(request, 'home.html', data)

def about(request):
    return render(request,'about.html')

def post(request,url):
    post = Post.objects.get(url=url)
    if (request.method == "POST"):
        comment_form = CommentForm(request.POST)
        if (comment_form.is_valid()):

            # Save form data to DB
            comment=Comment()
            comment.comment=comment_form.cleaned_data['comment']
            comment.post=post
            # Save encrypted password to DB
            comment.save()
            return HttpResponseRedirect(request.path_info)
    else:
        comment_form=CommentForm()
        cats = Category.objects.all()
        comments=Comment.objects.filter(post=post)
        return render(request,'posts.html',{'post':post,
         'cats':cats,
          'comments':comments,
          'comment_form':comment_form          
          })


def category(request, url):
    cat = Category.objects.get(url=url)
    posts = Post.objects.filter(cat=cat)
    return render(request,"category.html", {'cat':cat,'posts':posts})

