from django.contrib import admin
from data_scraping.models import State,County,Indicator,Year,StatePop,CountyPop
import requests

def run_state_indicator(modeladmin, request, queryset):
    for state in queryset:
        for i in Indicator.objects.all():
            for y in Year.objects.all():
                print (y.year, i.indicator_id, state.state_id)
                statepop, created = StatePop.objects.get_or_create(state=state, indicator=i, year=y)
                data = requests.get('https://api.census.gov/data/'+ y.year +'/acs/acs5?get=NAME,'+ i.indicator_id + '&for=state:'+ state.state_id)
                statepop.population = data.json()[1][1]
                statepop.save()

run_state_indicator.short_description = "Run selected state indicator"

class StateAdmin(admin.ModelAdmin):
    list_display = ['state_id', 'state_name', 'state_short_name']
    ordering = ['state_id']
    list_editable = ['state_name', 'state_short_name']
    actions = [run_state_indicator]
admin.site.register(State, StateAdmin)

def run_county_indicator(modeladmin, request, queryset):
        for county in queryset:
            for i in Indicator.objects.all():
                for y in Year.objects.all():
                    print (y.year, i.indicator_id, county.state.state_id, county.county_id)
                    countypop, created = CountyPop.objects.get_or_create(county=county,indicator=i, year=y)
                    data = requests.get('https://api.census.gov/data/'+ y.year +'/acs/acs5?get=NAME,'+ i.indicator_id + '&for=county:'+ county.county_id+'&in=state:'+county.state.state_id)
                    countypop.population = data.json()[1][1]
                    countypop.save()

run_county_indicator.short_description = "Run selected county indicator"

class CountyAdmin(admin.ModelAdmin):
    list_display = ['county_name', 'county_id','state']
    ordering = ['state']
    actions = [run_county_indicator]
admin.site.register(County, CountyAdmin)
admin.site.register(Indicator)
admin.site.register(Year)

class StatePopAdmin(admin.ModelAdmin):
    list_display = ['state', 'indicator', 'year', 'population']
    ordering = ['id']

admin.site.register(StatePop,StatePopAdmin)

class CountyPopAdmin(admin.ModelAdmin):
    def get_state(self, obj):
        return obj.county.state
    list_display = ['county','get_state','indicator', 'year', 'population']
    ordering = ['id']

    

admin.site.register(CountyPop,CountyPopAdmin)

