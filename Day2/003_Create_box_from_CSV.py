# -*- coding: utf-8 -*-

# highlight as new
__highlight__ = 'new'
__author__ = 'maipatana'

__title__ = 'xxxx'
__doc__ = 'This is the text for the button tooltip associated with this script.'

from Autodesk.Revit.DB import UnitUtils, DisplayUnitType, Structure, XYZ, Transaction

doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument

def changefrommeter(number):
    ### ถ้าเป็น Version 2021+
    ### return UnitUtils.ConvertToInternalUnits(number, UnitTypeId.Meters)
    return UnitUtils.ConvertToInternalUnits(number, DisplayUnitType.DUT_METERS)

s0 = [doc.GetElement(i) for i in uidoc.Selection.GetElementIds()][0]
sym = s0.Symbol
s_type = Structure.StructuralType.NonStructural
loc = XYZ(0,0,0)

t = Transaction(doc)
t.Start('Create Box')
with open('building_programs.csv', 'r') as rFile:
    lines = rFile.readlines()
    x = 0
    for line in lines:
        data = line.Split(',')
        if data[1] != 'Width':
            y = 0
            width = float(data[1])
            length = float(data[2])
            height = float(data[3])
            count = int(data[4])
            for c in range(count):
                loc = XYZ(changefrommeter(x), changefrommeter((5+length)*c), 0)
                new_box = doc.Create.NewFamilyInstance(loc, sym, s_type)
                new_box.LookupParameter('Width').Set(changefrommeter(width))
                new_box.LookupParameter('Length').Set(changefrommeter(length))
                new_box.LookupParameter('Height').Set(changefrommeter(height))
            x += changefrommeter(5)

t.Commit()