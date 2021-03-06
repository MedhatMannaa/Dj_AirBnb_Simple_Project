from django.db import models
from django.utils import timezone
from django.urls import reverse


# Create your models here.

UNIT_TYPE = (
    ('CHALEH','CHALEH'),
    ('ROOM' , 'ROOM'),
    ('FLAT' , 'FLAT'),
    ('STUDIO' , 'STUDIO'),
    ('Lounge' , 'Lounge'),
)

UNIT_STATUS = (
    ('AVAILABLE TO RENT','AVAILABLE TO RENT'),
    ('RENTED' , 'RENTED'),
    ('AVAILABLE TO SELL','AVAILABLE TO SELL'),
    ('SOLD' , 'SOLD'),
    ('SUSPENDED' , 'SUSPENDED'),

)

# Area Table
class Area(models.Model):
    title = models.CharField(max_length=60, verbose_name='Area', )

    def __str__(self):
        return self.title

# City Table
class City(models.Model):
    title = models.CharField(max_length=60, verbose_name='City', )
    #area = models.ManyToManyField(Area)

    def __str__(self):
        return self.title

# Country Table
class Country(models.Model):
    title = models.CharField(max_length=60, verbose_name='Country', )
    #city = models.ManyToManyField(City)

    def __str__(self):
        return self.title

# Furniture Table
class Furniture(models.Model):
    title = models.CharField(max_length=60, verbose_name='Furniture', )
    #city = models.ManyToManyField(Furniture)

    def __str__(self):
        return self.title

# Rooms Table
class Room(models.Model):
    title = models.CharField(max_length=60, verbose_name='Room', )
    
    def __str__(self):
        return self.title        

# Main Unite Table
class Unit(models.Model):

    title = models.CharField(max_length=60, verbose_name='Unit Title', unique=True ,) # Title
    description = models.TextField(max_length=500, verbose_name='Unit Description') # Description
    price = models.DecimalField(max_digits=10,decimal_places=2) # How much Price
    num_bedrooms = models.IntegerField( verbose_name='Number of Bed rooms') # Count of Closed Rooms
    hole_space = models.IntegerField( verbose_name='Hole Space') # Count of Closed Rooms
    image = models.ImageField(upload_to='units_images/' , blank=True , null=True, verbose_name='Unit Main Image') # Internal Images
    active = models.BooleanField(default=True) # Post Status
    owner_email = models.EmailField(default='m.medhat@dropsgroup.com') # Email
    type = models.CharField(choices=UNIT_TYPE , default='FLAT',max_length=20) # Unite Type
    status = models.CharField(choices=UNIT_STATUS , default='SUSPENDED',max_length=20) # Unite Status
    country = models.ForeignKey(Country, on_delete=models.CASCADE) # Country
    city = models.ForeignKey(City, on_delete=models.CASCADE) # City
    area = models.ForeignKey(Area, on_delete=models.CASCADE) # Area
    #furniture = models.ForeignKey(Furniture, on_delete=models.CASCADE) 
    furniture = models.ManyToManyField(Furniture) # Room Type
    Room = models.ManyToManyField(Room) # Room Type
    remarks = models.TextField(max_length=500, blank=True , null=True, verbose_name='Remarks') # Remarks
    created_at = models.DateTimeField(default=timezone.now) # Post Creation Date

    def __str__(self):
        return self.title       

