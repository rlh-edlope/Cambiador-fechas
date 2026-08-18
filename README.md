# Cambiador-fechas
Programa simple para modificar la fecha de estudio de archivo DICOM por medio 
de Python.

## Introducción
Uno de las pruebas de control de calidad en mamografía que se requieren es 
la prueba de Contrast-Detalle. Esta prueba usualmente se realiza por medio de 
un maniquí de Contraste-Detalle como es el CDMAM. 

El análisis de las imágenes usualmente se realiza por medio de softwares
automatizados como el cdcom  [^1]. Adicionalmente a esto se utilizan programas
complementarios como es el caso de CDMAM Analysis  [^2], el cual es un software
de pago que limita su uso en un intervalo de tiempo específico. De esta manera
las versiones antiguas dejan de funcionar y obligan a comprar una nueva versión
y un nuevo maniquí, lo cual es inviable para muchos sitio. 

Una de las formas en las cuales se puede seguir usando el software de análisis 
es modificar el año de los estudios para entrar dentro del margen de la
licencia. De manera que este repositorio busca brindar las herramientas
necesarias para hacer lo de manera fácil y práctica por medio de Python. 

## Requisitos

Python >= 3.9
- pydicom >=3.0.0
- wxpython >= 4.0.0

## Uso *script*
Para usar la herramienta solo es necesario correr el *script* de
python, que se encuentra en la carpeta de `Rutina Base`, se abrirá una ventana
para elegir el/los archivo/s que se van a modificar. Dentro de la rutina el año
que está configurado es 2008, pero se puede modificar al año que se quiera.

Ya que se eligieron lo/s archivo/s se solicitará seleccionar la carpeta donde 
se guardarán todas las imágenes modificadas. Se añadirá un marcador al nombre
del archivo (_mod) para indicar que ha sido modificado. 

La etiqueta DICOM que se modifica es unicamente *StudyDate* (0008,0020).

## Interfaz gráfica GUI
Se ha desarrollado una interfaz gráfica para realizar este proceso para aquellos
que no quieren usar el *script* directamente. 
La interfaz es relativamente fácil de usar. Se puede definir cual es el sufijo
que se quiere utilizar para los nombres de archivo así como se puede seleccionar
la fecha que se quiere utilizar por medio de un calendario. 
Se puede seleccionar la ruta de salida donde se guardarán las imágenes modificadas.
Para iniciar la interfaz gráfica solo se requiere correr el *scrip* de python 
dentro de la carpeta `GUI` y tener instalado wxPython.
Si así lo desea también puede hacer uso de nuestros binarios compilados para correr
o instalar la aplicación directamente, hay versiones tanto para windows como para linux.

La compilación de la aplicación se hizo por medio de CXFrezee y Pyinstaller. 

## Referencias
[^1]: Karssemeijer, N., and M. A. O. Thijssen. "Determination of contrast-detail curves of mammography systems by automated image analysis." Digital mammography 96 (1996): 155-160. [Cdcom](https://euref.org/download/cdcom-version-1-6-and-cdcom-readme-cdmam3-4/)

[^2]: CDMAM Analysis software [CDMAM_Analysis](https://medphys.royalsurrey.nhs.uk/nccpm/tools/cdmam-analysis/)