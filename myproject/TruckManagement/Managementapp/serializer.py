from rest_framework import serializers
from Managementapp.models import User, Driver, Admin, Owner, Truck, AssignTruck

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "is_admin", "is_driver", "is_superuser")


# Registering Admin Serializer
class AdminSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = ("id", "username", "email", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def save(self, **kwargs):
        user = User(
            username=self.validated_data["username"], email=self.validated_data["email"]
        )
        password = self.validated_data["password"]
        user.set_password(password)
        user.is_admin = True
        user.is_superuser = True
        user.save()
        Admin.objects.create(user=user)
        return user


# Registering Owner Serializer
class OwnerSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = ("id", "username", "email", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def save(self, **kwargs):
        user = User(
            username=self.validated_data["username"], email=self.validated_data["email"]
        )
        password = self.validated_data["password"]

        user.set_password(password)
        user.is_owner = True
        user.is_superuser = True
        user.save()
        Owner.objects.create(user=user)
        return user


# Registering Driver Serializer
class DriverSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = ("id", "username", "first_name", "last_name", "email", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def save(self, **kwargs):
        user = User(
            username=self.validated_data["username"], email=self.validated_data["email"]
        )
        password = self.validated_data["password"]

        user.set_password(password)
        user.is_driver = True

        # For saving new driver into driver table
        user2 = Driver(
            username=self.validated_data["username"],
            email=self.validated_data["email"],
            firstname=self.validated_data["first_name"],
            lastname=self.validated_data["last_name"],
        )

        user2.is_driver = True
        user2.save()
        user.save()
        return user


# for driver records
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ("id", "firstname", "lastname", "email", "username")


# for truck records
class TruckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Truck
        fields = "__all__"


# for assign trucks to drivers
class AssignTruckSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignTruck
        fields = "__all__"
