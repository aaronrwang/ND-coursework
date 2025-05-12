from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Blog

def index(request):
	context = {'course': "CSE-30332",'semester':'Spring 25'}
	return render(request, 'blog/index.html', context)

class IndexView(ListView):
	template_name = 'blog/list_posts.html'
	context_object_name = 'latest_posts'

	def get_queryset(self):
		return Blog.objects.order_by('-pub_date')

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/post.html'
