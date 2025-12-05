# 🧠 Aforo IQE UC  
### Optimización del bienestar estudiantil mediante análisis inteligente de salas de estudio

Este proyecto fue desarrollado para una hackathon UC con el objetivo de mejorar el bienestar estudiantil, la salud mental y la logística universitaria mediante la evaluación inteligente de salas de estudio.

Durante los periodos de alta carga académica, las salas más conocidas se saturan, mientras que otras permanecen subutilizadas. Nuestro sistema utiliza visión computacional y la API de Gemini para analizar imágenes en tiempo real, estimar aforo y calcular un Índice de Calidad de Estudio (IQE).

---

## 📌 Características principales

- Recepción de imágenes desde cámaras instaladas en salas.
- Análisis multimodal mediante Google Gemini 1.5 Pro.
- Cálculo de métricas del ambiente:
  - IQE (Índice de Calidad de Estudio)
  - Ruido esperado
  - Nivel de orden
  - Hacinamiento
  - Comodidad visual
- API REST para consultar el estado de las salas.
- Simulador de cámara para pruebas sin hardware real.

---

## 📁 Arquitectura del proyecto

aforo-iqe-uc/
├─ backend/
│ ├─ main.py
│ ├─ iqe_service.py
│ ├─ requirements.txt
│ └─ .env.example
│
├─ camera_simulator/
│ ├─ simulator.py
│ └─ images/
│ ├─ sala_tranquila.jpg
│ ├─ sala_llena.jpg
│ └─ sala_caotica.jpg
│
└─ README.md

## 🤖 ¿Cómo calcula IQE el sistema?

1. El backend recibe una imagen.
2. La envía a Gemini con un prompt especializado.
3. Gemini devuelve un JSON con:
   - **IQE**
   - **Ruido esperado**
   - **Orden**
   - **Hacinamiento**
   - **Comodidad visual**
4. La información se guarda en memoria para consulta.

---

## 🎯 Objetivo del proyecto

- Reducir estrés estudiantil.
- Evitar aglomeraciones en salas de estudio.
- Mejorar la distribución de estudiantes en horarios punta.
- Facilitar la búsqueda de espacios tranquilos para estudiar.
- Aprovechar mejor la infraestructura universitaria.
