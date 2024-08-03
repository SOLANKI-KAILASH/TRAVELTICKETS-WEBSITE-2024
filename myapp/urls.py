from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.index,name="index"),
    path('user',views.user,name="user"),
    path("gallery",views.gallery,name="gallery"),
    path("contact",views.contact,name="contact"),
    path("tourpackage",views.tourpackage,name="tourpackage"),
    path("booking",views.booking,name="booking"),
    path("passenger",views.passenger,name="passenger"),
    path("payment",views.payment,name="payment"),
    path("review",views.review,name="review"),
    path("bookingsuccess",views.bookingsuccess,name="bookingsuccess"),
    path("reviewsuccess",views.reviewsuccess,name="reviewsuccess"),
    path("contactsuccess",views.contactsuccess,name="contactsuccess"),
]
