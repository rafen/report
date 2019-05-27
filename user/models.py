from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _
from sorl.thumbnail import ImageField
from django.conf import settings


class User(AbstractUser):
    birthday = models.DateField(blank=True, null=True)
    picture = ImageField(verbose_name=_('Picture'), blank=True, null=True, upload_to='patients')
    address_line_1 = models.CharField(max_length=256, blank=True, null=True,
                                      verbose_name=_('Address line 1'))
    address_line_2 = models.CharField(max_length=256, blank=True, null=True,
                                      verbose_name=_('Address line 2'))
    phone = models.CharField(max_length=128, null=True, blank=True, verbose_name=_('Phone'))
    city = models.CharField(max_length=128, blank=True, null=True,
                            verbose_name=_('City'))
    state = models.CharField(max_length=128, blank=True, null=True,
                             verbose_name=_('State/Province/Region'))
    zip = models.CharField(max_length=128, blank=True, null=True,
                           verbose_name=_('Zip/Postal code'))
    country = models.CharField(max_length=128, blank=True, null=True,
                               verbose_name=_('Country'))
    notes = models.TextField(blank=True, null=True)
    language = models.CharField(
        max_length=10,
        choices=settings.LANGUAGES,
        default=settings.LANGUAGE_CODE,
    )
