# Example file for Advanced Python: Hands On by Joe Marini
# Transform data from one format to another

import json
import copy
import pprint

# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)

# the map() function is used to transform data from one form to another
# TODO: Let's convert the weather data from imperial to metric units
def ToC(f):
    return (f - 32) * 5/9


def ToMM(i):
    return i * 25.4


def ToKPH(s):
    return s * 1.60934


def ToMetric(wd):
    new_wd = copy.copy(wd)
    new_wd['tmin'] = ToC(wd['tmin'])
    new_wd['tmax'] = ToC(wd['tmax'])
    new_wd['prcp'] = ToMM(wd['prcp'])
    new_wd['snow'] = ToMM(wd['snow']) if wd['snow']  else 0.0
    new_wd['snwd'] = ToMM(wd['snwd']) if wd['snwd']  else 0.0
    new_wd['awnd'] = ToMM(wd['awnd']) if wd['awnd']  else 0.0
    return new_wd 
# TODO: Use map() to call ToMetric and convert weatherdata to metric
# result = list(map(ToMetric, weatherdata))
# pprint.pp(result[0])

# TODO: use the map() function to convert objects to tuples
# in this case, create tuples with a date and the average of tmin and tmax
Avg_Temp = lambda t1, t2: (t1 + t2) / 2.0
avg_tmp = list(map(lambda x: Avg_Temp(x['tmin'], x['tmax']), weatherdata))
print(avg_tmp[0])
