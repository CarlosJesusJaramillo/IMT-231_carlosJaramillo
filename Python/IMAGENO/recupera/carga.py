import pydicom
import numpy as np

def cargar_imagen_dicom(ruta):
    ds = pydicom.dcmread(ruta)
    im = ds.pixel_array.astype(np.float32)
    im = 255 * (im - im.min()) / (im.max() - im.min())
    im = im.astype(np.uint8)
    meta = {
        "Paciente": getattr(ds, "PatientName", "Desconocido"),
        "Modalidad": getattr(ds, "Modality", "Desconocido"),
        "Tamaño": im.shape
    }
    return im, meta
