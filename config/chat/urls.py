from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ChatRoomViewSet, ChatMessageViewSet

app_name = 'chat'

router = DefaultRouter()
router.register(r'rooms', ChatRoomViewSet, basename='chat_room')
router.register(r'messages', ChatMessageViewSet, basename='chat_message')

urlpatterns = [
    path('api/', include(router.urls)),
]