from .consumers import chatConsumer
from django.urls import path
websocket_urlpatterns = [
    path('ws/chatapp/', chatConsumer.as_asgi())
]