# -*- coding: utf-8 -*-

# highlight as new
__highlight__ = 'new'
__author__ = 'maipatana'

__title__ = 'xxxx'
__doc__ = 'This is the text for the button tooltip associated with this script.'

from Autodesk.Revit.DB import UnitUtils, DisplayUnitType, FilteredElementCollector, BuiltInCategory, Transaction, Wall

doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument

def changefrommeter(number):
    ### ถ้าเป็น Version 2021+
    ### return UnitUtils.ConvertToInternalUnits(number, UnitTypeId.Meters)
    return UnitUtils.ConvertToInternalUnits(number, DisplayUnitType.DUT_METERS)

## Get First Wall Type
wt = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Walls).WhereElementIsElementType().ToElements()[0].Id
## Get First Level
levels = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Levels).WhereElementIsNotElementType().ToElements()

## Get Selected Model Lines
lines = [doc.GetElement(i) for i in uidoc.Selection.GetElementIds()]

t = Transaction(doc, 'สร้างผนังจากเส้น Model Line')
t.Start()

for i in lines:
    for level in levels:
        Wall.Create(doc, i.Location.Curve, wt, level.Id, changefrommeter(3), 0, False, False)
    doc.Delete(i.Id)
t.Commit()