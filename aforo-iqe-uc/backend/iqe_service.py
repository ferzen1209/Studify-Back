import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    raise RuntimeError("Falta GOOGLE_API_KEY en el archivo .env")

# Configurar cliente de Gemini
genai.configure(api_key=API_KEY)

# Puedes cambiar el modelo según lo que pida la hackathon
MODEL_NAME = "gemini-1.5-pro"

PROMPT_IQE = """
Eres un modelo que analiza salas de estudio universitarias.
Debes evaluar qué tan bueno es el ambiente para estudiar.

Devuelve SIEMPRE un JSON válido con este formato EXACTO:

{
  "iqe": <número entre 0 y 100>,
  "ruido_esperado": <0-100>,
  "orden": <0-100>,
  "hacinamiento": <0-100>,
  "comodidad_visual": <0-100>,
  "descripcion_corta": "<máx 15 palabras>"
}

Definiciones:
- iqe: calidad global del ambiente para estudiar en silencio.
- ruido_esperado: más alto = más ruido/conversación.
- orden: más alto = más ordenado y organizado.
- hacinamiento: más alto = más apretado/lleno.
- comodidad_visual: iluminación y sensación de espacio.

No expliques nada, NO agregues texto fuera del JSON.
"""

def compute_iqe(image_bytes: bytes) -> dict:
    """
    Llama a Gemini con la imagen y devuelve un dict con el IQE y los indicadores.
    Si algo falla, devuelve valores por defecto.
    """
    model = genai.GenerativeModel(MODEL_NAME)

    image = {
        "mime_type": "image/jpeg",  # si usas PNG puedes ajustar esto
        "data": image_bytes,
    }

    try:
        response = model.generate_content(
            [PROMPT_IQE, image]
        )
        raw_text = response.text.strip()
        data = json.loads(raw_text)
    except Exception as e:
        # Para debug, puedes imprimir el error si quieres
        print("Error llamando a Gemini o parseando JSON:", e)
        data = {
            "iqe": 50,
            "ruido_esperado": 50,
            "orden": 50,
            "hacinamiento": 50,
            "comodidad_visual": 50,
            "descripcion_corta": "No se pudo analizar correctamente la imagen."
        }

    # Aseguramos que tenga todos los campos
    data.setdefault("iqe", 50)
    data.setdefault("ruido_esperado", 50)
    data.setdefault("orden", 50)
    data.setdefault("hacinamiento", 50)
    data.setdefault("comodidad_visual", 50)
    data.setdefault("descripcion_corta", "")

    return data
