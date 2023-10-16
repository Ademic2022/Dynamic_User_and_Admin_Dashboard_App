from django_sse.views import BaseSseView
from .trader import Trader
from .conn import db
import time

class TraderSSEView(BaseSseView):
    def iterator(self):
        trader = Trader("trader_hassan_109f")  
        trader.set_simulation_state("running", db)  # Set simulation state to "running"
        
        duration_minutes = 10  # Set the simulation duration
        try:
            for minute in range(1, duration_minutes + 1):
                profit_loss = trader.generate_profit_loss()
                trader.update_balance(profit_loss)
                trader.total_trades += 1
                trader.store_data(db)

                """Send data to the client"""
                data = {
                    "trader_name": trader.name,
                    "balance": round(trader.balance, 2),
                    "minute": minute,
                }
                yield data
                time.sleep(60)  # Wait for 60 seconds before the next update
        
        except Exception as e:
            """Handle exceptions here, such as logging the error"""
            print(f"Error in SSE view: {e}")
        
        finally:
            trader.set_simulation_state("stopped", db)  # Set simulation state to "stopped"
