# -*- coding: utf-8 -*-

# highlight as new
__highlight__ = 'new'
__author__ = 'maipatana'

#__title__ = 'xxxx'
__doc__ = """เลือก Modelline แล้วสร้างผนังบนเส้นเหล่านั้น
เครื่องมือจะทำการลบเส้น Modelline เมื่อเสร็จสิ้น"""

__context__ = "Lines"

from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory, UnitUtils, DisplayUnitType, Transaction, Wall

doc = __revit__.ActiveUIDocument.Document
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