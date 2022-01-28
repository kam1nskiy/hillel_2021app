from django.views.generic import ListView
from django.views.generic import TemplateView



from core.models import Post


# def posts(request):
#     posts = Post.objects.all()
#     results = ",".join([post.title for post in posts])
#     #posts = "post 1: USER"
#     return HttpResponse(results)



# class PostsView(TemplateView):
#     template_name = 'core/posts.html'


#     def get_context_data(self, **kwargs):
#         ctx = super().get_context_data(**kwargs)
#         ctx['posts'] = Post.objects.all() 
#         return ctx


class PostsView(TemplateView):
    template_name = 'core/posts.html'

    def get_context_data(self, **kwargs):
        #Post = get_user_model()
        ctx = super().get_context_data(**kwargs)
        ctx['posts'] = Post.objects.all()
        return ctx


class IndexView(TemplateView):
    template_name = 'core/index.html'




