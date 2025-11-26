from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse
import cv2, numpy as np

app = FastAPI()

def read_image_bytes(data: bytes):
    arr = np.frombuffer(data, np.uint8)
    img = cv2.imdecode(arr, cv2.IMREAD_COLOR)
    if img is None:
        return None
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

@app.post("/api/analyze")
async def analyze(mode: str = Form(...), file: UploadFile = File(...)):
    data = await file.read()
    img = read_image_bytes(data)
    if img is None:
        return JSONResponse({"error": "Invalid image"}, status_code=400)

    # Placeholder outputs
    result = {
        "pulse_bpm": 72.0,
        "stress_score": 45.0,
        "respiration_rate": 15.0,
        "hydration_score": 70.0,
        "fatigue_score": 55.0,
        "anemia_indicator": 30.0,
        "jaundice_indicator": 20.0,
        "tremor_score": 10.0,
        "notes": "Demo placeholder output."
    }

    return {"mode": mode, "result": result}
