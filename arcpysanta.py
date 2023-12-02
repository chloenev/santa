# import modules
import arcpy
from arcpy import env

# environment settings
env.workspace = "C:\_GEOM67\SantaTracking\SantaPath"

try:

    # variable settings

    table = "CADcities.csv"
    x_coords = "Y"
    y_coords = "X"
    out_layer = "cities1_layer"
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

# set variables
input_table = "C:\_GEOM67\SantaTracking\SantaPath\cities.csv"
out_lines = "C:\_GEOM67\SantaTracking\SantaPath\SantaPath.gdb\XYlines"

# XY to line
arcpy.XYToLine_management(input_table, out_lines, "X_S", "Y_S", "X_E", "Y_E","GEODESIC")     
