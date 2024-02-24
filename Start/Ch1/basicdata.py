# Example file for Advanced Python: Hands On by Joe Marini
# Introspect the data to make some determinations

import json
import pprint

# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)

# TODO: What was the warmest day in the data set?
warm_day = max(weatherdata, key= lambda x: x['tmax'])
print(f"warm day {warm_day['date']}")
# max_temp_day = ""
# max_temp = 0
# for d in weatherdata:
#     if d["tmax"] > max_temp:
#         max_temp =  d["tmax"]
#         max_temp_day = d
# pprint.pp(f"Max day:{max_temp_day}, max temp={max_temp}")
    
# TODO: What was the coldest day in the data set?
cold_day = min(weatherdata, key= lambda x: x['tmin'])
print(f"cold day: {cold_day['date']}")

# TODO: How many days had snowfall?
snow_days = [day for day in weatherdata if day["snow"] >0]
print(f"number of snow_days: {len(snow_days)}")

