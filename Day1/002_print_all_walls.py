from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory

doc = __revit__.ActiveUIDocument.Document
app = __revit__app = __revit__.Application

walls = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Walls).WhereElementIsNotElementType().ToElements()

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
    print("{} ยาว {} เมตร".format(name, wall_types[name]))