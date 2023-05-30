from django.http import HttpResponseRedirect
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView

from .models import Post
from .forms import ContactForm


class PostListView(ListView):
    template_name = 'blog/index.html'
    model = Post
    context_object_name = 'posts'
    http_method_names = ('get',)

    def get_queryset(self):
        return Post.objects.all()[:5]

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data()
        data['heading'] = 'Post List'
        data['subheading'] = 'First Blog'
        return data


class PostDetailView(DetailView):
    template_name = 'blog/post.html'
    slug_url_kwarg = 'post_slug'
    model = Post


class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'blog/contact.html'
    success_url = '/contact'

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.get_success_url())
