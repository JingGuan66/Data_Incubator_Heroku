from django.core.management.base import BaseCommand, CommandError
from data_scraping.models import Indicator, State, County, Year, StatePop, CountyPop
import requests
from pathlib import Path
import csv


class Command(BaseCommand):
    help = 'Export Indicator from indicator to csv, please make sure you have indicator_csv/ folder'

    #def add_arguments(self, parser):
    #    parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):
        #print ('Export Indicator data')
        #run = input('Please Enter "s" State, "c" County level data: ')
            writer = csv.writer(open("indicator_csv/export_data.csv","w"), delimiter=',')
            year = Year.objects.filter(year='2016').first()
        #if run == 'c':
            gender = ("Male", "Female")
            age = ("20 - 21 years", "22 - 24 years", "25 - 29 years", "30 - 34 years", 
                   "35 - 44 years", "45 - 54 years",
                   "55 - 59 years", "60 - 61 years", "62 - 64 years", "65 - 69 years", 
                   "70 - 74 years", "75 years - over")
            job_type = ("In labor force", "In labor force Unemployed")
            header = ["county_name"]
            
            for g in gender:
                for a in age:
                    for j in job_type:
                        name = "%s%s %s"%(g, a, j)
                        header.append(name)
                    header.append("%s%s %s"%(g, a, "In labor force employed"))
            writer.writerow(header)
            for c in County.objects.all().order_by('state__state_name'):
                row = ["%s - %s"%(c.state.state_name, c.county_name)]
                for g in gender:
                    for a in age:
                        for j in job_type:
                            name = "%s%s %s"%(g, a, j)
                            #print ("[*]", name)
                            i = Indicator.objects.filter(indicator_name=name).first()
                            row.append(CountyPop.objects.filter(county = c, indicator=i, year=year).first().population)
                        row.append(row[-2]-row[-1])
                writer.writerow(row)