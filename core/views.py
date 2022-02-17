from django.http import Http404, HttpResponseRedirect
from django.views.generic import *

from core.models import Post
from .forms import CreateForm


class PostsView(TemplateView):
    template_name = 'core/posts.html'

    def get_context_data(self, **kwargs):
        posts = Post.objects.all()
        ctx = super().get_context_data(**kwargs)
        posts = Post.objects.all()
        ctx['results'] = [
            (
                p,
                p.like_set.filter(status=True).count(),
                p.like_set.filter(status=False).count()
            )
            for p in posts
        ]
        return ctx


class IndexView(TemplateView):
    template_name = 'core/index.html'


class PostDetailView(DetailView):
    model = Post
    template_name = "core/post_detail.html"
    context_object_name = "post"

    def get_slug_field(self, **kwargs):
        ctx = super().get_slug_field(**kwargs)
        return ctx   


class PostCreateView(CreateView):
    model = Post
    form_class = CreateForm
    template_name = 'core/post_create.html'
    success_url = '/posts'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)



class PostUpdateView(UpdateView):
    model = Post
    template_name = 'core/post_update.html'
    fields = ['title',
              'content',
              'image',
              ]
    template_name_suffix = '_update_form'
    success_url = '/posts'

    def get(self, request, *args, **kwargs):
        if self.get_object().user != request.user:
            return HttpResponseRedirect("/posts/")
        return super().get(request, *args, **kwargs)


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'core/post_delete.html'
    success_url = '/posts'

    def get(self, request, *args, **kwargs):
        if self.get_object().user != request.user:
            return HttpResponseRedirect("/posts")
        return super().get(request, *args, **kwargs)





