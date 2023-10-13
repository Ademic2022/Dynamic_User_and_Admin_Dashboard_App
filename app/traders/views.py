from django.shortcuts import render
from django.http import HttpResponse
from .models import person
from .models import User, TradingData

# Create your views here.
def index(request):
    return render(request, 'index.html')

def new_user(request):
    new_person = {
        "fname":"Fatimah",
        "lname":"Hassan"
    }

    person.insert_one(new_person)
    return HttpResponse('New Person added successfully')

def show_person(request):
    persons = person.find()
    return HttpResponse(persons)



# from django.shortcuts import render

def user_dashboard(request):
    users = User.objects.all()
    return render(request, 'user_dashboard.html', {'users': users})

def admin_dashboard(request):
    users = User.objects.all()
    return render(request, 'admin_dashboard.html', {'users': users})

