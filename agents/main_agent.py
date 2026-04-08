# agents/main_agent.py

from agents.task_agent import handle_task
from agents.calendar_agent import handle_calendar
from agents.notes_agent import handle_notes

from services.llm import detect_intent_llm


def handle_user_request(user_input: str):
    """
    Main AI-powered controller using Gemini + fallback logic
    """

    user_input = user_input.lower()

    # ==============================
    # STEP 1: Detect overall intent
    # ==============================
    intent = detect_intent_llm(user_input)

    responses = []

    # ==============================
    # STEP 2: MULTI-STEP WORKFLOW
    # ==============================
    if intent == "multi" or "and" in user_input:
        parts = [p.strip() for p in user_input.split("and")]

        for part in parts:
            sub_intent = detect_intent_llm(part)

            # 🔥 HYBRID DETECTION (LLM + KEYWORD FALLBACK)

            # TASK AGENT
            if "task" in sub_intent or "task" in part:
                responses.append(handle_task(part))

            # CALENDAR AGENT
            elif (
                "calendar" in sub_intent
                or "schedule" in part
                or "meeting" in part
            ):
                responses.append(handle_calendar(part))

            # NOTES AGENT
            elif (
                "notes" in sub_intent
                or "remember" in part
                or "note" in part
                or "save" in part
            ):
                responses.append(handle_notes(part))

            # UNKNOWN
            else:
                responses.append({
                    "message": f"🤖 Could not understand: {part}"
                })

        return {
            "multi_step": True,
            "results": responses
        }

    # ==============================
    # STEP 3: SINGLE INTENT
    # ==============================
    if "task" in intent or "task" in user_input:
        return handle_task(user_input)

    elif (
        "calendar" in intent
        or "schedule" in user_input
        or "meeting" in user_input
    ):
        return handle_calendar(user_input)

    elif (
        "notes" in intent
        or "remember" in user_input
        or "note" in user_input
    ):
        return handle_notes(user_input)

    else:
        return {
            "message": "🤖 I can help with tasks, scheduling, and notes!"
        }