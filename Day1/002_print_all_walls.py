# -*- coding: utf-8 -*-

from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory, UnitUtils
### ถ้าเป็น Version 2021-
from Autodesk.Revit.DB import DisplayUnitType
### ถ้าเป็น Version 2021+
### from Autodesk.Revit.DB import UnitTypeId

doc = __revit__.ActiveUIDocument.Document
app =  __revit__.Application
uidoc = __revit__.ActiveUIDocument

walls = FilteredElementCollector(doc)\
.OfCategory(BuiltInCategory.OST_Walls)\
.WhereElementIsNotElementType()\
.ToElements()




for wall in walls:
    print('--------')
    print(wall.GetParameters('Length')[0].AsDouble())
    wallType = doc.GetElement(wall.GetTypeId())
    print(wallType.LookupParameter('Type Name').AsString())


### -------------------------------------------------- ###

wall_types = {}  ## Dictionary ว่าง

for wall in walls:
    wallType = doc.GetElement(wall.GetTypeId())
    name = wallType.LookupParameter('Type Name').AsString()
    if name in wall_types.keys(): ## ถ้าชื่อ Type Name เป็น Key อยู่ใน Dictionay wall_types แล้ว
        wall_types[name] += wall.GetParameters('Length')[0].AsDouble()  ## ให้ + ความยาวเพิ่มเข้าไป
    else:  ## ถ้ายัง
        wall_types[name] = wall.GetParameters('Length')[0].AsDouble()  ## ให้เพิ่ม Key:Value เข้าไปใน wall_types

for name in wall_types.keys():
    ### ถ้าเป็น Version 2021+
    ### length = UnitUtils.ConvertFromInternalUnits(wall_types[name], UnitTypeId.Meters)
    length = UnitUtils.ConvertFromInternalUnits(wall_types[name], DisplayUnitType.DUT_METERS)
    print("{} ยาว {} เมตร".format(name, length))