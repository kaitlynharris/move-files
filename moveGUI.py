import wx
import movefunctions
import os
import filecopydb

class Frame(wx.Frame):
    def __init__(self, title):
        # get time of last update
        self.lastupdate = filecopydb.getLastUpdate()
        print (self.lastupdate)
        self.lastupdatedisplay = self.lastupdate[1]
        print (self.lastupdatedisplay)

        #create window
        wx.Frame.__init__(self, None, title=title, size = (320,420))
        panel = wx.Panel(self)

        #create menu bar
        menuBar = wx.MenuBar()
        fileMenu = wx.Menu()
        exitItem = fileMenu.Append(wx.NewId(), "Exit")
        menuBar.Append(fileMenu, "File")

        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU, self.exitProgram, exitItem)
        self.CreateStatusBar()

        #create file manip UI

        wx.StaticBox(panel, label='Source and Destination', pos=(10,20), size=(300, 170))

        wx.StaticText(panel, label='Select Source: ', pos=(20,50))
        self.sourcebox = wx.TextCtrl(panel, size=(150,-1), pos=(150,50))
        srcButton = wx.Button(panel, label='Choose...', pos=(210,75))
        srcButton.Bind(wx.EVT_BUTTON, self.selectSource)

        wx.StaticText(panel, label='Select Destination: ', pos=(20,120))
        self.destbox = wx.TextCtrl(panel, size=(150,-1), pos=(150,120))
        destButton = wx.Button(panel, label='Choose...', pos=(210,145))
        destButton.Bind(wx.EVT_BUTTON, self.selectDest)

        save = wx.Button(panel, label='Initiate File Check', pos=(95,200))
        save.Bind(wx.EVT_BUTTON, self.checkFiles)

        wx.StaticBox(panel, label='Status', pos=(10,230), size=(300, 100))
        self.lastcopy = wx.StaticText(panel, label = 'Last Update: ' + self.lastupdatedisplay, pos=(20, 250))
        self.statusmessage = wx.StaticText(panel, label = '', pos=(20, 280))

        save = wx.Button(panel, label='Copy Files', pos=(115,340))
        save.Bind(wx.EVT_BUTTON, self.copyFiles)

        #functions to allow user to set directories in finder

    def selectSource(self, event):
        selectDirDialog = wx.DirDialog(self, message = "Select Source Directory")
        selectDirDialog.ShowModal()
        selection = selectDirDialog.GetPath()
        self.sourcebox.SetValue(value = selection)

    def selectDest(self, event):
        selectDirDialog = wx.DirDialog(self, message = "Select Destination Directory")
        selectDirDialog.ShowModal()
        selection = selectDirDialog.GetPath()
        self.destbox.SetValue(value = selection)

        #allows user to check how many files in the directory have been altered in the past day

    def checkFiles(self, event):
        dirpath = self.sourcebox.GetValue()
        dircontents =  os.listdir(dirpath)
        self.filestocopy = movefunctions.createfilearray(dirpath, dircontents)
        self.statusmessage.SetLabel(label = str(len(self.filestocopy)) + ' recently modified files located')

        #copies files from source directory to destination

    def copyFiles(self, event):
        srcpath = self.sourcebox.GetValue()
        destpath = self.destbox.GetValue()
        movefunctions.copy(self.filestocopy, srcpath, destpath)
        filecopydb.addLatestUpdate()
        self.statusmessage.SetLabel(label = str(len(self.filestocopy)) + ' files copied')
        self.lastupdate = filecopydb.getLastUpdate()
        self.lastupdatedisplay = self.lastupdate[1]
        self.lastcopy.SetLabel(label = 'Last Update: ' + self.lastupdatedisplay)

    def exitProgram(self, event):
        self.Destroy()

def main():
    app = wx.App()
    frame = Frame("File Copier")
    frame.Show()
    app.MainLoop()

if __name__ == "__main__": main()
