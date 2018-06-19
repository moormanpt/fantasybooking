from django.core.management.base import BaseCommand
from fantasybooking.home.models import Match

class Command(BaseCommand):
    help = 'Resolves the results of a match'

    def handle(self, *args, **options):
        match = Match.objects.exclude(winner__isnull=False).first()
        match.resolve()

        self.stdout.write('Successfully resolved a match')
