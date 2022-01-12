from django.shortcuts import redirect
import logging

from rest_framework.viewsets import ModelViewSet

from .models import CustomUser
from .serializers import CustomUserSerializer
from .permissions import IsManager


logger = logging.getLogger(__name__)


class CustomUserViewSet(ModelViewSet):
    """
    A custom ViewSet to list, retrieve, create, update and delete CustomUser
    models.
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsManager]


def redirection_view(request):
    """
    A FBV (Function-Based View) redirecting index page to the login page.
    """
    return redirect("/admin/")
