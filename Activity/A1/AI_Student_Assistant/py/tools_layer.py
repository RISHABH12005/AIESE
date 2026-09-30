import sqlite3
from pathlib import Path


# =========================================================
# Database Path
# =========================================================

database_directory = (
    Path(__file__).resolve().parent.parent / "db"
)

database_directory.mkdir(
    parents=True,
    exist_ok=True
)

database_file = database_directory / "student.db"


# =========================================================
# Database Setup
# =========================================================

def get_connection():

    return sqlite3.connect(database_file)


def initialize_database():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS registrations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_name TEXT NOT NULL,
            course_name TEXT NOT NULL
        )
    """)

    conn.commit()

    conn.close()


# Create the table when the application starts

initialize_database()


# =========================================================
# Tools Layer
# =========================================================

def register_course(student_name, course_name):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO registrations (student_name, course_name)
        VALUES (?, ?)
        """,
        (student_name, course_name)
    )

    conn.commit()

    conn.close()

    return (
        f"{course_name} has been successfully "
        f"registered for {student_name}."
    )


# =========================================================
# Verify Tool Action
# =========================================================

def get_registrations():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM registrations"
    )

    registrations = cursor.fetchall()

    conn.close()

    return registrations