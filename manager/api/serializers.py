from django.conf import settings
from patient.models import Patient, Practice
from organization.models import Organization
from rest_framework import serializers
from .fields import SorlImageField


class OrganizationForeignKey(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        return Organization.objects.user_orgs(self.context['request'].user)


class PatientSerializer(serializers.ModelSerializer):

    organization = OrganizationForeignKey(required=False)
    picture_big = SorlImageField(settings.PICTURE_BIG,
                                 source='picture',
                                 options=settings.PICTURE_BIG_OPTIONS,
                                 read_only=True)
    picture_small = SorlImageField(settings.PICTURE_SMALL,
                                   source='picture',
                                   options=settings.PICTURE_SMALL_OPTIONS,
                                   read_only=True)

    class Meta:
        model = Patient
        exclude = []

    def save(self):
        # if no organization was provided, get use default organization
        if 'organization' not in self.validated_data:
            user = self.context['request'].user
            self.validated_data['organization'] = Organization.objects.user_default_orgs(user).first()
        super().save()


class PatientForeignKey(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        return Patient.objects.user_patients(self.context['request'].user)


class PracticeSerializer(serializers.ModelSerializer):
    patient = PatientForeignKey()

    class Meta:
        model = Practice
        exclude = []
