from manager.models import Report
from rest_framework import serializers


class ReportSerializer(serializers.ModelSerializer):

    class Meta:
        model = Report
        exclude = ['user']

    def save(self):
        self.validated_data['user'] = self.context['request'].user
        super().save()
