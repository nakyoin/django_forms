from django.shortcuts import render
from django.http import HttpResponse

def index (request):
    return render (request, "index.html")

def postuser(request):
    print(request.POST)
    name = request.POST.get("name", "undefined")
    email = request.POST.get("email", "undefined")
    phone = request.POST.get("service", "undefined")
    about = request.POST.get("about", "undefined")
    service = request.POST.get("service", "undefined")
    return HttpResponse(f"<h2>Name: {name} <br>  Email: {email} <br>  Phone: {phone} <br> Service: {service} <br>  About car: {about}  </h2>")