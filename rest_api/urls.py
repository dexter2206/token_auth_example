from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import HelloView, NotesView


urlpatterns = [
    path("auth", obtain_auth_token),
    path("hello-world", HelloView().as_view()),
    path("notes", NotesView().as_view()),
    path('jwt/auth', TokenObtainPairView.as_view()),
    path('jwt/refresh', TokenRefreshView.as_view()),
]
