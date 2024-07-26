# -*- coding: utf-8 -*-

import clr
clr.AddReference("System")
from System.Collections.Generic import List

from Autodesk.Revit.DB import (
    FilteredElementCollector, 
    BuiltInCategory, 
    UnitUtils, 
    Transaction, 
    Wall,
    SpatialElementBoundaryOptions,
    SpatialElementBoundaryLocation,
    CurveLoop,
    GeometryCreationUtilities,
    XYZ,
    ElementIntersectsSolidFilter,
    DirectShape,
    ElementId
    )
from Autodesk.Revit.DB import UnitTypeId

doc = __revit__.ActiveUIDocument.Document
app =  __revit__.Application
uidoc = __revit__.ActiveUIDocument

rooms = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Rooms).WhereElementIsNotElementType().ToElements()

def convert_from_m_to_internal(number):
    return UnitUtils.ConvertToInternalUnits(number, UnitTypeId.Meters)

def CreateSolidFromRoomWithHeight(room, height):
    opt = SpatialElementBoundaryOptions()
    opt.SpatialElementBoundaryLocation = SpatialElementBoundaryLocation.Finish
    geo = room.GetBoundarySegments(opt)
    roomLoop = List[CurveLoop]([])
    for h in geo:
        loop = []   
        for seg in h:
            loop.append(seg.GetCurve())
        roomLoop.Add(CurveLoop.Create(loop))
    return GeometryCreationUtilities.CreateExtrusionGeometry(roomLoop, XYZ.BasisZ,convert_from_m_to_internal(height))

for room in rooms:
    solid = CreateSolidFromRoomWithHeight(room, 2.1)
    #ds = DirectShape.CreateElement(doc, ElementId(BuiltInCategory.OST_GenericModel))
    #ds.SetShape([solid])
    fil = ElementIntersectsSolidFilter(solid)
    floors = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Floors).WhereElementIsNotElementType()
    floor_intersect_found = floors.WherePasses(fil).ToElements()
    for interfound in floor_intersect_found:
        print(interfound.Category.Name + "-" + interfound.Name)