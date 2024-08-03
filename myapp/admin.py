from django.contrib import admin
from .models import userdetails,country,state,city,destination,trip,bookings,payments,reviews,message,passengers,favourite,contactus
# Register your models here.
#username==kailash
#password==1577
class showuserdetails(admin.ModelAdmin):
    list_display=["name","email","password","date_joined","last_login"]
admin.site.register(userdetails,showuserdetails)

class showcountry(admin.ModelAdmin):
    list_display = ['name', 'code']
admin.site.register(country,showcountry)

class showstate(admin.ModelAdmin):
    list_display=["country","name"]
admin.site.register(state,showstate)

class showcity(admin.ModelAdmin):
    list_display=["state","name"]
admin.site.register(city,showcity)

class showdestination(admin.ModelAdmin):
    list_display=["name","city","description"]
admin.site.register(destination,showdestination)


class showtrip(admin.ModelAdmin):
    list_display=[ 
     "image","title","tripdescription", 'destination', 'departure_location', 'departure_date', 'return_date', 'price', 'available_seats', 
        'total_seats', 'trip_type', 'created_date', 'updated_date', 'is_active'
    ]
admin.site.register(trip,showtrip)

class showbookings(admin.ModelAdmin):
    list_display=['booktrip', 'user', 'booking_date', 'no_of_seats', 'total_price', 'status', 'is_available', 'created_at']
admin.site.register(bookings,showbookings)

class showpayments(admin.ModelAdmin):
    list_display=['booking', 'user', 'amount', 'payment_date', 'payment_method', 'status']
admin.site.register(payments,showpayments)

class showreviews(admin.ModelAdmin):
    list_display=['reviewtrip', 'reviewer', 'rating', 'comment', 'review_date']
admin.site.register(reviews,showreviews)
    
class showmessage(admin.ModelAdmin):
    list_display=['sender', 'receiver', 'content', 'sent_date', 'read']
admin.site.register(message,showmessage)

class showpassengers(admin.ModelAdmin):
    list_display=['booking', 'first_name', 'last_name', 'date_of_birth', 'passport_no']
admin.site.register(passengers,showpassengers)

class showfavourite(admin.ModelAdmin):
    list_display=['user', 'trip', 'added_date', 'available_seats']
admin.site.register(favourite,showfavourite)

class showcontactus(admin.ModelAdmin):
    list_display=["fullname","email","phone","message"]
admin.site.register(contactus,showcontactus)
