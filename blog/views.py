from django.shortcuts import render,redirect,reverse,get_object_or_404
from .models import Blog
#from django.urls import reverse_lazy
#from django.views.generic.edit import DeleteView

# Create your views here.

def home_blog_view(request):
    blogs = Blog.objects.order_by('-counter')
    return render(request,'main/home.html',{'blogs':blogs})


def complete_blog_view(request,pk):
    blog = Blog.objects.get(pk=pk)
    blog.counter += 1
    blog.save()
    return render(request,'main/post.html',{'blog':blog})


def customer_delete_view(request, pk):
    if request.method == 'POST':
        blog = get_object_or_404(Blog,pk=pk)
        blog.delete()
    return redirect(reverse('home-url'))

# class PostDeleteview(DeleteView):
#     model = Blog
#     template_name = 'main/post_delete.html'
#     success_url = reverse_lazy('home-url')

def blog_css_view(request):
    blogss = Blog.objects.all()
    return render(request,'main/blog_css_shablon.html',{'natijalar':blogss})


