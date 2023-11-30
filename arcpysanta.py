# description: create XY layer and export to layer file

# import modules
import arcpy
from arcpy import env

# environment settings
env.workspace = "C:\_GEOM67\SantaTracking\SantaPath"

try:

    # setting variables

    table = "CADcities.csv"
    x_coords = "Y"
    y_coords = "X"
    out_layer = "cities_layer"
    saved_layer = "C:\_GEOM67\SantaTracking\SantaPath\santacities.lyr"

    # set spatial reference
    spref = arcpy.SpatialReference("Sinusoidal (world)")

    # make event layer
    arcpy.management.MakeXYEventLayer(table, x_coords, y_coords, out_layer, spref)

    # save to layer file
    arcpy.SaveToLayerFile_management(out_layer, saved_layer)

except:
        # if error occurs print message(s) to screen
    count = arcpy.GetMessageCount()
    print (arcpy.GetMessage(count-1))
