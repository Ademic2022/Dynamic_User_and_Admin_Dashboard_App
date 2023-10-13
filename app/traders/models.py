from django.db import models
from .conn import db

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    balance = models.FloatField(default=100.0)

class TradingData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    profit_loss = models.FloatField()

person = db['Person']