# tools/task_tool.py

from db.db import execute_query, fetch_query


def add_task(task_text):
    query = "INSERT INTO tasks (task) VALUES (%s)"
    execute_query(query, (task_text,))
    return f"✅ Task added: {task_text}"


def list_tasks():
    query = "SELECT * FROM tasks ORDER BY id DESC"
    return fetch_query(query)


def complete_last_task():
    query = """
    UPDATE tasks
    SET status = 'completed'
    WHERE id = (SELECT id FROM tasks ORDER BY id DESC LIMIT 1)
    """
    execute_query(query)
    return "✅ Last task marked as completed"