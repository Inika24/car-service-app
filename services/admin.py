from django.contrib import admin
from .models import ServiceCategory, Service, Vehicle, Booking


@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "price",
        "estimated_duration",
    )
    search_fields = ("name",)
    list_filter = ("category",)


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = (
        "owner",
        "brand",
        "model",
        "registration_number",
    )
    search_fields = (
        "brand",
        "model",
        "registration_number",
    )
    list_filter = ("brand",)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        "customer",
        "vehicle",
        "service",
        "booking_date",
        "booking_time",
        "status",
    )
    list_filter = (
        "status",
        "booking_date",
    )
    search_fields = (
        "customer__username",
        "vehicle__registration_number",
    )
    list_editable = ("status",)
    ordering = ("-booking_date",)