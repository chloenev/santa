## Purpose: importing top 30 Canadian cities to provided map
## Description: create XY layer and export to layer file to produce top 30 cities on a map 
## Inputs: using csv file, obtaining city's X.Y coordinates 
## Outputs: creating points as a layer in ArcGIS

# import modules
import arcpy
import csv
from arcpy import env

# environment settings
env.workspace = "C:\_GEOM67\SantaTracking\SantaPath"

try:

    # variable settings

    table = "CADcities.csv"
    x_coords = "X"
    y_coords = "Y"
    out_layer = "cities2_layer"
    saved_layer = "C:\_GEOM67\SantaTracking\SantaPath\santacities.lyr"

    # set spatial reference
    spref = arcpy.SpatialReference("GCS_North_American_1983")

    # make event layer
    arcpy.management.MakeXYEventLayer(table, x_coords, y_coords, out_layer, spref)

    # save to layer file
    arcpy.SaveToLayerFile_management(out_layer, saved_layer)

except:
        # if error occurs print message(s) to screen
    count = arcpy.GetMessageCount()
    print (arcpy.GetMessage(count-1))
## -------------------------------------------------------------------------------------- ##

## Purpose: creation of Santa's travel path generated from user's selected city in main program code
## Description: plotting a line between Santa's workshop and chosen city's coordinate from python script's generated csv file
## Inputs: chosen city's coordinates, in csv format
## Outputs: X,Y line generated from Santa's workshop to user's selected city

# import modules
import arcpy
import csv
from arcpy import env

# environment settings
env.workspace = "C:\_GEOM67\SantaTracking\SantaPath"

# set variables (input = table created from main program, output = new map layer)
input_table = "C:\_GEOM67\SantaTracking\SantaPath\cityCoordinates.csv"
out_lines = "C:\_GEOM67\SantaTracking\SantaPath\SantaPath.gdb\SantasPathXY"

# run XY to line tool (from Santa's workshop to chosen city)
arcpy.XYToLine_management(input_table, out_lines, "Longitude", "Latitude", "X_S", "Y_S","GEODESIC", "City")
