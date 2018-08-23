from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from blog.models import Post

class PostListView(ListView):
    
    model=Post
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now']=timezone.now()
        return context

class PostView(DetailView):
    
    model = Post
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now']=timezone.now()
        return context

