from django.urls import path

from .views import UserLanguageAPIView

urlpatterns = [
    path('user/language/', UserLanguageAPIView.as_view(), name='api-user-language')
]
