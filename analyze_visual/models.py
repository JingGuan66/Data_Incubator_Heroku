from django.db import models
from data_scraping.models import State, County, StatePop, CountyPop, Indicator, Year
# Create your models here.

CHART_TYPE = (
    ('BAR', 'Bar Chart'),
    ('GEO', 'Geo Chart'),
    ('LINE', 'Line Chart'),
    ('PIE', 'Pie Chart')
)

class Visual(models.Model):
    name = models.CharField(max_length = 140)
    title = models.CharField(max_length = 140, null=True, blank=True)
    short_title = models.CharField(max_length = 140, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    chart_type = models.CharField(max_length=32, choices=CHART_TYPE, default='GEO')
    indicator = models.ManyToManyField(Indicator)
    order = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
        
class StateInfo(models.Model):
    state = models.ForeignKey(State,on_delete=models.CASCADE)
    visual = models.ForeignKey(Visual,on_delete=models.CASCADE)
    title = models.CharField(max_length = 140, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.title