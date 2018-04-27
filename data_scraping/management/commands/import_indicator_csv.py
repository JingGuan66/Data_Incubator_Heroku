from django.core.management.base import BaseCommand, CommandError
from data_scraping.models import Indicator
from pathlib import Path
import csv


class Command(BaseCommand):
    help = 'Import Indicator from indicator csv, please make sure you have indicator_csv/import_indicator.csv'

    #def add_arguments(self, parser):
    #    parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):
        filename = "indicator_csv/import_indicator.csv"
        my_file = Path(filename)
        if my_file.exists():
            with open(filename, 'r') as f:
                reader = csv.reader(f)
                for row in reader:
                    indicator_id = row[0]
                    indicator_name = row[1]
                    Indicator.objects.get_or_create(indicator_id=indicator_id, indicator_name=indicator_name)
        else:
            print ("file %s do not exists"%filename)
            
        
