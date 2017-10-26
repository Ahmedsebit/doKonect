from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils import timezone


def validate_booked_date(value):
    content = value
    if content < timezone.now():
        raise ValidationError('Booking date cannot be earlier that today')
    return value