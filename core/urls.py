from django.urls import path

from .views import PostListView, PostDetailView, AboutTemplateView, ContactCreateView, NewsListView


urlpatterns = [
    path('', PostListView.as_view(), name='main'),
    path('about/', AboutTemplateView.as_view(), name='about'),
    path('contact/', ContactCreateView.as_view(), name='contact'),
    path('news/', NewsListView.as_view(), name='news'),
    path('news/<slug:post_slug>/', PostDetailView.as_view(), name='post'),
]

