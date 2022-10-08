# -*- coding: utf-8 -*-

from pyrevit import HOST_APP
from pyrevit import forms
from pyrevit import EXEC_PARAMS
from pyrevit import DB, UI
from pyrevit import script

from pyrevit.framework import Windows
from pyrevit.framework import wpf
from pyrevit.coreutils import Guid

import os.path as op

forms.toast(
    "ยินดีต้อนรับสู่ Python for Revit Workshop",
    title="ยินดีต้อนรับสู่ Python for Revit Workshop",
    appid="maipatana",
    click="https://eirannejad.github.io/pyRevit/",
    actions={
        "Open Google":"https://google.com",
        "Open Toast64":"https://github.com/go-toast/toast"
        })

# class DockableExample(Windows.Controls.Page):
#     def __init__(self, xaml_file):
#         wpf.LoadComponent(self, op.join(op.dirname(__file__), xaml_file))
        
#     def do_something(self, sender, args):
#         forms.alert("ใกล้จะจบ Workshop แล้วละ อดทนอีกนิดนะ")

#     def open_dummy_link(self,sender,args):
#         script.open_url("https://google.com")

# class DockableExamplePanelProvider (UI.IDockablePaneProvider):
#     def SetupDockablePane(self, data):
#         data.FrameworkElement = DockableExample("DockableExample.xaml")
#         data.VisibleByDefault = True


# DOCKABLE_PANE_ID = UI.DockablePaneId(Guid.NewGuid())
# HOST_APP.uiapp.RegisterDockablePane(
#     DOCKABLE_PANE_ID,
#     "Maipatana Workshop",
#     DockableExamplePanelProvider()
# )