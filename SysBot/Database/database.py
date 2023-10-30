import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE_PATH = os.path.join(BASE_DIR, '../database.db')


def data_base():
    with sqlite3.connect(DATABASE_PATH) as db:
        cursor = db.cursor()

        # Alter the table to add new columns
        cursor.execute("PRAGMA table_info(users)")
        existing_columns = [column[1] for column in cursor.fetchall()]
        if 'department' not in existing_columns:
            cursor.execute("ALTER TABLE users ADD COLUMN department VARCHAR(50)")
        if 'problem_category' not in existing_columns:
            cursor.execute("ALTER TABLE users ADD COLUMN problem_category VARCHAR(50)")
        if 'pc_number' not in existing_columns:
            cursor.execute("ALTER TABLE users ADD COLUMN pc_number VARCHAR(50)")

        # Commit the changes
        db.commit()


def save_user_data_to_db(full_name, email, department, problem_category, pc_number):
    with sqlite3.connect("../database.db") as db:
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO users (full_name, email, department, problem_category, pc_number) VALUES (?, ?, ?, ?, ?)",
            (full_name, email, department, problem_category, pc_number))
        db.commit()
