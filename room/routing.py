from django.urls import path
from . import consumers2

websocket_urlpatterns = [path("ws/<str:room_name>/", consumers2.ChatConsumer.as_asgi())]
