from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import UserCreationFormCustom
from django.views.generic import CreateView

# Create your views here.
def home_page(request):
    user = request.user
    return render(request, 'main/home_page.html',context={'user':user})



class SignupPage(CreateView):
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    form_class = UserCreationFormCustom