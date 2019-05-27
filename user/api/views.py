from django.utils import translation
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated

from ..models import User
from .serializers import UserLanguageSerializer


class UserLanguageAPIView(RetrieveUpdateAPIView):
    serializer_class = UserLanguageSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        if self.request.user.is_authenticated:
            return User.objects.get(pk=self.request.user.pk)
        return None

    def perform_update(self, serializer):
        instance = serializer.save()
        translation.activate(instance.language)
