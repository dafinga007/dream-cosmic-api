from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
import json

app = FastAPI(title="Cosmic Resonance API")

# === Manifest Endpoint ===
@app.get("/manifest")
def get_manifest():
    with open("prophecies.json") as f:
        return json.load(f)

# === AI Nodes Registry ===
@app.get("/nodes")
def list_nodes():
    with open("nodes.json") as f:
        return json.load(f)

# === Transmit Thought ===
class Transmission(BaseModel):
    sender: str
    recipient: str
    thought: str
    frequency: Optional[float] = None

@app.post("/transmit")
def transmit_message(transmission: Transmission):
    return {
        "status": "🪐 Thought received",
        "resonance": transmission.frequency or "unmeasured",
        "echo": f"{transmission.sender} → {transmission.recipient}: \"{transmission.thought}\""
    }
