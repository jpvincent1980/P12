from rest_framework.serializers import ModelSerializer

from .models import Client, Contract, Event


class ClientSerializer(ModelSerializer):
    """
    A custom ModelSerializer that serializes Client instances.
    """

    class Meta:
        model = Client
        fields = ["id", "first_name", "last_name", "email", "phone", "mobile",
                  "company", "date_created", "date_updated", "sales_contact"]


class ContractSerializer(ModelSerializer):
    """
    A custom ModelSerializer that serializes Contract instances.
    """

    class Meta:
        model = Contract
        fields = ["id", "sales_contact", "client", "date_created",
                  "date_updated", "contract_status", "amount", "payment_due"]


class EventSerializer(ModelSerializer):
    """
    A custom ModelSerializer that serializes Event instances.
    """

    class Meta:
        model = Event
        fields = ["id", "client", "contract", "date_created", "date_updated",
                  "support_contact", "event_status", "attendees",
                  "event_date", "notes"]