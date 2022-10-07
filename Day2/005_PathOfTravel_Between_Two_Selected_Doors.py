# -*- coding: utf-8 -*-

# highlight as new
__highlight__ = 'new'
__author__ = 'maipatana'

__title__ = 'xxxx'
__doc__ = 'This is the text for the button tooltip associated with this script.'

__context__ = ["Doors"]

from Autodesk.Revit.DB import UnitUtils, DisplayUnitType, Transaction, Analysis

doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument

def changetometer(number):
    ### ถ้าเป็น Version 2021+
    ### return UnitUtils.ConvertFromInternalUnits(number, UnitTypeId.Meters)
    return UnitUtils.ConvertFromInternalUnits(number, DisplayUnitType.DUT_METERS)

doors = [doc.GetElement(i) for i in uidoc.Selection.GetElementIds()]

### เริ่ม Transaction
t = Transaction(doc, 'Create Path Of Travel between Doors')
t.Start()
for door_start in doors:
    for door_end in doors:
        if door_start.Id != door_end.Id:
            path= Analysis.PathOfTravel.Create(doc.ActiveView, door_start.Location.Point, door_end.Location.Point)
            print(changetometer(path.GetParameters('Length')[0].AsDouble()))
            doc.Delete(path.Id)
### จบ Transaction
t.Commit()