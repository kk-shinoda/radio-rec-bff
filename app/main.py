import uvicorn
from fastapi import FastAPI
from routers import rec_api, programs

app = FastAPI()
app.include_router(rec_api.router)
app.include_router(programs.router)

if __name__ == '__main__':
    uvicorn.run(app)
