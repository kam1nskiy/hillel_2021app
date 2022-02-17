from django.urls import path
from .views import UserSignUpView, UserEditView

urlpatterns = [
    path('sign_up/', UserSignUpView.as_view(), name='sign_up'),
    path('profile/', UserEditView.as_view(), name='profile'),
]