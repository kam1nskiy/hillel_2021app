
from django.contrib.auth import get_user_model
from django.views.generic import TemplateView

class UserView(TemplateView):
    template_name = 'users/users.html'

    def get_cotext_data(self, **kwargs):
        User =get_user_model()
        ctx = super().get_cotext_data(**kwargs)
        ctx['users'] = User.objects.all
        return ctx
