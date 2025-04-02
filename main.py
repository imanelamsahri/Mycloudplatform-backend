from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Bienvenue sur l'API Mycloudplatform 🎉"}

@app.get("/analyser")
def analyser(produit: Optional[str] = "pomme", rayon: Optional[float] = 10):
    return {
        "produit": produit,
        "rayon": rayon,
        "geojson": {
            "type": "FeatureCollection",
            "features": []
        }
    }
