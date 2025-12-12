from django.urls import path
from .views import HomePageView, AboutPageView, PostCreateView, PostDetailView, PostUpdateView, PostDeleteView

urlpatterns = [
    path("post/new/", PostCreateView.as_view(), name="post_new"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("post/<int:pk>/edit/", PostUpdateView.as_view(), name="post_edit"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post_delete"),
]