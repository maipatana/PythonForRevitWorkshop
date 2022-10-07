# -*- coding: utf-8 -*-

# highlight as new
__highlight__ = 'new'
__author__ = 'maipatana'

__title__ = 'xxxx'
__doc__ = 'This is the text for the button tooltip associated with this script.'

from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory
from Autodesk.Revit.UI import TaskDialog, TaskDialogCommandLinkId, TaskDialogCommonButtons, TaskDialogResult

doc = __revit__.ActiveUIDocument.Document

FILE_LOCATION = "C:\\Users\\User\\Downloads\\"  ## ใช้ไฟล์ Path ของตัวเอง

sheets = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Sheets).WhereElementIsNotElementType().ToElements()

"""
w - เขียนทับไฟล์
r - อ่านไฟล์
a - เพิ่มเข้าไปในไฟล์
"""
with open(FILE_LOCATION + "sheets.csv", "w") as wFile:
    head = "Number, Name"
    wFile.write(head)
    for sheet in sheets:
        data = "{}, {} \n".format(sheet.LookupParameter('Sheet Number').AsString(), sheet.LookupParameter('Sheet Name').AsString())
        wFile.write(data.encode("utf-8"))

mainDialog = TaskDialog("Sheets Export Completed!");
mainDialog.MainInstruction = "Export รายการ Sheets ไปที่ {} เสร็จสิ้น".format(FILE_LOCATION + "sheets.csv")
mainDialog.CommonButtons = TaskDialogCommonButtons.Close
mainDialog.DefaultButton = TaskDialogResult.Close
mainDialog.Show()