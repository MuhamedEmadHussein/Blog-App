from django.shortcuts import render
from django.views.generic import (ListView,DetailView)
from django.views.generic.edit import (CreateView,UpdateView,DeleteView)
from .models import Post
from django.urls import reverse_lazy
# Create your views here.

class BlogListView(ListView):
    model = Post
    template_name = "home.html"
    # Note that model_list comes from ListView 
    # and contains all the objects in our view of the model post.

class BlogDetailsView(DetailView):
    # context_object_name -> explicit identifying name of context
    model = Post
    template_name = "post_details.html"
    # Context -> Lowercase of our Model Name

    # DetailView expects either a primary key 
    # or a slug passed to it as the identifier
class BlogCreateView(CreateView):
    model = Post
    template_name = "post_new.html"
    fields = ['title','author','body']
    
class BlogUpdateView(UpdateView):
    model = Post
    template_name = "post_edit.html"
    fields = ["title","body"] 
    # Explicitly specifying fields we want to use
    #  instead of "__all__"   
class BlogDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")
