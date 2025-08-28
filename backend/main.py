from fastapi import FastAPI
from routes import upload, claims
from database import Base, engine


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(upload.router, prefix="/api")
app.include_router(claims.router, prefix="/api")

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or use ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Backend running successfully!"}
