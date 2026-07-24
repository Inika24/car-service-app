from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import VehicleForm, BookingForm
from .models import Booking,Vehicle
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
@login_required
def add_vehicle(request):

    if request.method == "POST":
        form = VehicleForm(request.POST)

        if form.is_valid():
            vehicle = form.save(commit=False)
            vehicle.owner = request.user
            vehicle.save()
            return redirect("vehicle_list")

    else:
        form = VehicleForm()

    return render(
        request,
        "services/add_vehicle.html",
        {"form": form}
    )
@login_required
def vehicle_list(request):

    vehicles = request.user.vehicle_set.all()

    return render(
        request,
        "services/vehicle_list.html",
        {"vehicles": vehicles},
    )

@login_required
def book_service(request):

    if request.method == "POST":
        form = BookingForm(request.POST)

        # Show only logged-in user's vehicles
        form.fields["vehicle"].queryset = request.user.vehicle_set.all()

        if form.is_valid():
            booking = form.save(commit=False)
            booking.customer = request.user
            booking.save()
            messages.success(
                request,
                "Service booked successfully!"
            )

            return redirect("booking_list")

    else:
        form = BookingForm()
        form.fields["vehicle"].queryset = request.user.vehicle_set.all()

    return render(
        request,
        "services/book_service.html",
        {"form": form},
    )
@login_required
def booking_list(request):

    bookings = Booking.objects.filter(customer=request.user)

    search = request.GET.get("search")
    status = request.GET.get("status")

    if search:
        bookings = bookings.filter(
            vehicle__registration_number__icontains=search
        )

    if status:
        bookings = bookings.filter(status=status)

    paginator = Paginator(bookings, 5)

    page_number = request.GET.get("page")

    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "services/booking_list.html",
        {
            "page_obj": page_obj,
        },
    )
@login_required
def edit_vehicle(request, pk):

    vehicle = get_object_or_404(
        Vehicle,
        pk=pk,
        owner=request.user
    )

    if request.method == "POST":
        form = VehicleForm(request.POST, instance=vehicle)

        if form.is_valid():
            form.save()
            return redirect("vehicle_list")

    else:
        form = VehicleForm(instance=vehicle)

    return render(
        request,
        "services/edit_vehicle.html",
        {"form": form},
    )
@login_required
def delete_vehicle(request, pk):

    vehicle = get_object_or_404(
        Vehicle,
        pk=pk,
        owner=request.user
    )

    if request.method == "POST":
        vehicle.delete()
        return redirect("vehicle_list")

    return render(
        request,
        "services/delete_vehicle.html",
        {"vehicle": vehicle},
    )
@login_required
def booking_detail(request, pk):

    booking = get_object_or_404(
        Booking,
        pk=pk,
        customer=request.user
    )

    return render(
        request,
        "services/booking_detail.html",
        {"booking": booking},
    )
@login_required
def cancel_booking(request, pk):

    booking = get_object_or_404(
        Booking,
        pk=pk,
        customer=request.user
    )

    if booking.status == "pending":
        booking.status = "cancelled"
        booking.save()
        messages.success(request, "Booking cancelled successfully.")

    return redirect("booking_list")
@login_required
def service_history(request):

    bookings = Booking.objects.filter(
        customer=request.user,
        status="completed"
    )

    return render(
        request,
        "services/service_history.html",
        {
            "bookings": bookings,
        },
    )