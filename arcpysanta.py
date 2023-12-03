# description: create XY layer and export to layer file

# import modules
import arcpy
import csv
from arcpy import env

# environment settings
env.workspace = "C:\_GEOM67\SantaTracking\SantaPath"


try:

    # variable settings

    table = "CADcities.csv"
    x_coords = "Y"
    y_coords = "X"
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

# description: plotting a line between Santa's workshop and cities across Canada

# set variables
input_table = "C:\_GEOM67\SantaTracking\SantaPath\cities.csv"
out_lines = "C:\_GEOM67\SantaTracking\SantaPath\SantaPath.gdb\XYcoordlines"

# run XY to line
arcpy.XYToLine_management(input_table, out_lines, "X_S", "Y_S", "X_E", "Y_E","GEODESIC", "Name")      


# description: script reads coordinates in csv format and prints list of pairs with city name for user

print("Jot down your city's accompanying X,Y coordinates! (X_E and Y_E). You will use this to input into our script tool - SantasPathScript - to see his route on the globe!")

with open ("C:\_GEOM67\SantaTracking\SantaPath\cities.csv") as santacities:
     csvReader = csv.reader(santacities)
     for row in csvReader:
          print(row)
