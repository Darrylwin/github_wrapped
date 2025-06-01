from django.urls import path
from .views import GitHubWrapped

urlpatterns = [
    path('api/wrapped', GitHubWrapped.as_view()),
]
