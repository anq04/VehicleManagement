from django.utils.timezone import now
from django.db.models.signals import post_save
from django.db import models
from django.conf import settings
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Overriding User class to define new attributes inorder to distinguish among users"""

    is_admin = models.BooleanField(default=False)
    is_driver = models.BooleanField(default=False)
    is_owner = models.BooleanField(default=False)
    REQUIRED_FIELDS = ["email", "first_name", "last_name"]

    def __str__(self) -> str:
        return self.username


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Owner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="owner")
    name = models.CharField(max_length=20, null=True)
    stocks_owned = models.CharField(max_length=20, null=True)

    def __str__(self) -> str:
        return self.user.username


class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="admin")

    def __str__(self) -> str:
        return self.user.username


class Driver(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="driver", null=True
    )
    firstname = models.CharField(max_length=20, null=True)
    lastname = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=20, null=True)
    username = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.user.username


class Truck(models.Model):
    no_plate = models.CharField(max_length=50, null=True)
    model_name = models.CharField(max_length=50, null=True)
    miles_per_gallon = models.CharField(max_length=50, null=True)
    drive_type = models.CharField(max_length=50, null=True)
    engine_type = models.CharField(max_length=50, null=True)
    color = models.CharField(max_length=20, null=True)
    horsepower = models.CharField(max_length=50, null=True)
    fuel_capacity = models.CharField(max_length=50, null=True)

    def get_object(self) -> str:
        return "%s %s" % (self.model_name, self.no_plate)


class AssignTruck(models.Model):
    driver = models.OneToOneField(Driver, on_delete=models.CASCADE, unique=True)
    vehicle = models.OneToOneField(Truck, on_delete=models.CASCADE, unique=True)
    issue_date = models.DateTimeField(default=now)
    return_date = models.DateTimeField(default=now)

    def __str__(self) -> str:
        return str(self.driver) + "- " + str(self.vehicle)
