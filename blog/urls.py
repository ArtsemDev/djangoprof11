from django.urls import path

from .views import PostListView, PostDetailView, ContactFormView


urlpatterns = [
    path('', PostListView.as_view(), name='blog_index'),
    path('contact/', ContactFormView.as_view(), name='blog_contact'),
    path('<slug:post_slug>/', PostDetailView.as_view(), name='blog_post_detail')
]
