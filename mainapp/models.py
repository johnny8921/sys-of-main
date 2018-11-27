from django.db import models
from django.utils import timezone


class Work(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    deviceType = models.CharField(max_length=25, default="device")
    number = models.CharField(max_length=5)
    serialNumber = models.DecimalField(max_digits=20, decimal_places=0)
    workBody = models.TextField()
    work_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return (self.deviceType + " " + self.number)