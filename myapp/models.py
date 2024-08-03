from django.db import models

# Create your models here.
class userdetails(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    password=models.CharField(max_length=16)
    date_joined=models.DateField()
    last_login=models.DateTimeField()
    def __str__(self):
        return self.name
    
class country(models.Model):
    name=models.CharField(max_length=30)
    code=models.IntegerField()
    def __str__(self):
        return self.name

class state(models.Model):
    country=models.ForeignKey(country,on_delete=models.CASCADE)
    name=models.CharField(max_length=30)
    def __str__(self):
        return self.name
    
class city(models.Model):
    state=models.ForeignKey(state,on_delete=models.CASCADE)
    name=models.CharField(max_length=30)
    def __str__(self):
        return self.name

class destination(models.Model):
    name=models.CharField(max_length=30)
    city=models.ForeignKey(city,on_delete=models.CASCADE)
    description=models.TextField()
    def __str__(self):
        return self.name

class trip(models.Model):
    image=models.CharField(max_length=20,default=" ")
    title=models.CharField(max_length=100,default=" ")
    tripdescription=models.TextField(default=" ")
    destination=models.ForeignKey(destination,on_delete=models.CASCADE)
    departure_location=models.CharField(max_length=30)
    departure_date=models.DateField()
    return_date=models.DateField()
    price=models.IntegerField()
    available_seats=models.IntegerField()
    total_seats=models.IntegerField()
    trip_type=models.CharField(max_length=30)
    created_date=models.DateField()
    updated_date=models.DateField()
    is_active=models.BooleanField()
    def __str__(self):
        return str(self.destination)

statuslist=[
    ("pending","Pending"),
    ("completed","Completed"),
    ("failed","Failed"),
]

class bookings(models.Model):
    booktrip=models.ForeignKey(trip,on_delete=models.CASCADE)
    user=models.CharField(max_length=30)
    booking_date=models.DateField()
    no_of_seats=models.IntegerField()
    total_price=models.IntegerField()
    status=models.CharField(max_length=30,choices=statuslist,default="pending")
    is_available=models.BooleanField()
    created_at=models.DateField()
    def __str__(self):
        return str(self.booktrip)
    
payment_method_list=[
    ("credit card","Credit Card"),
    ("debit card","Debit Card"),
    ("paypal","PayPal"),
    ("other","Other")
]

class payments(models.Model):
    booking=models.ForeignKey(bookings,on_delete=models.CASCADE)
    user=models.CharField(max_length=40)
    amount=models.IntegerField()    
    payment_date=models.DateField()
    payment_method=models.CharField(max_length=30,choices=payment_method_list)
    status=models.CharField(max_length=30,choices=statuslist)
    

class reviews(models.Model):
    reviewtrip=models.ForeignKey(bookings,on_delete=models.CASCADE)
    reviewer=models.CharField(max_length=30)
    rating=models.IntegerField()
    comment=models.TextField()
    review_date=models.DateField()

class message(models.Model):
    sender=models.ForeignKey(userdetails,on_delete=models.CASCADE)
    receiver=models.CharField(max_length=30)
    content=models.TextField()
    sent_date=models.DateField()
    read=models.BooleanField()

class passengers(models.Model):
    booking=models.ForeignKey(bookings,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    date_of_birth=models.DateField()
    passport_no=models.BigIntegerField()

class favourite(models.Model):
    user=models.CharField(max_length=30)
    trip=models.ForeignKey(destination,on_delete=models.CASCADE)
    added_date=models.DateField()
    available_seats=models.IntegerField()

class contactus(models.Model):
    fullname=models.CharField(max_length=40)
    email=models.EmailField()
    phone=models.BigIntegerField()
    message=models.TextField()

