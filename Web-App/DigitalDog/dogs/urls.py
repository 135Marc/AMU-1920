from django.urls import include,path
from .views import RegisterDogView

app_name="dogs"

urlpatterns = [
    path(route="create/", view=RegisterDogView.as_view(),name="register_dog"),
]