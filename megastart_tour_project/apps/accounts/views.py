from django.shortcuts import render
from django.views.generic import CreateView
from .models import User
from .forms import SignUpForm

# Create your views here.

class SignUpView(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'pages/signup.html'
    success_url = '/'

    def form_valid(self, form):
        form.save()  # Сохраняем пользователя
        return super().form_valid(form)