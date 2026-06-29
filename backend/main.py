from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(
    title="Signalement Citoyen API",
    version="1.0.0"
)

# Configuration CORS : Permet au Frontend (JS) de faire des requêtes à l'API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En développement, on autorise toutes les origines (ex: Live Server)
    allow_credentials=True,
    allow_methods=["*"],  # Autorise GET, POST, PUT, DELETE
    allow_headers=["*"],
)

# Modèle de données pour tester un signalement
class Signalement(BaseModel):
    titre: str
    description: str

@app.get("/")
def home():
    return {"message": "API Signalement Citoyen en ligne"}

@app.post("/api/signalements")
def creer_signalement(data: Signalement):
    # C'est ici que tu ajouteras SQLAlchemy plus tard pour sauvegarder dans PostgreSQL
    return {"status": "success", "recu": data}