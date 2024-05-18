from django.db import models
from .managers import ThreadManager
from accounts.models import CustomUser


class TrackingModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class Thread(TrackingModel):
    THREAD_TYPE = (
        ("personal", "Personal"),
        ("groud", "Group")
    )

    name = models.CharField(max_length=50, null=True, blank=True)
    thread_type = models.CharField(max_length=15, choices=THREAD_TYPE, default="group")
    users = models.ManyToManyField(CustomUser)

    objects = ThreadManager()

    def __str__(self) -> str:
        return self.name

class Message(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.TextField(blank=False, null=False)
