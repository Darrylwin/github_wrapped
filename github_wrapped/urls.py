from django.urls import path

from wrapped.views import GitHubWrapped

urlpatterns = [
    path('api/wrapped', GitHubWrapped.as_view()),
]
