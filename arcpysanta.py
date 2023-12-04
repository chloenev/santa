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

import arcpy
import csv
from arcpy import env

# environment settings
env.workspace = "C:\_GEOM67\SantaTracking\SantaPath"

# description: plotting a line between Santa's workshop and chosen city's coordinate from python script's generated csv file

# set variables
input_table = "C:\_GEOM67\SantaTracking\SantaPath\cityCoordinates.csv"
out_lines = "C:\_GEOM67\SantaTracking\SantaPath\SantaPath.gdb\XYcoordlines11"

# run XY to line tool (from Santa's workshop to chosen city)
arcpy.XYToLine_management(input_table, out_lines, "Longitude", "Latitude", "X_S", "Y_S","GEODESIC", "City")
