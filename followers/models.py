from django.db import models
from profiles.models import UserNet


class Follower(models.Model):
    user = models.ForeignKey(UserNet, on_delete=models.CASCADE, related_name='owner')
    follower = models.ForeignKey(UserNet, on_delete=models.CASCADE, related_name='followers')

