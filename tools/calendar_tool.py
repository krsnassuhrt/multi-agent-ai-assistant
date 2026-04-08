# tools/calendar_tool.py

from db.db import execute_query, fetch_query


def add_event(event_text, event_time):
    query = "INSERT INTO events (event, event_time) VALUES (%s, %s)"
    execute_query(query, (event_text, event_time))
    return f"📅 Event scheduled: {event_text} ({event_time})"


def list_events():
    query = "SELECT * FROM events ORDER BY id DESC"
    return fetch_query(query)