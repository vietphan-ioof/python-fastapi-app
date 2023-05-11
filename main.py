from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI(title="Hello FastAPI from AWS ECS")
origins = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
) 

@app.get("/")
async def index():
    return {"Hello": "World"}

@app.get("/ping")
async def ping():
    return {"status": "pong"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str=None):
    return {"item_id": item_id, "q": q}

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)