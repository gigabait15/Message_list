from django.urls import path
from .consumer import WSConsumer


ws_urlpatterns = [
    path('ws/message/', WSConsumer.as_asgi())
]