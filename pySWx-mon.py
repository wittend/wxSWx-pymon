#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 1.0.0b1 on Wed Nov  4 09:54:44 2020
#

import wx

# begin wxGlade: dependencies
import wx.grid
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class TopFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: TopFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((1076, 622))
        self.SetTitle("pySWx-mon")

        # Menu Bar
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
        self.SetMenuBar(self.topFrame_menubar)
        # Menu Bar end

        # Tool Bar
        self.topFrame_toolbar = wx.ToolBar(self, -1)
        tool = self.topFrame_toolbar.AddTool(wx.ID_ANY, "New", wx.ArtProvider.GetBitmap(wx.ART_NEW, wx.ART_TOOLBAR, (24, 24)), wx.NullBitmap, wx.ITEM_NORMAL, "", "")
        self.Bind(wx.EVT_TOOL, self.OnFileNew, id=tool.GetId())
        self.topFrame_toolbar.AddTool(wx.ID_ANY, "Open", wx.ArtProvider.GetBitmap(wx.ART_FILE_OPEN, wx.ART_TOOLBAR, (24, 24)), wx.NullBitmap, wx.ITEM_NORMAL, "", "")
        tool = self.topFrame_toolbar.AddTool(wx.ID_ANY, "Save", wx.ArtProvider.GetBitmap(wx.ART_FILE_SAVE, wx.ART_TOOLBAR, (24, 24)), wx.NullBitmap, wx.ITEM_NORMAL, "Save current file", "")
        self.Bind(wx.EVT_TOOL, self.OnFileSave, id=tool.GetId())
        tool = self.topFrame_toolbar.AddTool(wx.ID_ANY, "SaveAs", wx.ArtProvider.GetBitmap(wx.ART_FILE_SAVE_AS, wx.ART_TOOLBAR, (24, 24)), wx.NullBitmap, wx.ITEM_NORMAL, "Save Current File As", "")
        self.Bind(wx.EVT_TOOL, self.OnFIleSaveAs, id=tool.GetId())
        self.SetToolBar(self.topFrame_toolbar)
        self.topFrame_toolbar.Realize()
        # Tool Bar end

        self.topFramePanel = wx.Panel(self, wx.ID_ANY)

        topFramePanelSizer = wx.BoxSizer(wx.VERTICAL)

        self.topFrameSplitterWindow = wx.SplitterWindow(self.topFramePanel, wx.ID_ANY)
        self.topFrameSplitterWindow.SetMinimumPaneSize(20)
        topFramePanelSizer.Add(self.topFrameSplitterWindow, 1, wx.ALL | wx.EXPAND, 3)

        self.topLeftSplitterPane = wx.Panel(self.topFrameSplitterWindow, wx.ID_ANY)
        self.topLeftSplitterPane.SetMinSize((135, -1))

        sizer_1 = wx.BoxSizer(wx.VERTICAL)

        self.topLeftTreeCtrl = wx.TreeCtrl(self.topLeftSplitterPane, wx.ID_ANY)
        sizer_1.Add(self.topLeftTreeCtrl, 1, wx.EXPAND, 0)

        self.topRightSplitterPane = wx.Panel(self.topFrameSplitterWindow, wx.ID_ANY)

        sizer_2 = wx.BoxSizer(wx.VERTICAL)

        self.topRightNBook = wx.Notebook(self.topRightSplitterPane, wx.ID_ANY, style=wx.NB_BOTTOM)
        sizer_2.Add(self.topRightNBook, 1, wx.EXPAND, 0)

        self.topRightNBookPlot = wx.Panel(self.topRightNBook, wx.ID_ANY)
        self.topRightNBook.AddPage(self.topRightNBookPlot, "Plot")

        sizer_3 = wx.BoxSizer(wx.VERTICAL)

        self.eightSpheres = wx.StaticBitmap(self.topRightNBookPlot, wx.ID_ANY, wx.Bitmap("/home/dave/Pictures/BH_Spheres_08_600.jpg", wx.BITMAP_TYPE_ANY))
        sizer_3.Add(self.eightSpheres, 0, wx.ALL, 2)

        self.topRightDataPane = wx.Panel(self.topRightNBook, wx.ID_ANY)
        self.topRightNBook.AddPage(self.topRightDataPane, "Data")

        sizer_4 = wx.BoxSizer(wx.VERTICAL)

        self.topDataGrid = wx.grid.Grid(self.topRightDataPane, wx.ID_ANY, size=(1, 1))
        self.topDataGrid.CreateGrid(10, 4)
        self.topDataGrid.SetColSize(1, 100)
        self.topDataGrid.SetColSize(2, 140)
        self.topDataGrid.SetColSize(3, 312)
        sizer_4.Add(self.topDataGrid, 1, wx.EXPAND, 0)

        self.topRightConfigPane = wx.Panel(self.topRightNBook, wx.ID_ANY)
        self.topRightNBook.AddPage(self.topRightConfigPane, "Config")

        sizer_5 = wx.BoxSizer(wx.VERTICAL)

        self.panel_1 = wx.Panel(self.topRightConfigPane, wx.ID_ANY)
        sizer_5.Add(self.panel_1, 1, wx.EXPAND, 0)

        grid_sizer_1 = wx.FlexGridSizer(7, 5, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        label_1 = wx.StaticText(self.panel_1, wx.ID_ANY, "Parameter 1")
        grid_sizer_1.Add(label_1, 0, wx.ALL, 2)

        self.text_ctrl_1 = wx.TextCtrl(self.panel_1, wx.ID_ANY, "")
        grid_sizer_1.Add(self.text_ctrl_1, 1, wx.ALL, 2)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        label_2 = wx.StaticText(self.panel_1, wx.ID_ANY, "Parameter 2")
        grid_sizer_1.Add(label_2, 0, wx.ALL, 2)

        self.button_1 = wx.ToggleButton(self.panel_1, wx.ID_ANY, "button_1")
        grid_sizer_1.Add(self.button_1, 0, wx.ALL, 2)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.Add((0, 0), 0, 0, 0)

        grid_sizer_1.AddGrowableRow(0)
        grid_sizer_1.AddGrowableRow(1)
        grid_sizer_1.AddGrowableRow(2)
        grid_sizer_1.AddGrowableRow(3)
        grid_sizer_1.AddGrowableRow(4)
        grid_sizer_1.AddGrowableRow(5)
        grid_sizer_1.AddGrowableRow(6)
        grid_sizer_1.AddGrowableCol(0)
        grid_sizer_1.AddGrowableCol(1)
        grid_sizer_1.AddGrowableCol(2)
        grid_sizer_1.AddGrowableCol(3)
        grid_sizer_1.AddGrowableCol(4)
        self.panel_1.SetSizer(grid_sizer_1)

        self.topRightConfigPane.SetSizer(sizer_5)

        self.topRightDataPane.SetSizer(sizer_4)

        self.topRightNBookPlot.SetSizer(sizer_3)

        self.topRightSplitterPane.SetSizer(sizer_2)

        self.topLeftSplitterPane.SetSizer(sizer_1)

        self.topFrameSplitterWindow.SplitVertically(self.topLeftSplitterPane, self.topRightSplitterPane, 175)

        self.topFramePanel.SetSizer(topFramePanelSizer)

        self.Layout()

        # end wxGlade

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

    def OnFIleSaveAs(self, event):  # wxGlade: TopFrame.<event_handler>
        print("Event handler 'OnFIleSaveAs' not implemented!")
        event.Skip()

# end of class TopFrame

class MyApp(wx.App):
    def OnInit(self):
        self.topFrame = TopFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.topFrame)
        self.topFrame.Show()
        return True

# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
