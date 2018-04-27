from django.core.management.base import BaseCommand, CommandError
from data_scraping.models import County
from pathlib import Path
import json

class Command(BaseCommand):
    help = 'Import County geometric data from World.geo.json folder'

    #def add_arguments(self, parser):
    #    parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):
        for county in County.objects.all():
            filename = "world.geo.json/countries/USA/%s/%s.geo.json"%(county.state.state_short_name, county.county_name)
            my_file = Path(filename)
            if my_file.exists():
                with open(filename, 'r') as f:
                    geojson = json.load(f)
                    county.geometry = geojson["features"][0]["geometry"]
                    county.save()
                    print ("Save County geometry information %s"%county.county_name)
