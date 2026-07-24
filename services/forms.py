from django import forms
from datetime import date
from .models import Vehicle, Booking


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = [
            "brand",
            "model",
            "registration_number",
            "manufacturing_year",
        ]


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            "vehicle",
            "service",
            "booking_date",
            "booking_time",
        ]

    def clean_booking_date(self):
        booking_date = self.cleaned_data["booking_date"]

        if booking_date < date.today():
            raise forms.ValidationError(
                "Booking date cannot be in the past."
            )

        return booking_date

    def clean(self):
        cleaned_data = super().clean()

        vehicle = cleaned_data.get("vehicle")
        booking_date = cleaned_data.get("booking_date")
        booking_time = cleaned_data.get("booking_time")

        if vehicle and booking_date and booking_time:

            exists = Booking.objects.filter(
                vehicle=vehicle,
                booking_date=booking_date,
                booking_time=booking_time,
            ).exists()

            if exists:
                raise forms.ValidationError(
                    "This vehicle already has a booking at the selected date and time."
                )

        return cleaned_data