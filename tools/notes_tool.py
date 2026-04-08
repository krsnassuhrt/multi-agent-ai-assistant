# tools/notes_tool.py

from db.db import execute_query, fetch_query


def add_note(note_text):
    query = "INSERT INTO notes (note) VALUES (%s)"
    execute_query(query, (note_text,))
    return f"📝 Note saved: {note_text}"


def list_notes():
    query = "SELECT * FROM notes ORDER BY id DESC"
    return fetch_query(query)


def search_notes(keyword):
    query = "SELECT * FROM notes WHERE note ILIKE %s"
    return fetch_query(query, (f"%{keyword}%",))