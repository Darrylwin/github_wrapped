import os
from dotenv import load_dotenv
from rest_framework.views import APIView
from rest_framework.response import Response

load_dotenv()

class GitHubWrapped(APIView):
    def get(self, request):
        userName = request.GET.get('username', 'Darrylwin')
        return Response({'message': f"Hello {userName}!"})