from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index),
    # path('add', views.new_user),
    # path('show', views.show_person),
    # path('admin/', views.admin_dashboard, name='admin_dashboard'),
    path('simulate_trading/', views.simulate_trading, name='simulate_trading'),
]
