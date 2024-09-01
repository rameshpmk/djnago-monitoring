from django.db import models
from django.utils import timezone

# Create your models here.

class IPAddress(models.Model):
    address = models.GenericIPAddressField(protocol='both', unpack_ipv4=True, unique=True)
    monitor = models.BooleanField(default=False)

    def __str__(self):
        return str(self.address)

class PingResult(models.Model):
    address = models.ForeignKey(IPAddress, on_delete=models.CASCADE, related_name='ping_results')
    timestamp = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=255)
    response_time = models.FloatField()  # Optional: Store the response time in seconds

    def __str__(self):
        return str(self.address)
