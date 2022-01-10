from django.contrib.auth.hashers import make_password

from rest_framework.serializers import ModelSerializer

from .models import CustomUser


class CustomUserSerializer(ModelSerializer):
    """
    A custom ModelSerializer that serializes CustomUser instances.
    """
    def validate_password(selfself, value: str) -> str:
        return make_password(value)

    class Meta:
        model = CustomUser
        fields = ["id", "first_name", "last_name", "email", "phone", "mobile",
                  "department", "date_created", "date_updated"]