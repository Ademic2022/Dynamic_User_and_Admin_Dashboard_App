# trader.py

import pymongo
import uuid
import random
import time

class Trader:
    def __init__(self, name, balance=100.0):
        self._id = str(uuid.uuid4())
        self.name = name
        self.balance = balance

    def generate_profit_loss(self):
        min_value = -0.10  # -10%
        max_value = 0.10   # +10%
        return random.uniform(min_value, max_value)

    def update_balance(self, profit_loss):
        self.balance += self.balance * profit_loss

    def simulate(self, db, duration_minutes):
        for minute in range(1, duration_minutes + 1):
            profit_loss = self.generate_profit_loss()
            self.update_balance(profit_loss)
            self.store_data(db)
            print(f"{self.name} - Minute {minute}: Balance = ${self.balance:.2f}")
            time.sleep(1)

    def store_data(self, db):
        collection = db[self._id]
        # print('collection created')
        data = {
            "timestamp": int(time.time()),
            "balance": self.balance,
        }
        collection.insert_one(data)
