# -*- coding: utf-8 -*-

## Import Class ที่จำเป็น
import clr
clr.AddReference("System")
from System.Collections.Generic import List

from Autodesk.Revit.DB import (
FilteredElementCollector, 
BuiltInCategory, 
ElementId,
UnitUtils,
DisplayUnitType
)

doc = __revit__.ActiveUIDocument.Document
app =  __revit__.Application
uidoc = __revit__.ActiveUIDocument

## Filter หาก Room ทั้งหมดใน View
rooms = FilteredElementCollector(doc,doc.ActiveView.Id)\
.OfCategory(BuiltInCategory.OST_Rooms)\
.WhereElementIsNotElementType()

SELECTED_NAME = "Bed Room"

bedrooms = List[ElementId]() ## สร้างตัวแปรว่างที่ข้อมูลเป็น List ของ ElementId
area = 0 ## สร้างตัวแปรชื่อ area เป็นตัวเลขมีค่า 0 
for room in rooms:
    if room.LookupParameter('Name').AsString() == SELECTED_NAME: ## ถ้าชื่อห้องคือ Bedroom
        area+=room.LookupParameter('Area').AsDouble() ## ให้ + พื้นที่เข้าไปในตัวแปรชื่อ area
        bedrooms.Add(room.Id)

area_in_sqm = UnitUtils.\
ConvertFromInternalUnits(area, DisplayUnitType.DUT_SQUARE_METERS) ## แปลงหน่วยให้เป็น ตารางเมตร

print("Bedroom มีจำนวน {} ห้อง\nพื้นที่ทั้งหมด {} ตารางเมตร\nใน View {}"\
.format(len(bedrooms), area_in_sqm, doc.ActiveView.Name)) ## Print ข้อความออกมาดู

uidoc.Selection.SetElementIds(bedrooms) ## เลือก ห้อง Bedroom ทั้งหมด ใน View ปัจจุบัน