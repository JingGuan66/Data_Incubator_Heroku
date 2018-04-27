from django.db import models

class State(models.Model):
    state_name = models.CharField(max_length = 140)
    state_id = models.CharField(max_length = 140)
    state_short_name = models.CharField(max_length = 2, null=True, blank=True)
    geometry = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.state_name

class County(models.Model):
    state = models.ForeignKey(State,on_delete=models.CASCADE)
    county_name = models.CharField(max_length = 140)
    county_id = models.CharField(max_length = 140)
    geometry = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.county_name        


        
class Year(models.Model):
    year = models.CharField(max_length = 4)
    def __str__(self):
        return str(self.year) 
        
class StatePop(models.Model):
    state = models.ForeignKey(State,on_delete=models.CASCADE)
    indicator = models.ForeignKey('Indicator',on_delete=models.CASCADE)
    year = models.ForeignKey(Year,on_delete=models.CASCADE)
    population = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    def __str__(self):
        return "%s"%self.population   
        
class CountyPop(models.Model):
    county = models.ForeignKey(County,on_delete=models.CASCADE)
    year = models.ForeignKey(Year,on_delete=models.CASCADE)
    indicator = models.ForeignKey('Indicator',on_delete=models.CASCADE)
    population = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    def __str__(self):
        return "%s"%self.population
        
class Indicator(models.Model):
    indicator_name = models.CharField(max_length = 140)
    indicator_id = models.CharField(max_length = 140)
    
    @property
    def state_pops(self):
        return StatePop.objects.filter(indicator=self)
    
    @property
    def county_pops(self):
        return CountyPop.objects.filter(indicator=self)
    
    def __str__(self):
        return self.indicator_name
'''        
class State(models.Model):
    state_ame = models.CharField(max_length = 140)
    body = models.TextField()
    date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title
'''        
