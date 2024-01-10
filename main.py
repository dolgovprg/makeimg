import base64
from fastapi import FastAPI, UploadFile, File
from PIL import Image
from io import BytesIO
from starlette.middleware.cors import CORSMiddleware
from config import settings
from resizeimage import resizeimage
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.ALLOW_ORIGINS],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/img")
async def convert_image(file: UploadFile = File(...)):

    with Image.open(file.file) as image:
        img_buffer = BytesIO()
        cover = resizeimage.resize_cover(image, [640, 480])
        cover.save(img_buffer, image.format)
        img_buffer.seek(0)
        img_byte = img_buffer.read()
        img_base64 = base64.b64encode(img_byte)

    
    return {"image_base64": img_base64}


if __name__ == '__main__':
    uvicorn.run('main:app',reload=True,workers=1)
