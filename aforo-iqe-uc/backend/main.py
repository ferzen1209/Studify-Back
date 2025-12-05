from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
from iqe_service import compute_iqe

app = FastAPI(
    title="Aforo UC - IQE API",
    description="API que recibe imágenes de salas y calcula un índice de calidad de estudio (IQE) usando Gemini.",
    version="0.1.0",
)

# CORS abierto para poder probar fácilmente desde cualquier frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # en producción conviene restringir
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Estado en memoria simple: room_id -> dict con estado
ROOM_STATUS = {}  # Esto en el futuro podría ser una BD

@app.get("/rooms/status")
def get_rooms_status():
    """
    Devuelve el estado actual de todas las salas registradas.
    Para la demo, guardamos todo en memoria en ROOM_STATUS.
    """
    # Devolvemos los valores como lista
    return list(ROOM_STATUS.values())

@app.post("/rooms/{room_id}/frame")
async def upload_frame(room_id: str, file: UploadFile = File(...)):
    """
    Endpoint que recibe una imagen (frame) de una sala de estudio,
    llama a Gemini para obtener el IQE y actualiza el estado de la sala.
    """
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="El archivo debe ser una imagen.")

    # Leer bytes de la imagen
    image_bytes = await file.read()

    # Llamar a Gemini para obtener IQE
    iqe_data = compute_iqe(image_bytes)

    # Por ahora, el aforo lo simulamos (random).
    # En una versión futura, esto vendría de un contador real de personas.
    import random
    aforo = random.randint(5, 50)
    capacidad = 60

    # Actualizar estado de la sala en memoria
    ROOM_STATUS[room_id] = {
        "room_id": room_id,
        "aforo": aforo,
        "capacidad": capacidad,
        "iqe": iqe_data["iqe"],
        "ruido_esperado": iqe_data["ruido_esperado"],
        "orden": iqe_data["orden"],
        "hacinamiento": iqe_data["hacinamiento"],
        "comodidad_visual": iqe_data["comodidad_visual"],
        "descripcion_corta": iqe_data["descripcion_corta"],
        "ultimo_update": datetime.utcnow().isoformat() + "Z",
    }

    return {
        "ok": True,
        "room_id": room_id,
        "iqe": iqe_data,
    }
