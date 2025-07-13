from django.shortcuts import render
from rest_framework import Modelviewsets
from .models import Room, Message
from .serializers import ChatRoomSerializer, ChatMessageSerializer
# Create your views here.



class ChatRoomView(Modelviewsets):
    quryset = Room.objects.all()
    serializer_class = ChatRoomSerializer


class ChatMessageView(Modelviewsets):
    quryset = Message.objects.select_related('user', 'room')
    serializer_class = ChatMessageSerializer

    def get_queryset(self):
        room_uuid = self.request.query_params.get('room', None)
        if room_uuid is not None:
            return self.queryset.filter(room_uuid=room_uuid)
        return self.queryset()
    