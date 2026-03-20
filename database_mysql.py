import os
import mysql.connector
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_NAME = os.getenv("DB_NAME", "marketing_agent")

def get_connection():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

def save_plan(goal, plan):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO plans (goal, plan, created_at)
    VALUES (%s, %s, %s)
    """

    cursor.execute(query, (goal, plan, datetime.now()))
    conn.commit()

    cursor.close()
    conn.close()

def load_plans():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT id, goal, plan, created_at
        FROM plans
        ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return rows

def delete_plan(plan_id):
    conn = get_connection()
    cursor = conn.cursor()

    query = "DELETE FROM plans WHERE id = %s"
    cursor.execute(query, (plan_id,))

    conn.commit()
    cursor.close()
    conn.close()

def clear_history():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM plans")

    conn.commit()
    cursor.close()
    conn.close()