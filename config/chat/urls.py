from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .view import ChatRoomView, ChatMessageView

APP_NAME = 'chat'

router = DefaultRouter()
router.register(r'rooms', ChatRoomView, basename='chat_room')
router.register(r'messages', ChatMessageView, basename='chat_message')

urlpatterns = [
    path('api/', include(router.urls)),
]