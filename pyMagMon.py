#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 1.0.0b1 on Wed Dec  9 09:33:20 2020
#

# This is an automatically generated file.
# Manual changes will be overwritten without warning!

import wx
from TopFrame import TopFrame


class TheApp(wx.App):
    def OnInit(self):
        self.topFrame = TopFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.topFrame)
        self.topFrame.Show()
        return True

# end of class TheApp

if __name__ == "__main__":
    pyMagMon = TheApp(0)
    pyMagMon.MainLoop()
