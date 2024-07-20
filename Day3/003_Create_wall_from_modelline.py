# -*- coding: utf-8 -*-

from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory, UnitUtils, Transaction, Wall
### ถ้าเป็น Version 2021-
from Autodesk.Revit.DB import DisplayUnitType
### ถ้าเป็น Version 2021+
### from Autodesk.Revit.DB import UnitTypeId

doc = __revit__.ActiveUIDocument.Document
app =  __revit__.Application
uidoc = __revit__.ActiveUIDocument

def changefrommeter(number):
    ### ถ้าเป็น Version 2021+
    ### return UnitUtils.ConvertToInternalUnits(number, UnitTypeId.Meters)
    return UnitUtils.ConvertToInternalUnits(number, DisplayUnitType.DUT_METERS)

## Get First Wall Type
wt = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Walls).WhereElementIsElementType().ToElements()[0].Id
## Get First Level
l = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Levels).WhereElementIsNotElementType().ToElements()[0].Id

## Get Selected Model Lines
lines = [doc.GetElement(i) for i in uidoc.Selection.GetElementIds()]

t = Transaction(doc, 'สร้างผนังจากเส้น Model Line')
t.Start()
for i in lines:
    Wall.Create(doc, i.Location.Curve, wt, l, changefrommeter(3), 0, False, False)
    doc.Delete(i.Id)
t.Commit()