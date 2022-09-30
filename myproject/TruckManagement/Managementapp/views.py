from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from .serializer import (
    UserSerializer,
    AdminSerializer,
    DriverSerializer,
    OwnerSerializer,
    CompanySerializer,
    TruckSerializer,
    AssignTruckSerializer,
)
from Managementapp.models import Driver, Truck, AssignTruck
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from .permissions import IsSuperuser, IsAdmin, IsDriver
from rest_framework import viewsets
import json

# from .router import router


class OwnerSignupView(generics.GenericAPIView):
    """Takes credentials from owner and creates a new account for them"""

    serializer_class = OwnerSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {
                "user": UserSerializer(
                    user, context=self.get_serializer_context()
                ).data,
                "token": Token.objects.get(user=user).key,
                "message": "Account is created",
            }
        )


class AdminSignupView(generics.GenericAPIView):
    """Takes credentials from admin and creates a new account for them"""

    serializer_class = AdminSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {
                "user": UserSerializer(
                    user, context=self.get_serializer_context()
                ).data,
                "token": Token.objects.get(user=user).key,
                "message": "Account is created",
            }
        )


class DriverSignupView(generics.GenericAPIView):
    """Takes credentials from drivers and creates a new account for them"""

    serializer_class = DriverSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {
                "user": UserSerializer(
                    user, context=self.get_serializer_context()
                ).data,
                "token": Token.objects.get(user=user).key,
                "message": "Account is created",
            }
        )


class CustomAuthToken(ObtainAuthToken):
    """For login purpose"""

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)

        return Response(
            {
                "token": token.key,
                "user_id": user.pk,
                "is_admin": user.is_admin,
                "is_driver": user.is_driver,
                "is_superuser": user.is_superuser,
            }
        )


class Logout(APIView):
    """Token of the loggedin user is destroyed and user is logged out"""

    def post(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class CompanyViewSet(viewsets.ModelViewSet):
    """Accessable to admins and owners to show all emplyee records, when driver tries to access, error is generated, admin and owner can add/update/view/delete records"""

    permission_classes = [permissions.IsAuthenticated & IsSuperuser]
    queryset = Driver.objects.all()
    serializer_class = CompanySerializer


class TruckViewSet(viewsets.ModelViewSet):
    """Accessable to admins and owners to show all emplyee records, when driver tries to access, error is generated,admin and owner can add/update/view/delete records"""

    permission_classes = [permissions.IsAuthenticated & IsSuperuser]
    queryset = Truck.objects.all()
    serializer_class = TruckSerializer


class AssignTruckViewSet(viewsets.ModelViewSet):
    """Accessable to admins to show all emplyee records, when driver or owner tries to access, error is generated, admin can add/update/view/delete records"""

    permission_classes = [permissions.IsAuthenticated & IsAdmin]
    queryset = AssignTruck.objects.all()
    serializer_class = AssignTruckSerializer


@api_view(["GET"])
@permission_classes([IsAuthenticated & IsDriver])
def getDriver(request):
    """Accessable to drivers only to show his record and which truck is aasigned to him"""
    user = request.user.username
    driver = Driver.objects.filter(username=user).values_list("id", flat=True)
    assignedTruck = AssignTruck.objects.filter(driver_id__in=driver.all()).values()
    truck_details = Truck.objects.filter(
        id__in=assignedTruck.all().values_list("vehicle_id")
    ).values()
    # driver_id=driver.id
    return Response({"your_record": assignedTruck, "truck_details": truck_details})
