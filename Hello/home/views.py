from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contacts
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        "variable1": 4,
        "variable2": 2,
    }
    # messages.success(request, "this is a text message")
    # return HttpResponse("This is Home Page")
    return render(request, "index.html", context)

def about(request):
    # return HttpResponse("This is About Page")
    return render(request, "about.html")

def services(request):
    # return HttpResponse("This is Services Page")
    return render(request, "services.html")

def contact(request):
    # return HttpResponse("This is Contact Page")
    if request.method=='POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        contact = Contacts(name=name, email=email, phone=phone, message=message, date=datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent!")
    return render(request, "contact.html")