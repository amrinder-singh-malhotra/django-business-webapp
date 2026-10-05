from django.shortcuts import render
from .models import Slidebar, HomeServiceCards, About, Contact

# Create your views here.

def home(request):
    slides = Slidebar.objects.all() 
    services = HomeServiceCards.objects.first() 
    
    context = {
        'items': slides,
        'services': services, # Passed to template
    }
    return render(request, 'home.html', context)


def services(request):
    return render(request, 'services.html')


def documentschecklist(request):
    return render(request, "documentschecklist.html")


def about(request):
    items = About.objects.first()
    return render(request, "about.html", {"items": items} )


def contact(request):
    if request.method=="POST":
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        phone_number=request.POST.get("phone_number")
        email=request.POST.get("email")
        service=request.POST.get("service")
        description=request.POST.get("description")
        
        
        # 1. Create a model instance with your extracted data
        new_contact = Contact(
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            email=email,
            service=service,
            description=description
        )

        # 2. Save it to the database
        new_contact.save()
    return render(request, "contact.html")



