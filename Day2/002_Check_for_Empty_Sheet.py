# -*- coding: utf-8 -*-

# highlight as new
__highlight__ = 'new'
__author__ = 'maipatana'

__title__ = 'xxxx'
__doc__ = 'This is the text for the button tooltip associated with this script.'

from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory

doc = __revit__.ActiveUIDocument.Document

sheets = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Sheets).WhereElementIsNotElementType().ToElements()
views = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Views).WhereElementIsNotElementType().ToElements()

all_sheets_in_views = []

for view in views:
    number = view.LookupParameter('Sheet Number').AsString() if view.LookupParameter('Sheet Number') else None
    name = view.LookupParameter('Sheet Name').AsString() if view.LookupParameter('Sheet Name') else None
    all_sheets_in_views.append("{} {}".format(number, name))

for sheet in sheets:
    number = sheet.LookupParameter('Sheet Number').AsString() if view.LookupParameter('Sheet Number') else None
    name = sheet.LookupParameter('Sheet Name').AsString() if view.LookupParameter('Sheet Name') else None
    for_check = "{} {}".format(number, name)
    if for_check not in all_sheets_in_views:
        print(for_check)