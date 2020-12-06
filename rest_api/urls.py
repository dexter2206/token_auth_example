from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import HelloView, NotesView


urlpatterns = [
    path("auth", obtain_auth_token),
    path("hello-world", HelloView().as_view()),
    path("notes", NotesView().as_view())
]
