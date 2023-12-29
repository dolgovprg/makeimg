from fastapi import FastAPI
import uvicorn

app = FastAPI()



@app.get('/')
async def get():
    return {"message": "Get Hello World"}

@app.post('/')
async def post():
    return {"message": "Post Hello World"}

if __name__ == '__main__':
    uvicorn.run('main:app',reload=True,workers=1)