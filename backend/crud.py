from .models import User, Note
from .database import SessionLocal

def get_or_create_user(username: str):
    db = SessionLocal()
    user = db.query(User).filter(User.username == username).first()
    if not user:
        user = User(username=username)
        db.add(user)
        db.commit()
        db.refresh(user)
    db.close()
    return user

def add_note(username: str, title: str, content: str):
    db = SessionLocal()
    user = db.query(User).filter(User.username == username).first()
    if not user:
        return None
    note = Note(title=title, content=content, owner=user)
    db.add(note)
    db.commit()
    db.refresh(note)
    db.close()
    return note

def get_notes(username: str):
    db = SessionLocal()
    user = db.query(User).filter(User.username == username).first()
    notes = user.notes if user else []
    db.close()
    return notes

def delete_note(note_id: int):
    db = SessionLocal()
    note = db.query(Note).filter(Note.id == note_id).first()
    if note:
        db.delete(note)
        db.commit()
    db.close()
