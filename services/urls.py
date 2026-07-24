from django.urls import path
from . import views

urlpatterns = [
    path("vehicles/", views.vehicle_list, name="vehicle_list"),
    path("vehicles/add/", views.add_vehicle, name="add_vehicle"),

    path("book/", views.book_service, name="book_service"),
    path("bookings/", views.booking_list, name="booking_list"),
    path("vehicles/<int:pk>/edit/", views.edit_vehicle, name="edit_vehicle"),
    path("vehicles/<int:pk>/delete/", views.delete_vehicle, name="delete_vehicle"),
    path(
    "bookings/<int:pk>/",
    views.booking_detail,
    name="booking_detail",
    ),
    path(
    "booking/<int:pk>/cancel/",
    views.cancel_booking,
    name="cancel_booking",
    ),
    path(
    "history/",
    views.service_history,
    name="service_history",
    ),
]