# agents/calendar_agent.py

from tools.calendar_tool import add_event, list_events


def handle_calendar(user_input: str):
    user_input = user_input.lower()

    # ==============================
    # ADD EVENT
    # ==============================
    if "schedule" in user_input or "add meeting" in user_input:
        event_text = extract_event(user_input)
        event_time = extract_time(user_input)

        if not event_text:
            return {"calendar": "⚠️ Could not understand event"}

        return {
            "action": "add_event",
            "message": add_event(event_text, event_time)
        }

    # ==============================
    # LIST EVENTS
    # ==============================
    elif "show" in user_input or "list" in user_input:
        return {
            "action": "list_events",
            "events": list_events()
        }

    else:
        return {
            "message": "🤖 Calendar agent can schedule and show events."
        }


def extract_event(user_input: str):
    keywords = ["schedule", "add", "meeting", "event"]

    words = user_input.split()
    filtered_words = [w for w in words if w not in keywords]

    event_text = " ".join(filtered_words).strip()

    return event_text if event_text else None


def extract_time(user_input: str):
    if "tomorrow" in user_input:
        return "tomorrow"
    elif "today" in user_input:
        return "today"
    elif "morning" in user_input:
        return "morning"
    elif "evening" in user_input:
        return "evening"
    else:
        return "unspecified"