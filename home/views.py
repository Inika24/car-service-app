from django.shortcuts import render


def home(request):
    return render(request, "home/index.html")
from django.contrib.admin.views.decorators import staff_member_required
from services.models import Vehicle, Booking, Service


@staff_member_required
def admin_dashboard(request):

    context = {
        "total_users": Booking.objects.values("customer").distinct().count(),
        "total_vehicles": Vehicle.objects.count(),
        "total_services": Service.objects.count(),
        "total_bookings": Booking.objects.count(),
        "pending": Booking.objects.filter(status="pending").count(),
        "completed": Booking.objects.filter(status="completed").count(),
    }

    return render(
        request,
        "home/admin_dashboard.html",
        context,
    )