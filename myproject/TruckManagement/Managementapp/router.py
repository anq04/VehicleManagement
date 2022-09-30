from .views import CompanyViewSet, TruckViewSet, AssignTruckViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(
    "company_details", CompanyViewSet
)  # to perform CRUD operations on all records of drivers
router.register(
    "truck_details", TruckViewSet
)  # to perfrom CRUD operations on truck records
router.register(
    "assign_truck", AssignTruckViewSet
)  # to assign a truck to a specific driver and perform CRUD operations related to it
