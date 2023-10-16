from django.urls import path
from . import views
from .livefeed import TraderSSEView


urlpatterns = [
    path('', views.index, name='home'),
    path('simulate_trading/<str:trader_name>/', views.simulate_trading, name='simulate_trading'),
    path('lucky_trader/', views.lucky_trader, name='lucky_trader'),
    path('account/<str:trader_name>/', views.account, name='account'),
    path('trade', views.trade, name='trade'),
    path('sse/trader_simulation/', TraderSSEView.as_view(), name='trader_sse'),
    # path('sse/', views.sse_view, name='sse_view'),


]
