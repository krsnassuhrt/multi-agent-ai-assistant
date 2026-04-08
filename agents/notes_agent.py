# agents/notes_agent.py

from tools.notes_tool import add_note, list_notes, search_notes


def handle_notes(user_input: str):
    user_input = user_input.lower().strip()

    # ==============================
    # ADD NOTE (STRONG DETECTION)
    # ==============================
    if any(word in user_input for word in ["remember", "note", "save"]):
        note_text = extract_note(user_input)

        if not note_text:
            return {"action": "add_note", "message": "⚠️ Could not extract note"}

        return {
            "action": "add_note",
            "message": add_note(note_text)
        }

    # ==============================
    # LIST NOTES
    # ==============================
    if any(word in user_input for word in ["show notes", "list notes", "my notes"]):
        return {
            "action": "list_notes",
            "notes": list_notes()
        }

    # ==============================
    # SEARCH NOTES
    # ==============================
    if any(word in user_input for word in ["find", "search"]):
        keyword = extract_keyword(user_input)

        if not keyword:
            return {"action": "search_notes", "message": "⚠️ No keyword provided"}

        return {
            "action": "search_notes",
            "results": search_notes(keyword)
        }

    # ==============================
    # DEFAULT (SMART FALLBACK)
    # ==============================
    return {
        "action": "unknown",
        "message": "⚠️ Could not understand note request"
    }


# ==============================
# EXTRACT NOTE TEXT
# ==============================
def extract_note(user_input: str):
    keywords = ["remember", "note", "save"]

    words = user_input.split()
    filtered_words = [w for w in words if w not in keywords]

    note_text = " ".join(filtered_words).strip()

    return note_text if note_text else None


# ==============================
# EXTRACT SEARCH KEYWORD
# ==============================
def extract_keyword(user_input: str):
    keywords = ["find", "search"]

    words = user_input.split()
    filtered_words = [w for w in words if w not in keywords]

    keyword = " ".join(filtered_words).strip()

    return keyword if keyword else None