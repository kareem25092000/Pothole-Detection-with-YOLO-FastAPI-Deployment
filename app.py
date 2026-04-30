from fastapi import FastAPI ,File ,UploadFile
from fastapi.responses import StreamingResponse
from PIL import Image
import io
from predict import predict_nano ,predict_small

app = FastAPI()

@app.post("/predict_small")
async def small(file : UploadFile = File(...)):
    image = Image.open(file.file)
    predicted_image = predict_small(image)
    buffer = io.BytesIO()
    predicted_image.save(buffer ,format="PNG")
    buffer.seek(0)

    return StreamingResponse(buffer ,media_type="image/png")

@app.post("/predict_nano")
async def small(file : UploadFile = File(...)):
    image = Image.open(file.file)
    predicted_image = predict_nano(image)
    buffer = io.BytesIO()
    predicted_image.save(buffer ,format="PNG")
    buffer.seek(0)

    return StreamingResponse(buffer ,media_type="image/png")