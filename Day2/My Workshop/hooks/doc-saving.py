# -*- coding: utf-8 -*-

from pyrevit import forms
from pyrevit import EXEC_PARAMS

from Autodesk.Revit.UI import TaskDialog
from Autodesk.Revit.DB import FilteredElementCollector, BuiltInParameter, BuiltInCategory

from Autodesk.Revit.DB import Transaction, Analysis


doc = EXEC_PARAMS.event_args.Document

rooms = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Rooms).WhereElementIsNotElementType()

to_delete = []
for room in rooms:
    if room.Area<=0 or room.Location==None:
        to_delete.append(room.Id)

ops = ['ลบห้องที่ Not placed จำนวน {} ห้อง'.format(len(to_delete)), 'เลือกคำสั่ง 1', 'เลือกคำสั่ง 2', 'เช็ค Sheet ว่าง']

selected_option = forms.CommandSwitchWindow.show(ops, message='เช็คคุณภาพของ Model ก่อน Save จะดีไหม?')

if selected_option == 'ลบห้องที่ Not placed จำนวน {} หรือไม่?'.format(len(to_delete)):
    ### เริ่ม Transaction
	t = Transaction(doc, 'Delete unused rooms.')
	t.Start()
	for i in to_delete:
	    doc.Delete(i)
	### จบ Transaction
	t.Commit()
elif selected_option =='เลือกคำสั่ง 1':
    TaskDialog("เลือกคำสั่งที่ 1").Show()
elif selected_option =='เลือกคำสั่ง 2':
    TaskDialog("เลือกคำสั่งที่ 2").Show()
elif selected_option =='เช็ค Sheet ว่าง':
    ## Sheets ทั้งหมด
    sheets = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Sheets).WhereElementIsNotElementType().ToElements()

    ## Views ทั้งหมด
    views = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Views).WhereElementIsNotElementType().ToElements()

    ## ทำ List ว่างไว้รอใส่ Sheet จากใน View
    all_sheets_in_views = []
    sheet_names = "รายชื่อ Sheets ที่ไม่มี View\n"
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
            sheet_names += for_check + "\n"
    forms.alert(sheet_names, 'รายชื่อ Sheet ที่ไม่มี View')