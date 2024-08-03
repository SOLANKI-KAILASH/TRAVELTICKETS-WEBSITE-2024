from django.shortcuts import render,redirect
from .models import contactus,userdetails,trip,bookings,reviews,passengers,payments
# Create your views here.
def index(request):
    return render(request,"index.html")
def user(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        password=request.POST.get("password")
        date_joined=request.POST.get("date_joined")
        last_login=request.POST.get("last_login")
        userinfo=userdetails(name=name,email=email,password=password,date_joined=date_joined,last_login=last_login)
        userinfo.save()
        return redirect("/")
    return render(request,"user.html")

def gallery(request):
    return render(request,"gallery.html")

def contact(request):
    if request.method=="POST":
        fullname=request.POST.get("fullname")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        message=request.POST.get("message")
        contact=contactus(fullname=fullname,email=email,phone=phone,message=message)
        contact.save()
        return redirect("/contactsuccess")
    return render(request,"contact.html")

def tourpackage(request):
    tripData=trip.objects.all()
    data={
        "tripData":tripData,
    }
    return render(request,"tourpackage.html",data)

def booking(request):
    tripData=trip.objects.all()
    data1={
        "tripData":tripData,
    }
    if request.method=="POST":
        booktrip=request.POST.get("booktrip")
        user=request.POST.get("user")
        booking_date=request.POST.get("booking_date")
        no_of_seats=request.POST.get("no_of_seats")
        total_price=request.POST.get("total_price")
        status=request.POST.get("status")
        is_available=request.POST.get("is_available")=="on"
        created_at=request.POST.get("created_at")
        bookingData=bookings(booktrip=trip(id=booktrip),user=user,booking_date=booking_date,no_of_seats=no_of_seats,total_price=total_price,status=status,is_available=is_available,created_at=created_at)
        bookingData.save()
        return redirect('/passenger')
    return render(request,"booking.html",data1)

def passenger(request):
    bookingsData=bookings.objects.all()
    data2={
        "bookingsData":bookingsData,
    }
    if request.method=="POST":
        booking=request.POST.get("booking")
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        date_of_birth=request.POST.get("date_of_birth")
        passport_no=request.POST.get("passport_no")
        passengerData=passengers(booking=bookings(id=booking),first_name=first_name,last_name=last_name,date_of_birth=date_of_birth,passport_no=passport_no)
        passengerData.save()
        return redirect("payment")
    return render(request,"passenger.html",data2)

def payment(request):
    bookingsData=bookings.objects.all()
    data3={
        "bookingsData":bookingsData,
    }
    if request.method=="POST":
        booking=request.POST.get("booking")
        user=request.POST.get("user")
        amount=request.POST.get("amount")
        payment_date=request.POST.get("payment_date")
        payment_method=request.POST.get("payment_method")
        status=request.POST.get("status")
        paymentData=payments(booking=bookings(id=booking),user=user,amount=amount,payment_date=payment_date,payment_method=payment_method,status=status)
        paymentData.save()
        return redirect("/bookingsuccess")
    return render(request,"payment.html",data3)

def review(request):
    bookingsData=bookings.objects.all()
    data3={
        "bookingsData":bookingsData,
    }
    if request.method=="POST":
        reviewtrip=request.POST.get("reviewtrip")
        reviewer=request.POST.get("reviewer")
        rating=request.POST.get("rating")
        comment=request.POST.get("comment")
        review_date=request.POST.get("review_date")
        reviewData=reviews(reviewtrip=bookings(id=reviewtrip),reviewer=reviewer,rating=rating,comment=comment,review_date=review_date)
        reviewData.save()
        return redirect("/reviewsuccess")
    return render(request,"review.html",data3)

def bookingsuccess(request):
    return render(request,"bookingsuccess.html")

def reviewsuccess(request):
    return render(request,"reviewsuccess.html")

def contactsuccess(request):
    return render(request,"contactsuccess.html")

def razorpay(request):
    return render(request,"razorpay.html")