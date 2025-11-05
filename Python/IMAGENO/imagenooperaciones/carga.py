import pydicom
import numpy as np
import os

def cargar_imagen_dicom(ruta):
    """Carga una imagen DICOM y la convierte a uint8."""
    ds = pydicom.dcmread(ruta)
    im = ds.pixel_array.astype(np.uint8)
    return im

def listar_dicoms(carpeta):
    """
    Lista todos los archivos .dcm de la carpeta y subcarpetas.
    Devuelve una lista de rutas completas.
    """
    dicoms = []
    for root, _, files in os.walk(carpeta):
        for f in files:
            if f.lower().endswith(".dcm"):
                dicoms.append(os.path.join(root, f))
    return dicoms

