from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ReservationForm
from .models import Reservation

@login_required
def reserve(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date']
            existing_reservation = Reservation.objects.filter(user=request.user, date=date).first()
            if existing_reservation:
                # The user has already made a reservation for this date
                # You can add a custom error message to the form like this:
                form.add_error('date', '이미 예약하신 날짜입니다')
            else:
                # The user has not made a reservation for this date yet
                reservation = form.save(commit=False)
                reservation.user = request.user
                reservation.save()
    else:
        form = ReservationForm()
    return render(request, 'calender.html', {'form': form})
