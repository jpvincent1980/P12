from django.db import models

from epicevents import settings


CONTRACTS_STATUS_CHOICES = [
    ("NOT SIGNED", "Not signed"),
    ("SIGNED", "Signed"),
    ("CANCELLED", "Cancelled")
]

EVENTS_STATUS_CHOICES = [
    ("CREATED", "Created"),
    ("FINISHED", "Finished"),
    ("CANCELLED", "Cancelled")
]


class Client(models.Model):
    """
    A model that represents a customer
    """
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(max_length=128)
    phone = models.CharField(max_length=20, blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    company = models.CharField(max_length=128)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True, blank=True, null=True)
    sales_contact = models.ForeignKey(settings.AUTH_USER_MODEL,
                                      on_delete=models.SET_NULL,
                                      null=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        ordering = ["last_name",]
        verbose_name = "Client"


class Contract(models.Model):
    """
    A model that represents a contract
    """
    sales_contact = models.ForeignKey(settings.AUTH_USER_MODEL,
                                      on_delete=models.RESTRICT)
    client = models.ForeignKey(Client, on_delete=models.RESTRICT)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True, blank=True, null=True)
    contract_status = models.CharField(max_length=128,
                                       choices=CONTRACTS_STATUS_CHOICES,
                                       default="NOT SIGNED")
    amount = models.FloatField(blank=True, null=True)
    payment_due = models.DateField(blank=True, null=True)

    def __str__(self):
        return "Contrat # " + str(self.id)

    class Meta:
        ordering = ["-id", ]
        verbose_name = "Contrat"


class Event(models.Model):
    """
    A model that represents an event
    """
    client = models.ForeignKey(Client, on_delete=models.RESTRICT)
    contract = models.ForeignKey(Contract, on_delete=models.RESTRICT)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True, blank=True, null=True)
    support_contact = models.ForeignKey(settings.AUTH_USER_MODEL,
                                      on_delete=models.SET_NULL, null=True)
    event_status = models.CharField(max_length=128,
                                    choices=EVENTS_STATUS_CHOICES,
                                    default="CREATED")
    attendees = models.IntegerField(blank=True, null=True)
    event_date = models.DateField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return "Evénement # " + str(self.id)

    class Meta:
        ordering = ["-id", ]
        verbose_name = "Evénement"

