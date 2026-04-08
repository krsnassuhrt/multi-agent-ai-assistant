# db/db.py

import psycopg2
import os


# ==============================
# DATABASE CONNECTION
# ==============================
def get_connection():
    return psycopg2.connect(os.getenv("DATABASE_URL"))


# ==============================
# EXECUTE QUERY (INSERT / UPDATE / DELETE)
# ==============================
def execute_query(query, params=None):
    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute(query, params)
        conn.commit()
        return {"status": "success"}

    except Exception as e:
        conn.rollback()
        return {"status": "error", "message": str(e)}

    finally:
        cur.close()
        conn.close()


# ==============================
# FETCH DATA (SELECT)
# ==============================
def fetch_query(query, params=None):
    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute(query, params)
        rows = cur.fetchall()

        colnames = [desc[0] for desc in cur.description]

        result = [dict(zip(colnames, row)) for row in rows]

        return result

    except Exception as e:
        return {"status": "error", "message": str(e)}

    finally:
        cur.close()
        conn.close()