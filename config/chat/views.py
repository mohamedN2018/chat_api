from rest_framework.viewsets import ModelViewSet
from .models import Room, Message
from .serializers import ChatRoomSerializer, ChatMessageSerializer
# Create your views here.

app_name = 'chat'

class ChatRoomViewSet(ModelViewSet):
    quryset = Room.objects.all()
    serializer_class = ChatRoomSerializer


class ChatMessageViewSet(ModelViewSet):
    quryset = Message.objects.select_related('user', 'room')
    serializer_class = ChatMessageSerializer

    def get_queryset(self):
        room_uuid = self.request.query_params.get('room', None)
        if room_uuid is not None:
            return self.queryset.filter(room_uuid=room_uuid)
        return self.queryset
