# -*- coding: utf-8 -*-


# highlight as new
__highlight__ = 'updated'
__author__ = 'maipatana'

__title__ = 'สร้าง Material Shading'
__doc__ = 'This is the text for the button tooltip associated with this script.'

from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory, Transaction, Material, Color

import clr
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Drawing')

from System.Windows.Forms import OpenFileDialog

doc = __revit__.ActiveUIDocument.Document

all_material_names = []

## ดึง Material ทั้งหมดออกมา
materials = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Materials).WhereElementIsNotElementType().ToElements()


## ถ้ามีชื่อ Material นี้อยู่แล้ว ให้ return ที่มีอยู่แล้ว ถ้ายัง ให้สร้างใหม่และ return ElementId ของ Material ที่สร้างใหม่
def get_existed_mat(name):
    for mat in materials:
        if mat.Name == name:
            return (mat.Id)
    return Material.Create(doc, name)

## กำหนดการเปิด Dialog เพื่อเลือกไฟล์
dialog = OpenFileDialog()
dialog.Filter = "CSV Files (*.csv)|*.csv"  ## กำหนดนามสกุลไฟล์

## เปิด Dialog ขึ้นมา
if dialog.ShowDialog():
    selectedFile = dialog.FileName  ## ชื่อไฟล์ของไฟล์ที่เลือก
    if selectedFile:  ## ถ้าเลือกอะไรสักอย่าง
        with open(selectedFile, 'r') as rFile:  ## เปิดไฟล์ที่เลือก แทนค่าด้วย rFile
            t = Transaction(doc)
            t.Start("Create Material")
            lines = rFile.readlines()  ## อ่านทุกบรรทัด
            for line in lines:  ## loop แต่ละบรรทัด
                raw_data = line.split(',')  ## เรารู้แล้วว่ามันเป็น CSV ไฟล์ มันจะแบ่งกันด้วย , ฉะนั้น split มันออก
                name = raw_data[0]  ## ชื่อ Material อยู่ index แรก
                if name != "material_name":  ## ถ้าชื่อไม่ใช่หัวข้อ
                    r = int(raw_data[1])
                    g = int(raw_data[2])
                    b = int(raw_data[3].strip('\n'))  ## ช่องสุดท้ายจะมี \n ติดมาด้วย เพราะมันขึ้นบรรทัดใหม่
                    new_matId = get_existed_mat(name)
                    new_mat = doc.GetElement(new_matId)
                    new_mat.Color = Color(r, g, b)  ## กำหนด ค่า Shading สี
            t.Commit()