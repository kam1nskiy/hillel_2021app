from django.views import generic
from django.contrib.auth.forms import UserChangeForm

from users.models import Profile
from .forms import UserSignUpForm


from .models import Profile, User
from core.models import Post



from django.urls import reverse_lazy


class UserSignUpView(generic.CreateView):
    form_class = UserSignUpForm
    template_name = 'registration/signup.html'
    success_url = ('/login')

class UserEditView(generic.UpdateView):
    form_class = UserChangeForm
    template_name = 'profiles/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user




