from .models import Message
from .serializer import ChatMessageSerializer
from channels.generic.websocket import AsyncWebsocketConsumer
import json
class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_grop = f'chat_{self.room_name}'

        await self.channel_layer.group_add(
            self.room_grop,
            self.channel_name
        )

        await self.accept()
        # return await super().connect()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.room_grop,
            self.channel_name
        )
        # return await super().disconnect(code)

    async def receive(self, text_date):
        text_data_json = json.loads(text_date)
        message = text_data_json['message']

        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )
        # return await super().receive(text_date)

    
