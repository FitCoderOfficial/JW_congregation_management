from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ReservationForm
from django.http import JsonResponse 
from .models import Reservation

# Create your views here.
def index(request):  
    all_events = Reservation.objects.all()
    context = {
        "events":all_events,
    }
    return render(request,'calender.html',context)

def all_events(request):                                                                                                 
    all_events = Reservation.objects.all()                                                                                    
    out = []                                                                                                             
    for event in all_events:                                                                                             
        out.append({                                                                                                     
            'user': event.username,                                                                                              
            'date': event.start.strftime("%m/%d/%Y"),                                                  
        })                                                                                                               
                                                                                                                      
    return JsonResponse(out, safe=False) 

def add_event(request):
    date = request.GET.get("date", None)
    username = request.GET.get("username", None)
    event = Reservation(user=str(username), date=date)
    event.save()
    data = {}
    return JsonResponse(data)

def update(request):
    date = request.GET.get("date", None)
    username = request.GET.get("username", None)
    event = Reservation.objects.get(username=username)
    event.username = username
    event.date = date
    event.save()
    data = {}
    return JsonResponse(data)
 
def remove(request):
    username = request.GET.get("username", None)
    event = Reservation.objects.get(username=username)
    event.delete()
    data = {}
    return JsonResponse(data)


# @login_required
# def reserve(request):
#     if request.method == 'POST':
#         form = ReservationForm(request.POST)
#         if form.is_valid():
#             date = form.cleaned_data['date']
#             existing_reservation = Reservation.objects.filter(user=request.user, date=date).first()
#             if existing_reservation:
#                 # The user has already made a reservation for this date
#                 # You can add a custom error message to the form like this:
#                 form.add_error('date', '이미 예약하신 날짜입니다')
#             else:
#                 # The user has not made a reservation for this date yet
#                 reservation = form.save(commit=False)
#                 reservation.user = request.user
#                 reservation.save()
#     else:
#         form = ReservationForm()
#     return render(request, 'calender.html', {'form': form})
