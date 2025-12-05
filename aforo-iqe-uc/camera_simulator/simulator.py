import time
import random
import requests
import os

# URL base del backend (donde está corriendo FastAPI)
BACKEND_URL_BASE = "http://localhost:8000"

# ID de la sala que queremos simular
ROOM_ID = "SJ_BIB_101"

# Carpeta donde están las imágenes de ejemplo
IMAGES_DIR = "images"

# Cada cuántos segundos enviamos una imagen
INTERVALO_SEGUNDOS = 30


def elegir_imagen_aleatoria():
    """Elige una imagen aleatoria de la carpeta images/."""
    archivos = [
        f for f in os.listdir(IMAGES_DIR)
        if f.lower().endswith((".jpg", ".jpeg", ".png"))
    ]
    if not archivos:
        raise RuntimeError(
            f"No hay imágenes en la carpeta {IMAGES_DIR}. "
            "Agrega al menos un .jpg o .png."
        )
    nombre = random.choice(archivos)
    ruta = os.path.join(IMAGES_DIR, nombre)
    return ruta


def enviar_imagen(ruta_imagen: str):
    """Envía la imagen al backend en el endpoint /rooms/{ROOM_ID}/frame."""
    url = f"{BACKEND_URL_BASE}/rooms/{ROOM_ID}/frame"

    with open(ruta_imagen, "rb") as f:
        files = {"file": (os.path.basename(ruta_imagen), f, "image/jpeg")}
        try:
            resp = requests.post(url, files=files, timeout=15)
            print(f"[{ROOM_ID}] Enviada {ruta_imagen} -> status {resp.status_code}")
            if resp.status_code != 200:
                print("Respuesta del backend:", resp.text)
        except Exception as e:
            print(f"Error enviando imagen: {e}")


def loop_envio():
    """Bucle principal: envía una imagen aleatoria cada INTERVALO_SEGUNDOS."""
    print(f"Iniciando simulador de cámara para sala {ROOM_ID}...")
    print(f"Usando imágenes desde: {IMAGES_DIR}/")
    while True:
        ruta = elegir_imagen_aleatoria()
        enviar_imagen(ruta)
        time.sleep(INTERVALO_SEGUNDOS)


if __name__ == "__main__":
    loop_envio()
