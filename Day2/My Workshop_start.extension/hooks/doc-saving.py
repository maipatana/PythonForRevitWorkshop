# -*- coding: utf-8 -*-

from pyrevit import forms
from pyrevit import EXEC_PARAMS

from Autodesk.Revit.UI import TaskDialog
from Autodesk.Revit.DB import FilteredElementCollector, BuiltInParameter, BuiltInCategory

from Autodesk.Revit.DB import Transaction, Analysis


doc = EXEC_PARAMS.event_args.Document

rooms = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Rooms).WhereElementIsNotElementType()
