import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from accounts.models import CustomUser
from .models import Thread, Message

class chatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = "broadcast"
        #me = self.scope["user"]
        #other_user_email = self.scope["url_route"]["kwargs"]["email"]
        #other_user = CustomUser.objects.filter(email=other_user_email)
        async_to_sync(self.channel_layer.group_add)(self.room_name, self.channel_name)
        self.accept()

    def disconnect(self, close_code):
        pass
    
    def receive (self, text_data):
        async_to_sync(self.channel_layer.group_send)(
            self.room_name,
            {
                "type": "broadcast.message",
                "text": text_data
            }
        )
        
    def broadcast_message(self, event):
        self.send(text_data=event["text"])