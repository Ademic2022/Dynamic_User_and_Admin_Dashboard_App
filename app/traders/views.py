from django.shortcuts import render
from django.http import HttpResponse
from .models import person

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

