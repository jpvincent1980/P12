from django.shortcuts import redirect

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly

from .models import CustomUser
from .serializers import CustomUserSerializer


class CustomUserViewSet(ModelViewSet):
    """
    A custom ViewSet to list, retrieve, create, update and delete CustomUser
    models.
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdminUser]


def redirection_view(request):
    """
    A FBV (Function-Based View) redirecting index page to the login page.
    """
    return redirect("/admin/")
