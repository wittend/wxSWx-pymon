# -*- coding: UTF-8 -*-
#
# generated by wxGlade 1.0.0b1 on Sun Dec 27 17:19:54 2020
#
import os
import sys
import wx
# begin wxGlade: dependencies
import wx.grid
# end wxGlade
from pathlib import Path

# begin wxGlade: extracode
import wx
import wx.adv
from wx.lib.dialogs import openFileDialog as OFdialog
import wx.html2 as webview
import numpy as np
from wx.lib import plot as wxplot
from wx.lib.plot import PlotCanvas 
from wx.lib.plot import PlotGraphics
from wx.lib.plot import  PolyLine
from wx.lib.plot import  PolyMarker
# end wxGlade
from  dirTreeCtrlClass import DirTreeCtrl
from  dataDisplayCtrl import DataDisplayCtrl
from  swxLogFileReader import SWxLogFileReader
from  configPageClass import configPage
#rom  nbPlotClass import nbPlotSimple
from  nbPlotClass import createPlot

caption = ("ID", "Name", "X", "Y", "Z")

data = [
    # (1, "Noel", 5570, 2638, 2933),
    # (2, "Martin", 1407, 663, 744),
    # (3, "Antoine", 1364, 652, 712),
    # (4, "Jenifer", 2347, 1140, 1208),
    # (5, "Marc", 1121, 527, 593),
    # (6, "Etienne", 1198, 575, 623),
    # (7, "Louise", 2067, 1004, 1063),
    # (8, "Justine", 2969, 1477, 1492),
    # (9, "Eloise", 2014, 1001, 1013),
    # (10, "Marguerite", 2016, 993, 1024),
    # (11, "Sophie", 7090, 3570, 3520),
    # (12, "Edith", 6098, 3047, 3051),
    # (13, "Jacob", 12758, 6354, 6405),
    # (14, "Nelly", 8880, 4484, 4396),
    ]

class TopFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: TopFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((1076, 622))
        self.SetTitle("pyMagMon")
        homeURL0="https://earth.nullschool.net/#current/wind/surface/level/orthographic=-89.78,20.10,454"
        homeURL1="http://rx.linkfanel.net/"

        #---- Menu Bar -------------------------------------------------------
        self.topFrame_menubar = wx.MenuBar()
        wxglade_tmp_menu = wx.Menu()
        self.topFrame_menubar.FileNew = wxglade_tmp_menu.Append(wx.ID_ANY, "New", "Create a new File")
        self.Bind(wx.EVT_MENU, self.OnFileNew, self.topFrame_menubar.FileNew)
        self.topFrame_menubar.FileOpen = wxglade_tmp_menu.Append(wx.ID_ANY, "Open", "Open a file")
        self.Bind(wx.EVT_MENU, self.OnFileOpen, self.topFrame_menubar.FileOpen)
        self.topFrame_menubar.FileSave = wxglade_tmp_menu.Append(wx.ID_ANY, "Save", "Save the current file")
        self.Bind(wx.EVT_MENU, self.OnFileSave, self.topFrame_menubar.FileSave)
        self.topFrame_menubar.FileSaveAs = wxglade_tmp_menu.Append(wx.ID_ANY, "Save &As", "Save the current file under a new name")
        self.Bind(wx.EVT_MENU, self.OnFileSaveAs, self.topFrame_menubar.FileSaveAs)
        self.topFrame_menubar.FileSaveAll = wxglade_tmp_menu.Append(wx.ID_ANY, "Save All", "Save all Open Files")
        self.Bind(wx.EVT_MENU, self.OnFileSaveAll, self.topFrame_menubar.FileSaveAll)
        self.topFrame_menubar.FileClose = wxglade_tmp_menu.Append(wx.ID_ANY, "Close", "Close current file")
        self.Bind(wx.EVT_MENU, self.OnFileClose, self.topFrame_menubar.FileClose)
        wxglade_tmp_menu.AppendSeparator()
        self.topFrame_menubar.FileExit = wxglade_tmp_menu.Append(wx.ID_ANY, "Exit", "Exit the current application")
        self.Bind(wx.EVT_MENU, self.OnFileExit, self.topFrame_menubar.FileExit)
        self.topFrame_menubar.Append(wxglade_tmp_menu, "File")
        wxglade_tmp_menu = wx.Menu()
        self.topFrame_menubar.EditUndo = wxglade_tmp_menu.Append(wx.ID_ANY, "Undo", "Undo last action")
        self.Bind(wx.EVT_MENU, self.OnEditUndo, self.topFrame_menubar.EditUndo)
        self.topFrame_menubar.EditRedo = wxglade_tmp_menu.Append(wx.ID_ANY, "Redo", "Redo the last action")
        self.Bind(wx.EVT_MENU, self.OnEditRedo, self.topFrame_menubar.EditRedo)
        wxglade_tmp_menu.AppendSeparator()
        self.topFrame_menubar.EditCut = wxglade_tmp_menu.Append(wx.ID_ANY, "Cut", "Cut the selected data")
        self.Bind(wx.EVT_MENU, self.OnEditCut, self.topFrame_menubar.EditCut)
        self.topFrame_menubar.EditCopy = wxglade_tmp_menu.Append(wx.ID_ANY, "Copy", "Copy selected text to the clipboard")
        self.Bind(wx.EVT_MENU, self.OnEditCopy, self.topFrame_menubar.EditCopy)
        self.topFrame_menubar.EditPaste = wxglade_tmp_menu.Append(wx.ID_ANY, "Paste", "Paste the contents from the clipboard")
        self.Bind(wx.EVT_MENU, self.OnEditPaste, self.topFrame_menubar.EditPaste)
        wxglade_tmp_menu.AppendSeparator()
        self.topFrame_menubar.EditPreferences = wxglade_tmp_menu.Append(wx.ID_ANY, "Preferences", "Set preferences")
        self.Bind(wx.EVT_MENU, self.OnEditPreferences, self.topFrame_menubar.EditPreferences)
        self.topFrame_menubar.Append(wxglade_tmp_menu, "Edit")
        wxglade_tmp_menu = wx.Menu()
        self.topFrame_menubar.toolsOptions = wxglade_tmp_menu.Append(wx.ID_ANY, "Options", "")
        self.Bind(wx.EVT_MENU, self.OnToolsOptions, self.topFrame_menubar.toolsOptions)
        self.topFrame_menubar.toolsPreferences = wxglade_tmp_menu.Append(wx.ID_ANY, "Preferences", "")
        self.Bind(wx.EVT_MENU, self.OnToolsPreferences, self.topFrame_menubar.toolsPreferences)
        self.topFrame_menubar.Append(wxglade_tmp_menu, "Tools")
        wxglade_tmp_menu = wx.Menu()
        self.topFrame_menubar.helpAbout = wxglade_tmp_menu.Append(wx.ID_ANY, "About", "")
        self.Bind(wx.EVT_MENU, self.OnHelpAbout, self.topFrame_menubar.helpAbout)
        self.topFrame_menubar.Append(wxglade_tmp_menu, "&Help")
        self.SetMenuBar(self.topFrame_menubar)
        # ---- Menu Bar end -----------------------------------------

        # ---- Tool Bar ---------------------------------------------
        self.topFrame_toolbar = wx.ToolBar(self, -1, style=wx.TB_DEFAULT_STYLE)
        tool = self.topFrame_toolbar.AddTool(wx.ID_ANY, "New", wx.ArtProvider.GetBitmap(wx.ART_NEW, wx.ART_TOOLBAR, (24, 24)), wx.NullBitmap, wx.ITEM_NORMAL, "", "")
        self.Bind(wx.EVT_TOOL, self.OnFileNew, id=tool.GetId())
        tool = self.topFrame_toolbar.AddTool(wx.ID_ANY, "Open", wx.ArtProvider.GetBitmap(wx.ART_FILE_OPEN, wx.ART_TOOLBAR, (24, 24)), wx.NullBitmap, wx.ITEM_NORMAL, "Open a file", "Open a file")
        self.Bind(wx.EVT_TOOL, self.OnFileOpen, id=tool.GetId())
        tool = self.topFrame_toolbar.AddTool(wx.ID_ANY, "Save", wx.ArtProvider.GetBitmap(wx.ART_FILE_SAVE, wx.ART_TOOLBAR, (24, 24)), wx.NullBitmap, wx.ITEM_NORMAL, "Save current file", "")
        self.Bind(wx.EVT_TOOL, self.OnFileSave, id=tool.GetId())
        tool = self.topFrame_toolbar.AddTool(wx.ID_ANY, "SaveAs", wx.ArtProvider.GetBitmap(wx.ART_FILE_SAVE_AS, wx.ART_TOOLBAR, (24, 24)), wx.NullBitmap, wx.ITEM_NORMAL, "Save Current File As", "")
        self.Bind(wx.EVT_TOOL, self.OnFileSaveAs, id=tool.GetId())
        self.topFrame_toolbar.AddSeparator()
        tool = self.topFrame_toolbar.AddTool(wx.ID_ANY, "Back", wx.ArtProvider.GetBitmap(wx.ART_GO_BACK, wx.ART_TOOLBAR, (24, 24)), wx.NullBitmap, wx.ITEM_NORMAL, "Go to the previous page.", "Go to the previous page.")
        self.Bind(wx.EVT_TOOL, self.OnGoBack, id=tool.GetId())
        tool = self.topFrame_toolbar.AddTool(wx.ID_ANY, "Home", wx.ArtProvider.GetBitmap(wx.ART_GO_HOME, wx.ART_TOOLBAR, (24, 24)), wx.NullBitmap, wx.ITEM_NORMAL, "Go to the home page.", "Go to the home page.")
        self.Bind(wx.EVT_TOOL, self.OnGoHome, id=tool.GetId())
        tool = self.topFrame_toolbar.AddTool(wx.ID_ANY, "Forward", wx.ArtProvider.GetBitmap(wx.ART_GO_FORWARD, wx.ART_TOOLBAR, (24, 24)), wx.NullBitmap, wx.ITEM_NORMAL, "Go to the next page.", "Go to the next page.")
        self.Bind(wx.EVT_TOOL, self.OnGoForward, id=tool.GetId())
        self.SetToolBar(self.topFrame_toolbar)
        self.topFrame_toolbar.Realize()
        # ---- Tool Bar end -----------------------------------------

        self.topFramePanel = wx.Panel(self, wx.ID_ANY)
        topFramePanelSizer = wx.BoxSizer(wx.VERTICAL)
        self.topFrameSplitterWindow = wx.SplitterWindow(self.topFramePanel, wx.ID_ANY)
        self.topFrameSplitterWindow.SetMinimumPaneSize(20)
        topFramePanelSizer.Add(self.topFrameSplitterWindow, 1, wx.ALL | wx.EXPAND, 3)
        self.topLeftSplitterPane = wx.Panel(self.topFrameSplitterWindow, wx.ID_ANY)
        self.topLeftSplitterPane.SetMinSize((175, -1))

        sizerTopLeft = wx.BoxSizer(wx.VERTICAL)

        self.home_dir = str(Path.home()) + "/PSWS/Srawdata"
        #home_dir = str(Path.home())

        #self.topLeftTreeCtrl = wx.TreeCtrl(self.topLeftSplitterPane, wx.ID_ANY)
        self.topLeftTreeCtrl = wx.GenericDirCtrl(self.topLeftSplitterPane, dir=self.home_dir)
        self.dirWidget = self.topLeftTreeCtrl
        sizerTopLeft.Add(self.topLeftTreeCtrl, 1, wx.EXPAND, 0)
        self.topRightSplitterPane = wx.Panel(self.topFrameSplitterWindow, wx.ID_ANY)

        sizerTopRight = wx.BoxSizer(wx.VERTICAL)
        self.topRightNBook = wx.Notebook(self.topRightSplitterPane, wx.ID_ANY, style=wx.NB_BOTTOM)
        sizerTopRight.Add(self.topRightNBook, 1, wx.EXPAND, 0)

#========== Begin Data Page ===============================
        self.topRightDataPane = wx.Panel(self.topRightNBook, wx.ID_ANY)
        self.topRightNBook.AddPage(self.topRightDataPane, "Data")
        sizerDataPane = wx.BoxSizer(wx.VERTICAL)
        self.ddCtrl = DataDisplayCtrl(self.topRightDataPane, data)
        sizerDataPane.Add(self.ddCtrl, 1, wx.EXPAND, 0)
#========== Begin Data Page ===============================

#========== Begin  Plot Page ===============================
        self.topRightNBookPlot = wx.Panel(self.topRightNBook, wx.ID_ANY)
        self.topRightNBook.AddPage(self.topRightNBookPlot, "Plot")
        sizerNBPlot = wx.BoxSizer(wx.VERTICAL)
        # self.nbPlot = nbPlotSimple(self.topRightNBookPlot, data)
        # sizerNBPlot.Add(self.nbPlot, 1, wx.EXPAND, 0)
        createPlot(self, self.topRightNBookPlot)
        sizerNBPlot.Add(self.nbplot, 1, wx.EXPAND, 0)
#========== End Plot Page ===============================

#========== Begin Web Page1 ===============================
        self.topRightWebPane = wx.Panel(self.topRightNBook, wx.ID_ANY)
        self.topRightNBook.AddPage(self.topRightWebPane, "Web")
        sizerWebPane = wx.BoxSizer(wx.VERTICAL)
        self.wvTopRight0 = wx.html2.WebView.New(self.topRightWebPane, wx.ID_ANY)
        self.wvTopRight0.LoadURL(homeURL0)
        sizerWebPane.Add(self.wvTopRight0, 1, wx.ALL | wx.EXPAND, 2)
#========== End Web Page1 ===============================

#========== Begin Web Page2 ===============================
        self.topRightNBook_OSMStations = wx.Panel(self.topRightNBook, wx.ID_ANY)
        self.topRightNBook.AddPage(self.topRightNBook_OSMStations, "OSM Stations")
        sizerOSMStations = wx.BoxSizer(wx.HORIZONTAL)
        self.wvTopRight1 = wx.html2.WebView.New(self.topRightNBook_OSMStations, wx.ID_ANY)
        self.wvTopRight1.LoadURL(homeURL1)
        sizerOSMStations.Add(self.wvTopRight1, 1, wx.EXPAND, 0)
#========== End Web Page2 ===============================

#========== Begin  Config Page ===============================
        self.topRightConfigPane = wx.Panel(self.topRightNBook, wx.ID_ANY)
        self.topRightNBook.AddPage(self.topRightConfigPane, "Config")
        sizer_5 = wx.BoxSizer(wx.VERTICAL)
        configPage(self, sizer_5)
#========== End Config Page ===============================

        self.topRightNBook_OSMStations.SetSizer(sizerOSMStations)
        self.topRightWebPane.SetSizer(sizerWebPane)
        self.topRightConfigPane.SetSizer(sizer_5)
        self.topRightDataPane.SetSizer(sizerDataPane)
        self.topRightNBookPlot.SetSizer(sizerNBPlot)
        self.topRightSplitterPane.SetSizer(sizerTopRight)
        self.topLeftSplitterPane.SetSizer(sizerTopLeft)
        self.topFrameSplitterWindow.SplitVertically(self.topLeftSplitterPane, self.topRightSplitterPane, 175)
        self.topFramePanel.SetSizer(topFramePanelSizer)
        self.Layout()

        def OnGoBack(self, event):  # wxGlade: TopFrame.<event_handler>
            if self.wvTopRight.CanGoBack():
                self.wvTopRight.GoBack()
            else:
                event.Skip()

        def OnGoHome(self, event):  # wxGlade: TopFrame.<event_handler>
            self.wvTopRight.LoadURL(self.homeURL)
            event.Skip()

        def OnGoForward(self, event):  # wxGlade: TopFrame.<event_handler>
            if self.wvTopRight.CanGoForward():
                self.wvTopRight.GoForward()
            else:
                event.Skip()

        # end wxGlade
        tree = self.dirWidget.GetTreeCtrl()
        self.Bind(wx.EVT_TREE_SEL_CHANGED, self.OnSelect, id=tree.GetId())

    def OnSelect(self, event):
        """
            OnSelect()
        """
        filePath = self.dirWidget.GetPath()
        if(os.path.isdir(filePath) != True):
            print('self.dirWidget.GetPath(): ' + self.dirWidget.GetPath())
            self.ddCtrl.ClearAll()
            self.ddCtrl.DeleteAllColumns()
            fr = SWxLogFileReader()
            fr.OpenLogFile(self.dirWidget.GetPath(), self.ddCtrl)
        else:
            print('Not a file: ' + self.dirWidget.GetPath())


    def OnFileNew(self, event):  # wxGlade: TopFrame.<event_handler>
        print("Event handler 'OnFileNew' not implemented!")
        event.Skip()

    def OnFileOpen(self, event):  # wxGlade: TopFrame.<event_handler>
        print("Event handler 'OnFileOpen' not implemented!")
        event.Skip()

    def OnFileSave(self, event):  # wxGlade: TopFrame.<event_handler>
        print("Event handler 'OnFileSave' not implemented!")
        event.Skip()

    def OnFileSaveAs(self, event):  # wxGlade: TopFrame.<event_handler>
        print("Event handler 'OnFileSaveAs' not implemented!")
        event.Skip()

    def OnFileSaveAll(self, event):  # wxGlade: TopFrame.<event_handler>
        print("Event handler 'OnFileSaveAll' not implemented!")
        event.Skip()

    def OnFileClose(self, event):  # wxGlade: TopFrame.<event_handler>
        print("Event handler 'OnFileClose' not implemented!")
        event.Skip()

    def OnFileExit(self, event):  # wxGlade: TopFrame.<event_handler>
        print("Event handler 'OnFileExit' not implemented!")
        event.Skip()

    def OnEditUndo(self, event):  # wxGlade: TopFrame.<event_handler>
        print("Event handler 'OnEditUndo' not implemented!")
        event.Skip()

    def OnEditRedo(self, event):  # wxGlade: TopFrame.<event_handler>
        print("Event handler 'OnEditRedo' not implemented!")
        event.Skip()

    def OnEditCut(self, event):  # wxGlade: TopFrame.<event_handler>
        print("Event handler 'OnEditCut' not implemented!")
        event.Skip()

    def OnEditCopy(self, event):  # wxGlade: TopFrame.<event_handler>
        print("Event handler 'OnEditCopy' not implemented!")
        event.Skip()

    def OnEditPaste(self, event):  # wxGlade: TopFrame.<event_handler>
        print("Event handler 'OnEditPaste' not implemented!")
        event.Skip()

    def OnEditPreferences(self, event):  # wxGlade: TopFrame.<event_handler>
        print("Event handler 'OnEditPreferences' not implemented!")
        event.Skip()

    def OnToolsOptions(self, event):  # wxGlade: TopFrame.<event_handler>
        print("Event handler 'OnToolsOptions' not implemented!")
        event.Skip()

    def OnToolsPreferences(self, event):  # wxGlade: TopFrame.<event_handler>
        print("Event handler 'OnToolsPreferences' not implemented!")
        event.Skip()

    def OnHelpAbout(self, event):  # wxGlade: TopFrame.<event_handler>
        description = """PyMagMon is a tool for monitoring and presenting data
from the ground based magnetometer used by the Citizen Science Low Cost Space Weather Station
and Personal Space Weather Station (PSWS) projects.
"""

        licence = """PyMagMon is free software; you can redistribute it and/or
modify it under the terms of version 3 of the GNU General Public License as
published by the Free Software Foundation.

PyMagMon is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

See the GNU General Public License for more details. You should have
received a copy of the GNU General Public License this program;
if not, write to the Free Software Foundation, Inc., 59 Temple Place,
Suite 330, Boston, MA  02111-1307  USA"""


        info = wx.adv.AboutDialogInfo()

        info.SetIcon(wx.Icon('bitmaps/049-windroses_256x256.png', wx.BITMAP_TYPE_PNG))
        info.SetName('PyMagMon')
        info.SetVersion('0.1.0')
        info.SetDescription(description)
        info.SetCopyright('(C) 2020 David Witten')
        info.SetWebSite('http://TangerineSDR.org')
        info.SetLicence(licence)
        info.AddDeveloper('David Witten')
        info.AddDocWriter('David Witten')
        #info.AddArtist('The Tango crew')
        #info.AddTranslator('David Witten')

        wx.adv.AboutBox(info)        
        # print("Event handler 'OnHelpAbout' not implemented!")
        #event.Skip()

    def OnGoBack(self, event):  # wxGlade: TopFrame.<event_handler>
        print("Event handler 'OnGoBack' not implemented!")
        event.Skip()

    def OnGoHome(self, event):  # wxGlade: TopFrame.<event_handler>
        print("Event handler 'OnGoHome' not implemented!")
        event.Skip()

    def OnGoForward(self, event):  # wxGlade: TopFrame.<event_handler>
        print("Event handler 'OnGoForward' not implemented!")
        event.Skip()

    def OnHelpAbout(self, event):  # wxGlade: TopFrame.<event_handler>
        description = """PyMagMon is a tool for monitoring and presenting data
from the ground based magnetometer used by the Citizen Science Low Cost Space Weather Station
and Personal Space Weather Station (PSWS) projects.
"""
        licence = """PyMagMon is free software; you can redistribute it and/or
modify it under the terms of version 3 of the GNU General Public License as
published by the Free Software Foundation.

PyMagMon is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

See the GNU General Public License for more details. You should have
received a copy of the GNU General Public License this program;
if not, write to the Free Software Foundation, Inc., 59 Temple Place,
Suite 330, Boston, MA  02111-1307  USA"""

        info = wx.adv.AboutDialogInfo()
        info.SetIcon(wx.Icon('bitmaps/049-windroses_256x256.png', wx.BITMAP_TYPE_PNG))
        info.SetName('PyMagMon')
        info.SetVersion('0.1.0')
        info.SetDescription(description)
        info.SetCopyright('(C) 2020 David Witten')
        info.SetWebSite('http://TangerineSDR.org')
        info.SetLicence(licence)
        info.AddDeveloper('David Witten')
        info.AddDocWriter('David Witten')
        #info.AddArtist('The Tango crew')
        #info.AddTranslator('David Witten')

        wx.adv.AboutBox(info)        
        # print("Event handler 'OnHelpAbout' not implemented!")
        #event.Skip()

    def OnGoBack(self, event):  # wxGlade: TopFrame.<event_handler>
        print("Event handler 'OnGoBack' not implemented!")
        event.Skip()

    def OnGoHome(self, event):  # wxGlade: TopFrame.<event_handler>
        print("Event handler 'OnGoHome' not implemented!")
        event.Skip()

    def OnGoForward(self, event):  # wxGlade: TopFrame.<event_handler>
        print("Event handler 'OnGoForward' not implemented!")
        event.Skip()


    def OnGoBack(self, event):  # wxGlade: TopFrame.<event_handler>
        print("Event handler 'OnGoBack' not implemented!")
        event.Skip()

    def OnGoHome(self, event):  # wxGlade: TopFrame.<event_handler>
        print("Event handler 'OnGoHome' not implemented!")
        event.Skip()

    def OnGoForward(self, event):  # wxGlade: TopFrame.<event_handler>
        print("Event handler 'OnGoForward' not implemented!")
        event.Skip()

# end of class TopFrame
