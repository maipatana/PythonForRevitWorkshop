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
materials = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Materials).WhereElementIsNotElementType().ToElements()



def get_existed_mat(name):
    for mat in materials:
        if mat.Name == name:
            return (mat.Id)
    return Material.Create(doc, name)

dialog = OpenFileDialog()
dialog.Filter = "CSV Files (*.csv)|*.csv"
if dialog.ShowDialog():
    selectedFile = dialog.FileName
    if selectedFile:
        with open(selectedFile, 'r') as rFile:
            t = Transaction(doc)
            t.Start("Create Material")
            lines = rFile.readlines()
            for line in lines:
                raw_data = line.split(',')
                name = raw_data[0]
                if name != "material_name":
                    r = int(raw_data[1])
                    g = int(raw_data[2])
                    b = int(raw_data[3].strip('\n'))
                    new_matId = get_existed_mat(name)
                    new_mat = doc.GetElement(new_matId)
                    new_mat.Color = Color(r, g, b)
            t.Commit()