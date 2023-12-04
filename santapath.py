## Calculating Time & Distance for Santa's Trip from the North Pole to Your City! 
## PSP Group Project 2023
## Section 60, Group 3
## Authors: Andie Herstek and Chloe Nevin 

## Purpose: To allow user to determine how long Santa's trip is (hr/min/sec) from his workshop in the North Pole to their chosen city.
## Description: This program is designed to allow a user to input variables based on their wind conditions (speed and direction)
# as well as the desired number of reindeer they wish Santa to be flying with to arrive at their chosen city's destination. This
# program will then take the user's input variables and calculate the time of Santa's trip as an output message. To keep with the
# Christmas spirit, the program also outputs a holiday drawing and message. From the city's XY coordinates chosen by user, one can
# open ArcGIS to input code into the command line to then see Santa's path mapped from his workshop to their city. Within the ArcGIS file, 
# a script was created to include the user to input known X,Y coordinates if their city did not display on provided list. 

## Assumptions: 
# 1. We assume Santa goes directly from the North Pole to the user's chosen location, 
# and does not travel between destinations prior to returning to his workshop. 
# 2. We assume Santa is always travelling South to his destination. 

## Planned for limitations: ArcGIS script does not calculate Santa's travel time/input variables other than XY, simply displays his route as a line.
# The program is designed for to calculate one trip from the North Pole to one city at a time - no stopping, or addding additional cities. 

## Special cases/known problems:

## Inputs: City of choice from list provided (30 cities), number of reindeer (1-9), wind speed (km/h), wind direction (N or S)
## Outputs: Time (hr/min/sec) it will take for Santa to travel from North Pole to user's city with inputs selected, turtle module drawing

## References: with help from examples at:
# https://ehmatthes.github.io/pcc_2e/beyond_pcc/extracting_from_excel/#extracting-data-from-specific-cells, 
# https://www.geeksforgeeks.org/haversine-formula-to-find-distance-between-two-points-on-a-sphere/, 
# https://www.movable-type.co.uk/scripts/latlong.html
# https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/xy-to-line.htm
# https://stackoverflow.com/questions/49859230/arcpy-create-points-with-xy-and-display-them-correctly
# https://gis.stackexchange.com/questions/88092/calculating-x-and-y-of-line-start-and-line-end-using-arcpy
# https://www.exprodat.com/blog/tip-25-using-the-xy-to-line-tool-4/
# https://pro.arcgis.com/en/pro-app/latest/arcpy/geoprocessing_and_python/setting-script-tool-parameters.htm
## Contributions: 

#   READING CSV FILE
# Import openpyxl module to read Excel file with city lat/long
from openpyxl import load_workbook

# Load the entire workbook
file = r"C:\GEOM67\GroupProject\SantaGIT\santa\top30CADcities.xlsx"
wb = load_workbook(file)

# Load worksheet 
ws = wb['Top30']
all_rows = list(ws.rows)
all_columns = list(ws.columns)
city = all_columns[0]
lat = all_columns[1]
long = all_columns[2]

# --------------------------------------------------------------------------------------------------------------------------------
import csv 
import math
from time import sleep
import turtle 
# random is used to generate random integers for the turtle drawing
from random import randint


while True:
    
    # #   HAVE USER INPUT CHOSEN CITY & WRITE COORDINATES TO FILE FOR USE IN ARCGIS PRO

    # Print list of cities from excel sheet for user to choose from
    print("Below is a list of the top 30 most populated cities in Canada. Please choose one to see how long it will take Santa to fly there in his sleigh.")
    sleep(1.5)

    for i, cell in enumerate (city):
        print(i+1,cell.value)
    print()

    # Display chosen city and its respective lat/long
    # Using 'raise' to raise an exception if number not in range (https://www.w3schools.com/python/ref_keyword_raise.asp
    try:
        chosenCity = int(input("From the above list, what is the number (1-30) of your city of choice? "))
        if chosenCity <1 or chosenCity >30:
            raise ValueError("Invalid input. Please enter a number between 1 and 30.")
    except ValueError as error:
        print("Error:", error)
        exit(1)

    destCity = city[chosenCity-1].value    

    # isolate x (latitude) and y (longitude) from the chosen city row 
    destLat = lat[chosenCity-1].value
    destLong = long[chosenCity-1].value

    # Write coordinates to a .csv file to be used in ArcGIS Pro 
    # Help from https://www.youtube.com/watch?v=DXzEijPCRc8 in understanding how to write headings and rows to file 
    with open('cityCoordinates.csv', 'w', newline='') as csvfile:
        row = ('-99.554603', '80.105289', destCity, str(destLat), str(destLong))
        writer = csv.writer(csvfile)
        writer.writerow(['X_S', 'Y_S', 'City', 'Latitude', 'Longitude'])
        writer.writerow(row)
        csvfile.close()

    # --------------------------------------------------------------------------------------------------------------------------------
    # #   DISTANCE CALCULATION

    def calculate_distance(destinationLat, destinationLong):
        northPoleLat = 80.105289
        northPoleLong = -99.554603

        # Calculate distance between latitudes & longitudes 
        dLat = math.radians(destLat - northPoleLat)
        dLong = math.radians(destLong - northPoleLong)

        # Apply Haversine formula for distance (takes into account the radius of earth = 6,371km)
        # Further explained at https://www.movable-type.co.uk/scripts/latlong.html 
        a = (math.sin(dLat / 2) ** 2) + math.cos(math.radians(northPoleLat)) * math.cos(math.radians(destLat)) * (math.sin(dLong / 2) **2)
        rad = 6371
        c = 2 * math.asin(math.sqrt(a))
        distance = rad * c

        return round(distance, 2)

    # --------------------------------------------------------------------------------------------------------------------------------
    #   SPEED CALCULATION

    # Dictionary of reindeer speeds (each reindeer alone has a speed of 300km/hr)
    reindeerSpeeds = {1:300, 2:600, 3:900, 4:1200, 5:1500, 6:1800, 7:2100, 8:2400, 9:2700}

    # Get number of reindeer (1-9) from user 
    try:
        reindeerNum = int(input("How many reindeers do you want to pull Santa's sleigh? Enter a number from 1-9: "))
        if reindeerNum <1 or reindeerNum >9:
            raise ValueError("Invalid input. Please enter a number between 1 and 9.")          
    except ValueError as error:
        print("Error:", error)
        exit(1)

    # Get wind speed from user 
    try:
        windSpeed = int(input("What is the wind speed (km/hr) in your city currently? Just enter the number (e.g. if the wind speed is 50km/hr, enter 50): "))
    except ValueError:
        print("Invalid input. Please enter a numeric value for wind speed.")
        exit(1)

    # Get wind direction from user 
    windDirection = input("What direction is the wind in your city blowing from? (South or North): ")
    windDirection = windDirection.capitalize()

    if windDirection == 'South':
        speed = reindeerSpeeds[reindeerNum] - windSpeed
    elif windDirection == 'North':
        speed = reindeerSpeeds[reindeerNum] + windSpeed
    else:
        print("Invalid direction. Please choose either 'South' or 'North'!")
        exit(1)

    # --------------------------------------------------------------------------------------------------------------------------------
    #   TIME CALCULATION

    def calculate_time(distanceTravelled, speedSleigh):
        decHours = distanceTravelled / speedSleigh 
        decMinutes = (decHours - int(decHours)) * 60
        decSeconds = decMinutes - int(decMinutes)

        hours = int(decHours)
        minutes = round(decMinutes)
        seconds = round(decSeconds * 60)

        return hours, minutes, seconds

    print()

    # --------------------------------------------------------------------------------------------------------------------------------
    # MAIN - call the functions and print the final message!  

    distance = calculate_distance(destLat, destLong)
    hours, minutes, seconds = calculate_time(distance, speed)


    print("The city you have chosen is", destCity, ", located at", destLat, "degrees latitude and", destLong, "degrees longitude.")
    print("You chose", reindeerNum, "reindeers to fly Santa's sleigh - which will travel at", reindeerSpeeds[reindeerNum], "km/hr.")
    print("And the wind conditions in your city are:", windDirection, "winds travelling at", windSpeed, "km/hr.")
    print()
    sleep(1)
    print("Therefore, it will take Santa and his reindeers", hours, "hour(s)", minutes, "minute(s) and", seconds, "secound(s) to get to your city to deliver presents!")
    print()
    sleep(1)

    # --------------------------------------------------------------------------------------------------------------------------------
    # Ask the user if they would like to run through the program again 

    answer = input("Would you like to try it again with another city? (Y/N)? ")
    answer = answer.upper()
    if answer == "Y":
        True
    elif answer == "N":
        break
    else:
        print("Invalid input. Please enter 'Y' or 'N'.")
        exit(1)
    
# --------------------------------------------------------------------------------------------------------------------------------
# Print final message & use the turtle module to draw a globe with snowflakes  
print("Happy Holidays!")

turtle.bgcolor("lightblue")

# defining different aspects of the drawing the turtle module will create
# drawing the globe
def draw_circle(color, radius, x, y):
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

# writing out a christmas message
def draw_text(message, font_size, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("red")
    turtle.write(message, font=("Arial", font_size, "bold"))

# drawing snowflakes of various sizes
def draw_snowflake(x, y, size):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("white")
    turtle.shape("turtle")
    turtle.setheading(randint(0, 360))
    for _ in range(6):
        turtle.forward(size)
        turtle.backward(size)
        turtle.left(60)
        
def draw_globe_with_text():
    turtle.speed(10)

    # Draw the Earth
    draw_circle("blue", 150, 0, 0)

    # Draw continents
    draw_circle("green", 40, -80, 40) 
    draw_circle("green", 40, 80, 40)   
    draw_circle("green", 40, 0, -30)   
    draw_circle("green", 40, -70, -90) 
    draw_circle("green", 40, 80, -90)  
    draw_circle("green", 40, 160, -30) 

    # Write "Merry Christmas" text
    draw_text("Happy Holidays!", 20, -60, -200)

    # Draw snowflakes
    for _ in range(20):
        x = randint(-200, 200)
        y = randint(-100, 200)
        draw_snowflake(x, y, 10)

    turtle.hideturtle()
    turtle.done()

# Call the function to create drawing
draw_globe_with_text()
