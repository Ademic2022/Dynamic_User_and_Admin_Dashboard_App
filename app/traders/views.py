from django.shortcuts import render
from django.http import HttpResponse
# from .models import Person
# from .models import User, TradingData
from .conn import db
from .trader import Trader


# Create your views here.
def simulate_trading(request):


    # Create a list of traders to simulate
    traders = [Trader(f"Trader {i}") for i in range(10)]

    # Simulate trading for each trader
    simulation_duration_minutes = 10
    for trader in traders:
        trader.simulate(db, simulation_duration_minutes)
        trader.store_data(db)

    return HttpResponse("Trading simulation complete.")


# def index(request):
#     return render(request, 'index.html')

# def new_user(request):
#     new_person = {
#         "fname": "Fatimah",
#         "lname": "Hassan"
#     }

#     user = {
#         "name": "balance",
#         "balance": 100
#     }

#     # Access the 'Person' collection and insert the new person
#     Person.insert_one(new_person)

#     # Access the 'User' collection and insert the new user
#     User.insert_one(user)

#     return HttpResponse('New Person added successfully')

# def show_person(request):
#     # Access the 'Person' collection and retrieve all documents
#     person_collection = db['Person']
#     persons = list(person_collection.find())

#     response = ''
#     for person in persons:
#         response += f"First Name: {person['fname']}, Last Name: {person['lname']}<br>"

#     return HttpResponse(response)



# from django.shortcuts import render

# def user_dashboard(request):
#     users = User.objects.all()
#     return render(request, 'user_dashboard.html', {'users': users})

# def admin_dashboard(request):
#     users = User.objects.all()
#     return render(request, 'admin_dashboard.html', {'users': users})

