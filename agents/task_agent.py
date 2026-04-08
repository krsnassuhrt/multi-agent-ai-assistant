# agents/task_agent.py

from tools.task_tool import add_task, list_tasks, complete_last_task


def handle_task(user_input: str):
    user_input = user_input.lower()

    # ==============================
    # ADD TASK
    # ==============================
    if "add" in user_input or "create" in user_input:
        task_text = extract_task(user_input)

        if not task_text:
            return {"task": "⚠️ Could not understand task"}

        return {
            "action": "add_task",
            "message": add_task(task_text)
        }

    # ==============================
    # LIST TASKS
    # ==============================
    elif "list" in user_input or "show" in user_input:
        return {
            "action": "list_tasks",
            "tasks": list_tasks()
        }

    # ==============================
    # COMPLETE TASK
    # ==============================
    elif "complete" in user_input:
        return {
            "action": "complete_task",
            "message": complete_last_task()
        }

    else:
        return {
            "message": "🤖 Task agent can add, list, or complete tasks."
        }


def extract_task(user_input: str):
    keywords = ["add", "create", "task", "todo"]

    words = user_input.split()
    filtered_words = [word for word in words if word not in keywords]

    task_text = " ".join(filtered_words).strip()

    return task_text if task_text else None