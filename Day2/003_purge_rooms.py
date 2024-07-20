# -*- coding: utf-8 -*-


# highlight as new
__highlight__ = 'updated'
__author__ = 'maipatana'

__title__ = 'Purge Room'
__doc__ = 'This is the text for the button tooltip associated with this script.'

from Autodesk.Revit.UI import TaskDialog, TaskDialogCommandLinkId, TaskDialogCommonButtons, TaskDialogResult
from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory, Transaction

doc = __revit__.ActiveUIDocument.Document

rooms = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Rooms).WhereElementIsNotElementType()

to_delete = []
for room in rooms:
    if room.Area<=0 or room.Location==None:
        to_delete.append(room.Id)

mainDialog = TaskDialog("ลบห้องที่ไม่ได้ใช้");
mainDialog.MainInstruction = "พบห้องที่ไม่ได้ใช้ {} ห้อง".format(len(to_delete))
mainDialog.AddCommandLink(TaskDialogCommandLinkId.CommandLink1, "ดำเนินการลบ")
mainDialog.CommonButtons = TaskDialogCommonButtons.Close
mainDialog.DefaultButton = TaskDialogResult.Close
tResult = mainDialog.Show()
if TaskDialogResult.CommandLink1 == tResult:
    ### เริ่ม Transaction
    t = Transaction(doc, 'Delete unused rooms.')
    t.Start()
    for i in to_delete:
        doc.Delete(i)
    ### จบ Transaction
    t.Commit()