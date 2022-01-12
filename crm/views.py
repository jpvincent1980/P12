import logging

from rest_framework.viewsets import ModelViewSet

from .models import Client, Contract, Event
from .serializers import ClientSerializer, ContractSerializer, EventSerializer
from .permissions import IsSalesContact, IsSupportContact


logger = logging.getLogger(__name__)


class ClientViewSet(ModelViewSet):
    """
    A custom ViewSet to list, retrieve, create, update and delete Client
    models.
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsSalesContact]


class ContractViewSet(ModelViewSet):
    """
    A custom ViewSet to list, retrieve, create, update and delete Contract
    models.
    """
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [IsSalesContact]


class EventViewSet(ModelViewSet):
    """
    A custom ViewSet to list, retrieve, create, update and delete Event
    models.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsSalesContact|IsSupportContact]


