from manager.api.serializers import ReportSerializer
from manager.models import Report
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .permissions import ReportIsOwner


class ReportViewSet(viewsets.ModelViewSet):
    """
    Patient endpoint
    """
    queryset = Report.objects.filter(zone__active=True)
    serializer_class = ReportSerializer
    permission_classes = (IsAuthenticated, ReportIsOwner)
    filter_fields = ('zone__name',)
    ordering_fields = ('zone__name',)
    search_fields = ('name__name', 'notes')

    def get_queryset(self):
        return Report.objects.filter(user=self.request.user).filter(active=True)
