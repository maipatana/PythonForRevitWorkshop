# -*- coding: utf-8 -*-

from Autodesk.Revit.DB import XYZ, Line, Plane, SketchPlane, Transaction

doc = __revit__.ActiveUIDocument.Document
app =  __revit__.Application
uidoc = __revit__.ActiveUIDocument


start_point = XYZ(0,0,0)
end_point = XYZ(10,10,0)
line = Line.CreateBound(start_point, end_point) 
plane = Plane.CreateByNormalAndOrigin(XYZ(0,0,1), start_point)

t = Transaction(doc, 'สร้าง Line')
t.Start()
skplane = SketchPlane.Create(doc, plane)
doc.Create.NewModelCurve(line , skplane)
t.Commit()
