"""
Prorama para la modifición de una cabecera DICOM para seguir usando el CDMAM
Analysis V1.5.5. Esta es la interfaz gráfica para que sea más fácil usar.

V1.0 del 10/08/26 - Se crea la rutina básica
V2.0 del 12/08/26 - Se crea la interfáz básica para utilizar la rutina base. Se
                    crea primeramente la versión de Linux (porque aquí se 
                    programa) y se usa wx para la interfaz.
V2.1 del 18/08/26 - Se optimiza la interfaz para que sea multiplataforma (win y Linux) 
"""

import wx
from wx.adv import CalendarCtrl
from os import environ, path
import pydicom
from platform import system
import sys





#aplicación de modificación de fechas
class mod_app(wx.Frame):

    #iniciamos la clase
    def __init__(self, *args, **kargs):
        super(mod_app, self).__init__(*args, **kargs)
        self.bob()

    #función que depende de la plataforma
    if system() == 'Linux':
        def resource_path(self, relative_path):
            """ Get absolute path to resource, works for dev and for PyInstaller """
            base_path = getattr(sys, '_MEIPASS', path.dirname(path.abspath(__file__)))
            return path.join(base_path, relative_path)


    def bob(self):
        #------------------------------------------------------------
        #                     Ventana General
        #------------------------------------------------------------        
        #va a faltar un icono depende de la plataforma(?)
        if system() == 'Linux':
            bundle = wx.IconBundle()
            bundle.AddIcon(self.resource_path('CFI_512.png'), wx.BITMAP_TYPE_PNG)
            bundle.AddIcon(self.resource_path('CFI_256.png'), wx.BITMAP_TYPE_PNG)
            bundle.AddIcon(self.resource_path('CFI_128.png'), wx.BITMAP_TYPE_PNG)
            bundle.AddIcon(self.resource_path('CFI_96.png'), wx.BITMAP_TYPE_PNG)
            bundle.AddIcon(self.resource_path('CFI_72.png'), wx.BITMAP_TYPE_PNG)
            bundle.AddIcon(self.resource_path('CFI_64.png'), wx.BITMAP_TYPE_PNG)
            bundle.AddIcon(self.resource_path('CFI_48.png'), wx.BITMAP_TYPE_PNG)
            bundle.AddIcon(self.resource_path('CFI_32.png'), wx.BITMAP_TYPE_PNG)
            bundle.AddIcon(self.resource_path('CFI_24.png'), wx.BITMAP_TYPE_PNG)
            bundle.AddIcon(self.resource_path('CFI_16.png'), wx.BITMAP_TYPE_PNG)
            self.SetIcons(bundle)
        elif system() == 'Windows':
            self.SetIcon(wx.Icon('CFI.ico'))       
        
        
        #ventana princial
        if system() == 'Linux':
            self.SetSize((540,530))
        elif system() == 'Windows':
            self.SetSize((540,485))
        self.SetTitle('Modificador de Fecha')
        self.pnl = wx.Panel(self)
        self.pnl.SetBackgroundColour((1, 55, 110))
        self.Centre()

        #------------------------------------------------------------
        #                     Menú
        #------------------------------------------------------------ 
        #generamos un menubar
        self.menubar = wx.MenuBar()

        #menú archivo
        fileMenu = wx.Menu()

        #añadimos cerrar
        quitItem = wx.MenuItem(fileMenu, wx.ID_EXIT, '&Cerrar\tCtrl+Q', 'Cerrar la aplicación')
        quitItem.SetBitmap(wx.ArtProvider.GetBitmap(wx.ART_QUIT))
        fileMenu.Append(quitItem)

        #menú ayuda
        helpMenu = wx.Menu()

        #se añade el primer elemento
        helpItem = wx.MenuItem(helpMenu, wx.ID_HELP, 'A&yuda ...\tCtrl+H', 'Ayuda de uso')
        helpItem.SetBitmap(wx.ArtProvider.GetBitmap(wx.ART_HELP))
        helpMenu.Append(helpItem)
        aboutItem = wx.MenuItem(helpMenu, wx.ID_ABOUT, '&Acerca de ...\tCtrl+U', 'Información sobre la aplicación')
        aboutItem.SetBitmap(wx.ArtProvider.GetBitmap(wx.ART_INFORMATION))
        helpMenu.Append(aboutItem)

        #añadimos a la barra de menús
        self.menubar.Append(fileMenu, '&Archivo')
        self.menubar.Append(helpMenu, 'A&yuda')

       # Por último añadimos la barra de menú 
        self.SetMenuBar(self.menubar) #aquí lo ponemos         


        #------------------------------------------------------------
        #             Estructuras de la venta principal
        #------------------------------------------------------------ 
        #general sizer
        genSizer = wx.BoxSizer(wx.VERTICAL)

        #box de configuración
        configSB = wx.StaticBox(self.pnl, label='Configuración')
        configSB.SetForegroundColour((255,255,255))
        configSBS  = wx.StaticBoxSizer(configSB, wx.VERTICAL)

        sufijoText = wx.StaticText(configSB,label='Sufijo')
        sufijoText.SetForegroundColour((255,255,255))
        self.sufijoTextCtrl = wx.TextCtrl(configSB, value='_mod', style=wx.TE_CENTRE)
        fechaText = wx.StaticText(configSB, label ='Fecha')
        fechaText.SetForegroundColour((255,255,255))
        self.fecha = CalendarCtrl(configSB, date=wx.DateTime(15,5,2010))

        configSBS.Add(sufijoText, flag=wx.ALIGN_CENTER|wx.ALL, border=5)
        configSBS.Add(self.sufijoTextCtrl, flag=wx.ALIGN_CENTER|wx.ALL, border=5)
        configSBS.Add(fechaText, flag=wx.ALIGN_CENTER|wx.ALL, border=5)
        configSBS.Add(self.fecha, flag=wx.ALIGN_CENTER|wx.ALL, border=5)
        


        #se añade un static box sizer para que esté la salida
        outSB = wx.StaticBox(self.pnl, label='Directorio de salida')
        outSB.SetForegroundColour((255,255,255))
        outSBS = wx.StaticBoxSizer(outSB, wx.VERTICAL)
        hBS = wx.BoxSizer(wx.HORIZONTAL)
        if system() == 'Linux':
            self.savepathTextCtrl = wx.TextCtrl(outSB,
                                            value=environ.get('HOME') or environ.get('USERPROFILE'),
                                            style=wx.TE_CENTRE, size=(400,33))
        elif system() == 'Windows':
            self.savepathTextCtrl = wx.TextCtrl(outSB,
                                            value=environ.get('HOME') or environ.get('USERPROFILE'),
                                            style=wx.TE_CENTRE, size=(400,22))

        self.savepathButton = wx.Button(outSB, label='...')
        hBS.Add(self.savepathTextCtrl, flag=wx.ALIGN_CENTER|wx.ALL, border=5)        
        hBS.Add(self.savepathButton, flag=wx.ALIGN_CENTER|wx.ALL, border=5)        
        
        outSBS.Add(hBS, flag=wx.ALIGN_CENTER|wx.ALL, border=5)
        
        #añadimos el boton chido
        self.cambioButton = wx.Button(self.pnl, label='Cambiar', size=(140, 60))
        self.cambioButton.SetFocus()
    
        # #añadimos todo
        genSizer.Add(configSBS, flag=wx.EXPAND|wx.ALL, border=5)
        genSizer.Add(outSBS, flag=wx.EXPAND|wx.ALL, border=5)
        genSizer.Add(self.cambioButton, flag=wx.ALIGN_CENTER|wx.ALL, border=5)

        self.pnl.SetSizer(genSizer)
        self.pnl.Layout() #muy necesario en windows

        #------------------------------------------------------------
        #                     Binds
        #------------------------------------------------------------
        self.Bind(wx.EVT_MENU, self.OnQuit, quitItem)
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)
        self.Bind(wx.EVT_MENU, self.OnHelp, helpItem)
        self.Bind(wx.EVT_BUTTON, self.OnPath, self.savepathButton)
        self.Bind(wx.EVT_BUTTON, self.OnCambiar, self.cambioButton)

    
    def OnQuit(self, e):
        #Rutina de cerrar
        self.Close()

    def OnAbout(self, e):
        #rutina de información about
        wx.MessageBox("Mod fecha Dicom \nV 2.1 \n Contacto: edlope@fisica.unam.mx \n RLH - 18/08/2026",
                      "Acerca de...", wx.OK|wx.ICON_INFORMATION)

    def OnHelp(self,e):
        #rutina de intrucciones de ayuda
        wx.MessageBox("El Sufijo se agregará al nombre del archivo modificado\n" \
                    "La fecha elegida será la nueva fecha del estudio\n" \
                    "La ruta de salida es donde se guardarán las imágenes modificadas\n" \
                    "El botón modificar permite seleccionar los archivos a modificar",
                      "Ayuda", wx.OK|wx.ICON_INFORMATION)

    def OnPath(self,e):
        #rutina para elegir path de guardado
        with wx.DirDialog(self, message='Ruta de Guardado', style=wx.DD_DEFAULT_STYLE) as dirDialog:   # wx.FD_MULTIPLE

            if dirDialog.ShowModal() == wx.ID_CANCEL:
                return     

            self.savepathTextCtrl.SetValue(dirDialog.GetPath())
            print(dirDialog.GetPath())

    def OnCambiar(self, e):
        #rutina para cambiar las fechas
        with wx.FileDialog(self,message='Elige los archivos a cambiar',
                           wildcard="Archivos Dicom (*.dcm, *.DCM)|*.dcm;*.DCM | Todos los Archivos (*.*, *)|*.*;*",
                           style=wx.FD_MULTIPLE) as fileDialog:
            
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return     

            #obtenemos la información necesaria
            if system() == 'Linux':
                savepath = self.savepathTextCtrl.GetValue()+'/'
            elif system() == 'Windows': 
                savepath = self.savepathTextCtrl.GetValue()+'\\'

            fecha = self.fecha.GetDate().Format('%Y%m%d')
            for file in fileDialog.GetPaths():
                if system() == 'Linux':
                    name = file.split('/')[-1]
                elif system() == 'Windows':
                    name = file.split('\\')[-1]
                try:
                    im = pydicom.dcmread(file)
                except:
                    errorDia = wx.MessageDialog(self, 'No se ha podido abrir la imagen dicom\nrevise el archivo',
                                     caption='Error al abrir %s' % name,
                                     style=wx.OK|wx.ICON_ERROR)
                    errorDia.ShowModal()
                    return
                im.StudyDate = fecha

                try:
                    if name.find('.dcm') == -1 and name.find('.DCM') == -1:
                        pydicom.dcmwrite(savepath+name+'_mod.dcm', im)
                    else:
                        if system() == 'Linux':
                            pydicom.dcmwrite(savepath+'/'+name[:-4]+'_mod.dcm', im)
                        elif system() == 'Windows':
                            pydicom.dcmwrite(savepath+'\\'+name[:-4]+'_mod.dcm', im)
                except:
                    errorDia = wx.MessageDialog(self, 'No se ha podido guardar la imagen dicom\nrevise el archivo',
                                        caption='Error al guardar %s' % name,
                                     style=wx.OK|wx.ICON_ERROR)
                    errorDia.ShowModal()
                    return

            wx.MessageBox('Todos los archivos modificados ✔','Estado',wx.OK|wx.ICON_INFORMATION)



#rutina main
if __name__ == '__main__':
    App =wx.App()
    ex = mod_app(None, style=wx.MINIMIZE_BOX|wx.SYSTEM_MENU|wx.CAPTION|wx.CLOSE_BOX)
    ex.Show()
    App.MainLoop()

