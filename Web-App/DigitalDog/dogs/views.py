from django.shortcuts import render
from django.views.generic import CreateView
from .models import Dog
from .forms import RegisterDogForm
# Create your views here.

class RegisterDogView(CreateView):
    template_name = "dogs/register_dog.html"
    
    model = Dog
    form_class = RegisterDogForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

