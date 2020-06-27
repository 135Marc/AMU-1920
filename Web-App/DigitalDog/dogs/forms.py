from django import forms
from .models import Dog

class RegisterDogForm(forms.ModelForm):
    class Meta:
        model = Dog
        fields = ['name','breed','weight','height']

    def __init__(self, user,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.user = user

    def save(self,commit=True):
        dog = super().save(commit=False)
        dog.owner = self.user
        dog.save()
        return dog        