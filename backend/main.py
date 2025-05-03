from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from . import models, database, crud

models.Base.metadata.create_all(bind=database.engine)


app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Notes app!"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/register")
async def register(request: Request):
    data = await request.json()
    user = crud.get_or_create_user(data["username"])
    return {"message": "User registered", "user_id": user.id}

@app.post("/add_note")
async def add_note(request: Request):
    data = await request.json()
    note = crud.add_note(data["username"], data["title"], data["content"])
    return {"message": "Note added", "note": {"id": note.id, "title": note.title, "content": note.content}}

@app.get("/notes/{username}")
async def get_user_notes(username: str):
    notes = crud.get_notes(username)
    return [{"id": n.id, "title": n.title, "content": n.content} for n in notes]

@app.delete("/note/{note_id}")
async def delete(note_id: int):
    crud.delete_note(note_id)
    return {"message": "Note deleted"}

