# STANDALONE TEXT
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



# PYTHON WINDOW VERSION
import arcpy
arcpy.env.workspace = "C:\_GEOM67\SantaTracking\SantaPath"
arcpy.management.MakeXYEventLayer('CADcities.csv', 'Y', 'X', "TopCities")
