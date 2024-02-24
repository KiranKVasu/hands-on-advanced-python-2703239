# Example file for Advanced Python: Hands On by Joe Marini
# Filter values out of a data set based on some criteria

import json
import pprint

# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)

# the filter() function gives us a way to remove unwanted data points
# TODO: create a subset of the data for days that had snowfall
snow_days = list(filter(lambda d: d["snow"] > 0, weatherdata))

pprint.pp(f" total snow_days: {len(snow_days)}")


# TODO: pretty-print the resulting data set
# pprint.pp(snow_days)
# filter can also be used on non-numerical data, like strings

# TODO: create a subset that contains summer days with heavy rain (more than 1 in, about 2.5cm)
def is_summer_rain_day(d):
    summer_months = ["-07-", "-08-"]
    if any(mon in d['date'] for mon in summer_months) and d['prcp'] >1.0:
        return True    
    return False

def cold_wind_rain_day(d):
    from statistics import mean
    print(d["date"])
    print(mean([d["tmin"], d['tmax']]))
    
    if ((d["prcp"] >0.7 or d["snow"]> 0.7) and mean([d["tmin"], d['tmax']])< 45.0 ):
        if  d['awnd'] and d['awnd'] >= 10.0:
            return True   
    return False

cold_windy_rainy_days = list(filter(cold_wind_rain_day, weatherdata))
pprint.pp(f"total cold windy rainy days: {len(cold_windy_rainy_days)}")

rainy_summer_days = list(filter(is_summer_rain_day, weatherdata))
pprint.pp(f"total rainy summer days: {len(rainy_summer_days)}")
# pprint.pp((rainy_summer_days))
