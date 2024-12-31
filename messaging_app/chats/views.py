from rest_framework.permissions import IsAuthenticated
from permissions import IsOwnerOrReadOnly
from rest_framework.viewsets import ModelViewSet

class MessageViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]