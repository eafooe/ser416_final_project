from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from users.forms import CustomUserCreationForm
from data.models import Offering, CreditCard, Booking
from django.contrib import messages
from django.http.response import HttpResponseRedirect
import json
from django.forms.models import model_to_dict

# Static Pages
def home(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'registration/login.html')

def employee_login(request):
    return render(request, 'registration/employee-login.html')

def logout(request):
    logout(request)

def about(request):
    return render(request, 'about.html')

def calendar(request):
    return render(request, 'calendar.html')

def contact(request):
    return render(request, 'contact.html')

def donate(request):
    return render(request, 'donate.html')


def donation(request):
    return render(request, 'donation-successful.html')

def profile(request):
    return render(request, 'profile.html')
    
# Pages w/ Templating Input
def services(request):
    context = {}
    context["list"] = Offering.objects.filter(offering_type="Service")
    context["title"] = "Services"
    context["card"] = CreditCard.objects.filter(
        owned_by=request.user.pk).first()
    return render(request, 'services.html', context)

def courses(request):
    context = {}
    context["list"] = Offering.objects.filter(offering_type="Course")
    context["title"] = "Courses"
    context["card"] = CreditCard.objects.filter(
        owned_by=request.user.pk).first()
    return render(request, 'courses.html', context)

def rentals(request):
    context = {}
    context["list"] = Offering.objects.filter(offering_type="Rental")
    context["card"] = CreditCard.objects.filter(
        owned_by=request.user.pk).first()
    context["title"] = "Rentals"
    return render(request, 'rentals.html', context)

def reservations(request):
    queryset = Offering.objects.select_related().filter(
        booking__booked_by=request.user)
    context = {}
    context["list"] = queryset
    return render(request, 'reservations.html', context)

# Logic Handlers
# https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password')
            role = form.cleaned_data.get('role')
            first_name = form.cleaned_data.get('first_name')
            django_login(request, user)
            return HttpResponseRedirect("/")
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@csrf_exempt
def add_offering(request):
    if request.method == 'POST':
        offer = request.POST.get("offering-type")
        name = request.POST.get("offering-name")
        description = request.POST.get("description")
        fee = request.POST.get("fee")
        start = request.POST.get("start")
        end = request.POST.get("end")
        maxOcc = request.POST.get("maxOccupancy")
        start_days = start[0:10]
        start_time = start[11:] + ":00"
        start = start_days + ' ' + start_time
        end = end[0:10] + ' ' + end[11:] + ":00"
        other = Offering(offering_type=offer, name=name, description=description, fee=fee,
                         start_time=start, end_time=end, current_occupancy=maxOcc, maximum_occupancy=maxOcc)
        Offering.add_offering(other)
    return redirect(request.META['HTTP_REFERER'])

@csrf_exempt
def addCard(request):
    if request.method == 'POST':
        month = request.POST['expiry_month']
        year = request.POST['expiry_year']
        last = request.POST['cardNumber'][-4:]
        card = CreditCard(owned_by=request.user, last_four=last,
                          expiry_month=month, expiry_year=year)
        CreditCard.add_card(card)
        return redirect(request.META['HTTP_REFERER'])

@csrf_exempt
def deleteOffering(request):
    if request.method == 'POST':
        offeringToDelete = request.POST['idToDelete']
        objToDel = Offering.objects.get(id=offeringToDelete)
        Offering.delete(objToDel)
    return redirect(request.META['HTTP_REFERER'])

@csrf_exempt
def book(request):
    if request.method == "POST":
        print("Booked ID: ")
        print(request.POST.get("offering-id"))
        obj = Offering.objects.get(id=request.POST.get("offering-id"))
        book = Offering.book(obj, request.user)
        if book:
            return HttpResponse(200)
        else:
            return HttpResponse(400)

@csrf_exempt
def unbook(request):
    if request.method == "POST":
        obj = Offering.objects.get(id=request.POST.get("id"))
        Offering.unbook(obj, request.user)
    return redirect(request.META['HTTP_REFERER'])

# Used to populate initial data
def dummy(request):
    other = Offering(offering_type="Course", name="Spanish for Beginners: Counting", description="Learn basic numbers in Spanish. Ideal for beginners.", fee=0.00, start_time="2021-05-26 12:30:00",
                     end_time="2021-05-26 13:00:00", current_occupancy=10, maximum_occupancy=10)
    Offering.add_offering(other)
    other = Offering(offering_type="Course", name="Spanish for Beginners: Colors & Shapes", description="Learn basic colors and shapes in Spanish. Ideal for beginners.", fee=0.00, start_time="2021-05-24 14:30:00",
                     end_time="2021-05-24 15:00:00", current_occupancy=9, maximum_occupancy=10)
    Offering.add_offering(other)
    other = Offering(offering_type="Course", name="Advanced Knitting: Gloves", description="Learn to make gloves in this class for advanced knitters. Materials provided.", fee=5.00, start_time="2021-05-21 12:30:00",
                     end_time="2021-05-21 13:45:00", current_occupancy=3, maximum_occupancy=5)
    Offering.add_offering(other)
    other = Offering(offering_type="Course", name="Spanish for Beginners: Counting", description="Learn basic numbers in Spanish. Ideal for beginners.", fee=0.00, start_time="2021-06-02 12:30:00",
                     end_time="2021-06-02 13:00:00", current_occupancy=10, maximum_occupancy=10)
    Offering.add_offering(other)
    other = Offering(offering_type="Course", name="Spanish for Beginners: Colors & Shapes", description="Learn basic colors and shapes in Spanish. Ideal for beginners.", fee=0.00, start_time="2021-05-31 14:30:00",
                     end_time="2021-05-31 15:00:00", current_occupancy=0, maximum_occupancy=10)
    Offering.add_offering(other)
    other = Offering(offering_type="Course", name="Advanced Knitting: Gloves", description="Learn to make gloves in this class for advanced knitters. Materials provided.", fee=5.00, start_time="2021-05-28 12:30:00",
                     end_time="2021-05-28 13:45:00", current_occupancy=4, maximum_occupancy=5)
    Offering.add_offering(other)
    other = Offering(offering_type="Rental", name="Fog Machine Rental", description="Fog machine rental",
                     fee=7.99, start_time="2021-05-26 10:00:00", end_time="2021-05-26 11:00:00")
    Offering.add_offering(other)
    other = Offering(offering_type="Rental", name="Fog Machine Rental", description="Fog machine rental",
                     fee=7.99, start_time="2021-05-26 11:00:00", end_time="2021-05-26 12:00:00", current_occupancy=0)
    Offering.add_offering(other)
    other = Offering(offering_type="Rental", name="Mini Excavator Rental", description="A driver's license is now required for this rental.",
                     fee=4.99, start_time="2021-05-24 9:00:00", end_time="2021-05-24 18:00:00")
    Offering.add_offering(other)
    other = Offering(offering_type="Rental", name="Bald Cap rental", description="Top hat rental",
                     fee=0.00, start_time="2021-04-23 2:00:00", end_time="2021-04-23 2:15:00",  current_occupancy=0)
    Offering.add_offering(other)
    other = Offering(offering_type="Rental", name="3D Printer Rental", description="3D printer rental",
                     fee=0.00, start_time="2021-05-26 10:00:00", end_time="2021-05-26 11:00:00", maximum_occupancy=3)
    Offering.add_offering(other)
    other = Offering(offering_type="Rental", name="3D Printer Rental", description="3D printer rental", fee=0.00,
                     start_time="2021-05-26 11:00:00", end_time="2021-05-26 12:00:00", current_occupancy=0, maximum_occupancy=3)
    Offering.add_offering(other)
    other = Offering(offering_type="Rental", name="Horse Rental", description="Horse rental",
                     fee=10.00, start_time="2021-05-26 11:00:00", end_time="2021-05-26 12:00:00")
    Offering.add_offering(other)
    other = Offering(offering_type="Rental", name="Roller Blade Rental", description="Roller blade rental (all sizes)",
                     fee=0.00, start_time="2021-05-26 11:00:00", end_time="2021-05-26 12:00:00", maximum_occupancy=20)
    Offering.add_offering(other)
    other = Offering(offering_type="Service", name="Catering Service", description="Must be booked two weeks in advance. Three meal choices available for 20 people.", fee=450.00,
                     start_time="2021-05-21 11:00:00", end_time="2021-05-21 13:00:00", location="Dining Hall")
    Offering.add_offering(other)
    other = Offering(offering_type="Service", name="Shuttle Service: Library", description="Shuttle service to the local library.", fee=0.00, start_time="2021-05-18 11:00:00",
                     end_time="2021-05-18 13:00:00", location="Main Building", current_occupancy=14, maximum_occupancy=24)
    Offering.add_offering(other)
    other = Offering(offering_type="Service", name="Catering Service", description="Must be booked two weeks in advance. Three meal choices available for 20 people.", fee=450.00,
                     start_time="2021-05-28 11:00:00", end_time="2021-05-28 13:00:00",  current_occupancy=0, location="Dining Hall")
    Offering.add_offering(other)
    other = Offering(offering_type="Service", name="Elderly Home Care", description="Home care for elderly individuals.", fee=110.00,
                     start_time="2021-05-14 11:00:00", end_time="2021-05-14 15:00:00", location="On-Site")
    Offering.add_offering(other)
    other = Offering(offering_type="Service", name="Elderly Home Care", description="Home care for elderly individuals.", fee=110.00,
                     start_time="2021-05-21 11:00:00", end_time="2021-05-21 15:00:00", location="On-Site")
    Offering.add_offering(other)
    other = Offering(offering_type="Service", name="Elderly Home Care", description="Home care for elderly individuals.", fee=110.00,
                     start_time="2021-05-28 11:00:00", end_time="2021-05-28 15:00:00", current_occupancy=0, location="On-Site")
    Offering.add_offering(other)
