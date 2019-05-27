from patient.api.serializers import PatientSerializer, PracticeSerializer
from patient.models import Patient, Practice
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .permissions import PatientIsOwner, PracticeIsOwner


class PatientViewSet(viewsets.ModelViewSet):
    """
    Patient endpoint
    """
    queryset = Patient.objects.filter(active=True)
    serializer_class = PatientSerializer
    permission_classes = (IsAuthenticated, PatientIsOwner)
    filter_fields = ('first_name', 'last_name', 'active')
    ordering_fields = ('first_name', 'last_name', 'created', 'updated')
    search_fields = ('first_name', 'last_name', 'email')

    def get_queryset(self):
        return Patient.objects.user_patients(user=self.request.user).filter(active=True)


class PracticeViewSet(viewsets.ModelViewSet):
    """
    Practice endpoint
    """
    queryset = Practice.objects.filter(active=True)
    serializer_class = PracticeSerializer
    permission_classes = (IsAuthenticated, PracticeIsOwner)
    filter_fields = ('patient', 'active')
    ordering_fields = ('date', 'created', 'updated')
    search_fields = ('name', 'notes', 'date')

    def get_queryset(self):
        return Practice.objects.user_practices(user=self.request.user).filter(active=True)
