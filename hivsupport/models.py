from django.contrib.auth.models import User
from django.db import models

CAREGIVERS = (
    ('DOCTOR', 'DOCTOR'),
    ('NURSE', 'NURSE'),
    ('THERAPIST', 'THERAPIST')
)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=255, blank=True)
    location = models.CharField(max_length=255, blank=True)
    birth_date = models.IntegerField(null=True, blank=True)
    phone_number = models.CharField(max_length=13, blank=True)
    user_type = models.CharField(choices=CAREGIVERS)
    website_url = models.URLField(max_length=200, blank=True)

def __str__(self):
    return self.user.username


class Message(models.Model):
    sender = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='sent_message')
    receiver = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='received_message')
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

def __str__(self):
    return f'{self.sender.user.username} to {self.receiver.user.username}: {self.content}'


class UserGroup(models.Model):
    name = models.TextField(max_length=255)
    members = models.ManyToManyField(Profile, blank=True)

def __str__(self):
    return self.user

