### STANDALONE TEXT IMPORTING CSV TO ARCGIS ###

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



### PYTHON WINDOW VERSION ###
import arcpy
arcpy.env.workspace = "C:\_GEOM67\SantaTracking\SantaPath"
arcpy.management.MakeXYEventLayer('CADcities.csv', 'Y', 'X', "TopCities")


### PLOTTING A LINE BETWEEN COORDINATES ###

# description: plotting a line between Santa's workshop and cities across Canada

# startX is start X point, EndX is end X point and similarly for Y's. 
# we will iterate through the input table (and then each row), setting the start/end X/Ys into a point, add the point to an array...
# ... then create a polygon from the array of 2 points. Finally, we insert into a feature class. 


in_rows = arcpy.SearchCursor(data)

point = arcpy.Point()
array = arcpy.Array()

featureList = []
cursor = arcpy.InsertCursor(lines.shp) #need to update shapefile to match which one i want to use :)
feat = cursor.newRow()

for in_row in in_rows:
    # set x and y for start and end points
    point.x = in_row.StartX
    point.y = in_row.StartY
    array.add(point)
    point.x = in_row.EndY
    point.y = in_row.EndY
    array.add(point)

    # create a polyline object base on the array of points
    polyline = arcpy.Polyline(array)

    # clear array for future use
    array.removeAll()

    # append to list of polyline objects
    featureList.append(polyline)

    # insert the feature
    feat.shape = polyline
    cursor.insertRow(feat)

del feat
del cursor
