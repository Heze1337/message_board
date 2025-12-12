from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post

class HomePageView(ListView):
    model = Post
    template_name = "home.html"

class AboutPageView(ListView):
    model = Post
    template_name = "about.html"

class PostDetailView(DetailView):
    model=Post
    template_name="post_detail.html"

class PostCreateView(CreateView):
    model=Post
    template_name="post_new.html"
    fields = ["text", "data", "temperature", "pressure", "wind_speed", "precipitation_probability"]
    success_url = reverse_lazy("home")

class PostUpdateView(UpdateView):
    model = Post
    fields = ["text", "data", "temperature", "pressure", "wind_speed", "precipitation_probability"]
    template_name = "post_edit.html"
    success_url = reverse_lazy("home")

class PostDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")