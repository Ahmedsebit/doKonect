from django.core.management.base import BaseCommand, CommandError
from patients.models import DoctorServices
from patients.doctors import doctors_services


class Command(BaseCommand):
    help = 'Add doctor services to databse'

    def handle(self, *args, **options):
        for service in doctors_services:
            DoctorServices.objects.create(**service)
            self.stdout.write(self.style.SUCCESS('Successfully added doctors poll'))