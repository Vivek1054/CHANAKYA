import sqlite3

import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Step 1: Create the table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
)
""")

# Step 2: Insert a user
# try:
#     cursor.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", (name, email, password))
#     conn.commit()
#     return{"success": True, "message": "Registration successful!"}
# except sqlite3.IntegrityError:
#     print("User already exists.")

# Step 3: Commit changes and close the connection
# conn.commit()
# conn.close()


def connect_db():
    return sqlite3.connect('users.db')
    

def register_user(name, email, password):
    try:
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (name, email, password) VALUES (?, ?, ?)', (name, email, password))
        conn.commit()
        conn.close()
        return { "success": True }
    except sqlite3.IntegrityError:
        return { "success": False, "message": "Email already registered." }

def check_login(email, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE email = ? AND password = ?', (email, password))
    user = cursor.fetchone()
    conn.close()
    if user:
        return { "success": True }
    else:
        return { "success": False, "message": "Invalid email or password." }
    

