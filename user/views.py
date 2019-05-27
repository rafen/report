from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.base import RedirectView, TemplateView
from django.views.generic.edit import UpdateView
from .forms import UserForm
from .models import User


class UserRootView(RedirectView):
    pattern_name = 'user_home'


class UserHomeView(LoginRequiredMixin, TemplateView):
    template_name = 'user/index.html'


class UserProfileView(LoginRequiredMixin, UpdateView):
    template_name = 'user/profile.html'
    form_class = UserForm
    model_class = User
    success_url = reverse_lazy('user_profile')

    def get_object(self):
        return self.request.user
