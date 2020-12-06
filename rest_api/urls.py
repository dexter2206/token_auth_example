from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import HelloView


urlpatterns = [
    path("auth", obtain_auth_token),
    path("hello-world", HelloView().as_view())
]
