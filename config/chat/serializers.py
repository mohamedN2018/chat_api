from rest_framework import serializers
from .models import Room, Message

class ChatRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class ChatMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'