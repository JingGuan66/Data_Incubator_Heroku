from django.core.management.base import BaseCommand, CommandError
from data_scraping.models import Indicator, State, County, Year, StatePop, CountyPop
import requests
from pathlib import Path
import csv


class Command(BaseCommand):
    help = 'Import Indicator from indicator csv, please make sure you have indicator_csv/import_indicator.csv'

    #def add_arguments(self, parser):
    #    parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):
        print ('Download Indicator data')
        run = input('Please Enter "f" fix blank, "s" State, "c" County or "a" All level data: ')
        
        if run == 'f':
            for statepop in StatePop.objects.filter(population=None):
                url = 'https://api.census.gov/data/'+ statepop.year.year +'/acs/acs5?get=NAME,'+ statepop.indicator.indicator_id + '&for=state:'+ statepop.state.state_id+'&key=3e64a91a18f5b875b217f2b413e3f1321baf32a2'
                try:
                    data = requests.get(url)
                    statepop.population = data.json()[1][1]
                    statepop.save()
                    print ("[Y] Saved %s"% statepop.indicator.indicator_name)
                except:
                    print ("[N] Can not save %s - %s"% (statepop.indicator.indicator_id, statepop.indicator.indicator_name))
                    print (url)
            for countypop in CountyPop.objects.filter(population=None):
                url = 'https://api.census.gov/data/'+ countypop.year.year +'/acs/acs5?get=NAME,'+ countypop.indicator.indicator_id + '&for=county:'+ countypop.county.county_id+'&in=state:'+countypop.county.state.state_id+'&key=3e64a91a18f5b875b217f2b413e3f1321baf32a2'
                try:
                    data = requests.get(url)
                    countypop.population = data.json()[1][1]
                    countypop.save()
                    print ("[Y] Saved %s"% countypop.indicator.indicator_name)
                except:
                    print ("[N] Can not save %s - %s"% (countypop.indicator.indicator_id, countypop.indicator.indicator_name))
                    print (url) 
        
        if run == 's' or run == 'a':
            for state in State.objects.all():
                for i in Indicator.objects.all():
                    for y in Year.objects.all():
                        print (y.year, i.indicator_id, state.state_id)
                        statepop, created = StatePop.objects.get_or_create(state=state, indicator=i, year=y)
                        url = 'https://api.census.gov/data/'+ y.year +'/acs/acs5?get=NAME,'+ i.indicator_id + '&for=state:'+ state.state_id+'&key=3e64a91a18f5b875b217f2b413e3f1321baf32a2'
                        try:
                            data = requests.get(url)
                            statepop.population = data.json()[1][1]
                            statepop.save()
                            print ("[Y] Saved %s"% i.indicator_name)
                        except:
                            print ("[N] Can not save %s - %s"% (i.indicator_id, i.indicator_name))
                            print (url)

        if run == 'c' or run == 'a':
            for county in County.objects.all():
                for i in Indicator.objects.all():
                    for y in Year.objects.all():
                        print (y.year, i.indicator_id, county.state.state_id, county.county_id)
                        countypop, created = CountyPop.objects.get_or_create(county=county,indicator=i, year=y)
                        url = 'https://api.census.gov/data/'+ y.year +'/acs/acs5?get=NAME,'+ i.indicator_id + '&for=county:'+ county.county_id+'&in=state:'+county.state.state_id+'&key=3e64a91a18f5b875b217f2b413e3f1321baf32a2'
                        try:
                            data = requests.get(url)
                            countypop.population = data.json()[1][1]
                            countypop.save()
                            print ("[Y] Saved %s"% i.indicator_name)
                        except:
                            print ("[N] Can not save %s - %s"% (i.indicator_id, i.indicator_name))
                            print (url)            
        
