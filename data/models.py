from django.db import models
from users.models import CustomUser

OFFERING_CHOICES = (
    ('Course', 'Course'),
    ('Rental', 'Rental'),
    ('Service', 'Service')
)

CARD_TYPES = (
    ('Visa', 'Visa'),
    ('MasterCard', 'MasterCard'),
    ('American Express', 'American Express')
)

class Offering(models.Model):
    # Fields
    offering_type = models.CharField(max_length=7, choices=OFFERING_CHOICES, default='Course')
    name = models.TextField(max_length=100, help_text="Course Name")
    description = models.TextField(max_length=400, help_text="Course Description")
    fee = models.DecimalField(decimal_places=2, max_digits=5)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    current_occupancy = models.IntegerField(default=0)
    maximum_occupancy = models.IntegerField(default=10)
    location = models.TextField(max_length=100, default="Main Building")

    # Metadata
    class Meta:
        ordering = ['start_time', 'name']

    # Methods
    def __str__(self):
        return self.name

    def get_end_time(self):
        return self.end_time.time()

    # Add offering
    def add_offering(self):
        if Offering.objects.filter(name = self.name, start_time = self.start_time, end_time = self.end_time).exists():
            print("Failed to add offering. Reason: duplicate.")
        else:
            self.save()
            print("Successfully added offering")

    # Edit name
    def edit_name(self, name):
        self.name = name
        self.save()
    
    # Edit description
    def edit_description(self, description):
        self.description = description
        self.save()

    # Edit location
    def edit_location(self, location):
        self.location = location
        self.save()

    # Delete offering
    def delete_offering(self):
        self.delete()

    # Book offering
    def book(self, user):
        if (self.current_occupancy == 0):
            print("No occupancy")
            return None
        elif (Booking.objects.filter(for_offering = self, booked_by = user).first()):
            print("Already booked")
            return None
        else :
            print("All good!")
            self.current_occupancy -= 1
            self.save()
            book = Booking(for_offering = self, booked_by = user)
            book.save()
            return book

    # Remove booked offering
    def unbook(self, user):
        if Booking.objects.filter(for_offering = self, booked_by = user):
            self.current_occupancy += 1
            self.save()
            Booking.delete_booking(Booking.objects.filter(for_offering = self, booked_by = user).first())
            print("Unbook successful")

class Booking(models.Model):
    for_offering = models.ForeignKey(Offering, on_delete=models.CASCADE)
    booked_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def delete_booking(self):
        self.delete()

class CreditCard(models.Model):
    owned_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    last_four = models.IntegerField(default=1324)
    card_type = models.CharField(max_length=40, choices=CARD_TYPES, default='Visa')
    expiry_month = models.IntegerField(default=11)
    expiry_year = models.IntegerField(default=21)

    # Add card
    def add_card(self):
        if CreditCard.objects.filter(owned_by = self.owned_by).exists():
            print("Failed to add card. Reason: duplicate.")
        else:
            self.save()
            print("Successfully added card")
    