# -*- coding: utf-8 -*-

# highlight as new
__highlight__ = 'new'
__author__ = 'maipatana'

__title__ = 'xxxx'
__doc__ = 'This is the text for the button tooltip associated with this script.'

from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory

doc = __revit__.ActiveUIDocument.Document

## Sheets ทั้งหมด
sheets = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Sheets).WhereElementIsNotElementType().ToElements()

## Views ทั้งหมด
views = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Views).WhereElementIsNotElementType().ToElements()

## ทำ List ว่างไว้รอใส่ Sheet จากใน View
all_sheets_in_views = []

for view in views:  ## Loop ตัว View
    number = view.LookupParameter('Sheet Number').AsString() if view.LookupParameter('Sheet Number') else None
    name = view.LookupParameter('Sheet Name').AsString() if view.LookupParameter('Sheet Name') else None
    for_check = "{} {}".format(number, name)
    all_sheets_in_views.append(for_check)  ## เจอ Sheet Number กับ Name คู่กันก็ใส่ไปใน List

for sheet in sheets:
    number = sheet.LookupParameter('Sheet Number').AsString() if sheet.LookupParameter('Sheet Number') else None
    name = sheet.LookupParameter('Sheet Name').AsString() if sheet.LookupParameter('Sheet Name') else None
    for_check = "{} {}".format(number, name)
    if for_check not in all_sheets_in_views:  ## เช็คว่าชื่อกับเลข Sheet ที่เจออยู่ใน List ที่มาจาก View ไหม
        print(for_check)