# -*- coding: utf-8 -*-

# highlight as new
__highlight__ = 'new'
__author__ = 'maipatana'

__title__ = 'xxxx'
__doc__ = 'This is the text for the button tooltip associated with this script.'

from Autodesk.Revit.DB import UnitUtils, DisplayUnitType, Structure, XYZ, Transaction, FilteredElementCollector, BuiltInCategory

doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument

def changefrommeter(number):
    ### ถ้าเป็น Version 2021+
    ### return UnitUtils.ConvertToInternalUnits(number, UnitTypeId.Meters)
    return UnitUtils.ConvertToInternalUnits(number, DisplayUnitType.DUT_METERS)

## ถ้ามี Material ชื่อ นั้นๆอยู่แล้วให้ return ElementId กลับมา ถ้าไม่มี return None
def GetMaterialId(name):
    mats = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Materials).WhereElementIsNotElementType().ToElements()
    for mat in mats:
        if mat.Name == name:
            return mat.Id
    return None

## s0 คือ item แรกที่กำลังเลือกอยู่
s0 = [doc.GetElement(i) for i in uidoc.Selection.GetElementIds()][0]

## เปลี่ยนเป็น Family Symbol
"""
ใน Revit API มี Family 3 แบบ
Family - ทุกอย่างของไฟล์ Family
FamilySymbol - ข้อมูลของ Family น้นๆ หรือที่ในไฟล์ Revit เรียกว่า Type 
FamilyInstance - ตัว Element นั้นๆ ที่เป็นชิ้นๆจับต้องได้
อ่านเพิ่มเติม https://www.revitapidocs.com/2016/a1acaed0-6a62-4c1d-94f5-4e27ce0923d3.htm#:~:text=The%20FamilySymbol%20object%20represents%20a,placed%20the%20Autodesk%20Revit%20project.
"""
sym = s0.Symbol

## กำหนด Type ที่เป็น NonStructural
s_type = Structure.StructuralType.NonStructural

## กำหนด ตำแหน่งเริ่มต้น
loc = XYZ(0,0,0)

t = Transaction(doc)
t.Start('Create Box')
with open('building_programs.csv', 'r') as rFile:  ## เปิดไฟล์ที่เลือก แทนค่าด้วย rFile
    lines = rFile.readlines()  ## อ่านทุกบรรทัด
    x = 0
    for line in lines:  ## loop แต่ละบรรทัด
        data = line.Split(',')  ## เรารู้แล้วว่ามันเป็น CSV ไฟล์ มันจะแบ่งกันด้วย , ฉะนั้น split มันออก
        if data[1] != 'Width':  ## ถ้าไม่ใช่หัวข้อ
            y = 0  ## เริ่มค่า y ที่ 0 
            width = float(data[1])
            length = float(data[2])
            height = float(data[3])
            count = int(data[4])
            color = data[5].strip("\n")  ## ช่องสุดท้ายจะมี \n ติดมาด้วย เพราะมันขึ้นบรรทัดใหม่
            for c in range(count):  ## loop ตามจำนวน count
                loc = XYZ(changefrommeter(x), changefrommeter((5+length)*c), 0)  ## ให้ เว้นระยะไปในแกน Y ทีละ 5+ความยาว
                new_box = doc.Create.NewFamilyInstance(loc, sym, s_type)  ## สร้าง Family ขึ้นมาในตำแหน่งที่กำหนด
                new_box.LookupParameter('Width').Set(changefrommeter(width))  ## กำหนด Parameter
                new_box.LookupParameter('Length').Set(changefrommeter(length))  ## กำหนด Parameter
                new_box.LookupParameter('Height').Set(changefrommeter(height))  ## กำหนด Parameter
                if GetMaterialId(color):
                    new_box.LookupParameter('Material').Set(GetMaterialId(color))  ## กำหนด Parameter
            x += changefrommeter(5)  ## เว้นระยะแกน x เพิ่ม

t.Commit()