from django.core.management.base import BaseCommand, CommandError
from data_scraping.models import State
from pathlib import Path
import json

class Command(BaseCommand):
    help = 'Import State geometric data from World.geo.json folder'

    #def add_arguments(self, parser):
    #    parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):
        for state in State.objects.all():
            filename = "world.geo.json/countries/USA/%s.geo.json"%state.state_short_name
            my_file = Path(filename)
            if my_file.exists():
                with open(filename, 'r') as f:
                    geojson = json.load(f)
                    state.geometry = geojson["features"][0]["geometry"]
                    state.save()
                    print ("Save State geometry information %s"%state.state_name)
