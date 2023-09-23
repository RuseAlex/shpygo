from django.db import models
from .utils import phone_regex, state_choices
from django.contrib.auth.models import AbstractUser


class Profile(AbstractUser):
    avatar = models.ImageField(default="default_avatar.jpg", upload_to='profile_pics')
    bio = models.TextField(max_length=500)


    def __str__(self):
        return self.username


class ContactInfo(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, null=True, blank=True, validators=[phone_regex])
    street_name = models.CharField(max_length=100)
    street_num = models.PositiveIntegerField(blank=True, null=False, default=1)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=25, choices=state_choices, default='B', null=False, blank=False)


    def __str__(self):
        return f"{self.street_num} {self.street_num} - "