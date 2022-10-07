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

ops = ['ลบห้องที่ Not placed จำนวน {} ห้อง'.format(len(to_delete)), 'เลือกคำสั่ง 1', 'เลือกคำสั่ง 2', 'เช็ค View ว่าง']

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
elif selected_option =='เช็ค View ว่าง':
    views = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Views).WhereElementIsNotElementType().ToElements()
    view_names = "รายชื่อ View ที่ไม่มี Element\n"
    for view in views:
        elements_in_view = FilteredElementCollector(doc, view.Id).ToElements()
        if len(elements_in_view) <=0:
            view_names += view.Name + '\n'
    forms.alert(view_names, 'รายชื่อ View ที่ไม่มี Element')