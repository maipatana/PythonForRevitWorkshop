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
    for level in levels:  ## Loop ทุกๆ Level
        ## สร้าง Wall จาก Curve อ่าน doc ที่ https://www.revitapidocs.com/2021.1/0ce4c555-4cee-f5fd-2e84-43cacf34ac5c.htm
        Wall.Create(doc, i.Location.Curve, wt, level.Id, changefrommeter(3), 0, False, False)
    ## ลบเส้น modelline ทิ้ง
    doc.Delete(i.Id)
t.Commit()