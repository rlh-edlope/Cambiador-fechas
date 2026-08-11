# Cambiador-fechas
Programa simple para modificar la fecha de estudio de archivo DICOM por medio 
de Python. 

## Introducción
Uno de las pruebas de control de calidad en mamografía que se requieren es 
la prueba de Contrast-Detalle. Esta prueba usualmente se realiza por medio de 
un maniquí de Contraste-Detalle como es el CDMAM. 

El análisis de las imágenes usualmente se realiza por medio de softwares
automatizados como el cdcom [^1]. Adicionalmente a esto se utilizan programas
complementarios como es el caso de CDMAM Analysis [^2], el cual es un software
de pago que limita su uso en un intervalo de tiempo específico. De esta manera
las versiones antiguas dejan de funcionar y obligan a comprar una nueva versión
y un nuevo maniquí, lo cual es inviable para muchos sitio. 

Una de las formas en las cuales se puede seguir usando el software de análisis 
es modificar el año de los estudios para entrar dentro del margen de la
licencia. De manera que este repositorio busca brindar las herramientas
necesarias para hacer lo demanera fácil y práctica por medio de Python. 

## Requisitos

Python >= 3.9
- pydicom >=3.0.0

## Uso
Para usar la herramienta actualmente solo es necesario correr el *script* de
python, que se encuentra en la carpeta de `Rutina Base`, se abrirá una ventana
para elegir el/los archivo/s que se van a modificar. Dentro de la rutina el año
que está configurado es 2008, pero se puede modificar al año que se quiera. 