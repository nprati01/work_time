from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Constants
   DAY_CHOICES = (
        ("MON", "Monday"),
        ("TUE", "Tuesday"),
        ("WED", "Wednesday"),
        ("THU", "Thursday"),
        ("FRI", "Friday"),
        ("SAT", "Satuday"),
        ("SUN", "Sunday"),

   )

# Employee Model
class Employee(models.Model):
    ROLE_CHOICES = ()

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.Charfield(max_length=50)
    phone_number = PhoneNumberField(unique = True, null = False, blank = False)
    availability = models.
