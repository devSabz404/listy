from django.db import models
from django.conf import settings

from phone_field import PhoneField


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    phone_number = PhoneField(blank=True, help_text='Contact phone number')


    def __str__(self):
        return f'Profile for user {self.user.username}'
