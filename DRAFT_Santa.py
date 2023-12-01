# Calculating Time & Distance for Santa's Trip from North Pole to Your City! 
# PSP Group Project 2023
# Section 60, Group 3
# Authors: Andie Herstek and Chloe Nevin 
# Purpose:
# Description:
# Assumptions:
# Planned for limitations: 
# Special cases/known problems:
# Inputs:
# Outputs:
# References:
# Contributions: 

# with help from example at https://ehmatthes.github.io/pcc_2e/beyond_pcc/extracting_from_excel/#extracting-data-from-specific-cells, 
# https://www.geeksforgeeks.org/haversine-formula-to-find-distance-between-two-points-on-a-sphere/, 
# https://www.movable-type.co.uk/scripts/latlong.html

#   READING CSV FILE
#import openpyxl module to read Excel file with city lat/long
from openpyxl import load_workbook

#load the entire workbook
file = r"C:\GEOM67\GroupProject\SantaGIT\santa\top30CADcities.xlsx"
wb = load_workbook(file)

#load worksheet 
ws = wb['Top30']
all_rows = list(ws.rows)
all_columns = list(ws.columns)
city = all_columns[0]
lat = all_columns[1]
long = all_columns[2]

# --------------------------------------------------------------------------------------------------------------------------------
from time import sleep

# print list of cities to choose from
print("Below is a list of the top 30 most populated cities in Canada. Please choose one to see how long it will take Santa to fly there in his sleigh.")
sleep(2)

for i, cell in enumerate (city):
    print(i+1,cell.value)
print()

# print chosen city and its respective lat/long
ChosenCity = int(input("From the above list, what is the number (1-30) of your city of choice? "))
print("The city you have chosen is", city[ChosenCity-1].value)

# isolate x (latitude) and y (longitude) from the chosen city row 
destLat = lat[ChosenCity-1].value
destLong = long[ChosenCity-1].value
print("Your city is located at",destLat, "degrees latitude and", destLong, "degrees longitude")

# #   SETTING LOCATION OF NORTH POLE (ORIGIN)
# northPole = "Rovaniemi, Finland"
# northPoleLat = 66.5433
# northPoleLong = 25.8475

# --------------------------------------------------------------------------------------------------------------------------------
# #   DISTANCE CALCULATION
import math

northPole = "North Pole"
northPoleLat = 80.105289
northPoleLong = -99.554603

# calculate distance between latitudes & longitudes
dLat = (destLat - northPoleLat) * math.pi / 180
dLong = (destLong- northPoleLong) * math.pi / 180

# convert to radians 
lat1 = northPoleLat * (math.pi / 180)
lat2 = destLat * (math.pi / 180)

# apply haversine formula 
a = (pow(math.sin(dLat / 2), 2) + pow(math.sin(dLong / 2), 2) * math.cos(lat1) * math.cos(lat2))
rad = 6371      # radius of Earth
c = 2 * math.asin(math.sqrt(a))
distance = rad * c
print("The distance between Santa's workshop and your city is", round(distance, 2), "km")
print()
sleep(1)

# --------------------------------------------------------------------------------------------------------------------------------
#   SPEED CALCULATION

# Dictionary of reindeer speeds (each reindeer alone has a speed of 80km/hr)
reindeerSpeeds = {1:300, 2:600, 3:900, 4:1200, 5:1500, 6:1800, 7:2100, 8:2400, 9:2700}

# Get number of reindeer (1-9) from user 
#       needs error handling - ONLY numbers 1 through 9 allowed, no letters or sumbols, no <1 or >9
reindeerNum = int(input("How many reindeers do you want to pull Santa's sleigh? Enter a number from 1-9: "))

# Wind speeds 
#       needs error handling - no letters or symbols 
windSpeed = int(input("What is the wind speed (km/hr) in your city currently? Just enter the number (e.g. if the wind speed is 50km/hr, enter 50): "))

windDirection = input("What direction is the wind in your city blowing from? (South or North): ")
if windDirection == 'South':
    speed = reindeerSpeeds[reindeerNum] - windSpeed
elif windDirection == 'North':
    speed = reindeerSpeeds[reindeerNum] + windSpeed
else:
    print("invalid direction")

# --------------------------------------------------------------------------------------------------------------------------------
#   TIME CALCULATION

decHours = distance / speed 
decMinutes = (decHours - int(decHours)) * 60
decSeconds = decMinutes - int(decMinutes)
print(decHours, decMinutes, decSeconds)

hours = int(decHours)
minutes = round(decMinutes)
seconds = round(decSeconds * 60)
print(hours, minutes, seconds)

print()
sleep(1)

# --------------------------------------------------------------------------------------------------------------------------------

print("With", reindeerNum, "reindeers travelling at", reindeerSpeeds[reindeerNum], "km/hr and", windSpeed, "km/hr winds coming from the", windDirection, "it will take Santa", hours, "hours", minutes, "minutes and", seconds, "secounds to get to your city!")

# --------------------------------------------------------------------------------------------------------------------------------
