from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='userprofile', related_query_name="userprofile", on_delete=models.CASCADE)
    active_team_id = models.IntegerField(default=0)

    def __str__(self):
        return str(self.user)