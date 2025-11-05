from scipy import ndimage as ndi
import numpy as np

def filtro_media(im):
    """Aplica un filtro de media 3x3 sobre la imagen."""
    weights = np.full((3,3), 0.11)
    return ndi.convolve(im, weights)
