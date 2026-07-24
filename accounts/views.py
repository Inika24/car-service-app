from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from .forms import RegisterForm
from services.models import Vehicle, Booking


def register(request):

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/login/")

    else:
        form = RegisterForm()

    return render(
        request,
        "accounts/register.html",
        {"form": form},
    )


def logout_user(request):
    if request.method == "POST":
        logout(request)

    return redirect("/")


@login_required
def dashboard(request):

    total_vehicles = Vehicle.objects.filter(
        owner=request.user
    ).count()

    total_bookings = Booking.objects.filter(
        customer=request.user
    ).count()

    pending_bookings = Booking.objects.filter(
        customer=request.user,
        status="pending",
    ).count()

    completed_bookings = Booking.objects.filter(
        customer=request.user,
        status="completed",
    ).count()

    context = {
        "total_vehicles": total_vehicles,
        "total_bookings": total_bookings,
        "pending_bookings": pending_bookings,
        "completed_bookings": completed_bookings,
    }

    return render(
        request,
        "home/dashboard.html",
        context,
    )
from .forms import ProfileForm


@login_required
def profile(request):

    if request.method == "POST":
        form = ProfileForm(
            request.POST,
            instance=request.user
        )

        if form.is_valid():
            form.save()
            return redirect("profile")

    else:
        form = ProfileForm(instance=request.user)

    return render(
        request,
        "accounts/profile.html",
        {"form": form},
    )