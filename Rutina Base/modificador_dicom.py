"""
Programa para la modificación de una cabecera DICOM para seguir usando el CDMAM
Analysis V1.5.5.

V1.0 del 10/08/26 - Se crea la rutina básica

"""

import pydicom
import tkinter as tk
from tkinter import filedialog

#---------------------------------abrir---------------------------------------------
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilenames(filetypes=[("Imagen", "*.dcm")])
save_path = filedialog.askdirectory()

for i in file_path:
    imagen = pydicom.dcmread(i)


#------------------------------modificar--------------------------------------------
    fecha_or = imagen.StudyDate
    fecha_new = '2008'+fecha_or[4:]
    imagen.StudyDate = fecha_new


    name = i.split('/')

    print(save_path)
  

#------------------------------ salvar----------------------------------------------
    pydicom.dcmwrite(save_path+'/'+name[-1][:-4]+'_mod.dcm', imagen)

root.destroy()