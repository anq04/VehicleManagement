from django.contrib import admin
from .models import User, Driver, Truck, AssignTruck

admin.site.register(User)
admin.site.register(Driver)
admin.site.register(Truck)
admin.site.register(AssignTruck)

