from django.db import models
from django.conf import settings


class Vehicle(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    registration_number = models.CharField(max_length=20, unique=True)
    manufacturing_year = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.brand} {self.model} ({self.registration_number})"


class ServiceCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Service(models.Model):
    category = models.ForeignKey(
        ServiceCategory,
        on_delete=models.CASCADE,
        related_name="services"
    )

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    estimated_duration = models.PositiveIntegerField(
        help_text="Duration in minutes"
    )

    def __str__(self):
        return self.name


class Booking(models.Model):

    STATUS_CHOICES = (
        ("pending", "Pending"),
        ("confirmed", "Confirmed"),
        ("in_progress", "In Progress"),
        ("completed", "Completed"),
        ("cancelled", "Cancelled"),
    )

    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="bookings"
    )

    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.CASCADE
    )

    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE
    )

    booking_date = models.DateField()
    booking_time = models.TimeField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending",
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer.username} - {self.service.name}"