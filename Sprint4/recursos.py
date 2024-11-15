import requests
from PIL import Image, ImageTk
import io


def descargar_imagen(url, size):
    """
    Descarga una imagen desde una URL, la redimensiona al tamaño especificado y la convierte
    en un formato compatible con Tkinter.

    Parámetros:
        url (str): URL de la imagen a descargar.
        size (tuple): Tamaño al que se redimensionará la imagen, en píxeles (ancho, alto).

    Retorna:
        ImageTk.PhotoImage: La imagen redimensionada en un formato compatible con Tkinter, o None en caso de error.
    """
    try:
        # Solicitar la imagen desde la URL
        response = requests.get(url)
        response.raise_for_status()  # Verifica que la solicitud fue exitosa

        # Cargar la imagen en memoria y redimensionarla
        imagen = Image.open(io.BytesIO(response.content))
        imagen = imagen.resize(size, Image.LANCZOS)

        # Convertir la imagen a un formato compatible con Tkinter
        imagen_tk = ImageTk.PhotoImage(imagen)
        return imagen_tk

    except requests.RequestException as e:
        print(f"Error al descargar la imagen desde {url}: {e}")
        return None
