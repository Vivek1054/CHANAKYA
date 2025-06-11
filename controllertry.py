import eel
import mysql.connector
from mysql.connector import Error

# Connect to MySQL database
def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='jarvis_db',
            user='root',  # Replace with your MySQL username
            password='root'  # Replace with your MySQL password
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print("Error while connecting to MySQL", e)
        return None

# Register new user
@eel.expose
def register(name, email, password):
    connection = get_db_connection()
    if connection is None:
        return {"success": False, "message": "Database connection failed."}
    
    cursor = connection.cursor()
    try:
        # Insert user into the database
        cursor.execute("INSERT INTO users (name, email, password) VALUES (%s, %s, %s)", (name, email, password))
        connection.commit()
        return {"success": True, "message": "Registration successful!"}
    except Error as e:
        return {"success": False, "message": f"Error: {e}"}
    finally:
        cursor.close()
        connection.close()

# User login
@eel.expose
def login(email, password):
    connection = get_db_connection()
    if connection is None:
        return {"success": False, "message": "Database connection failed."}
    
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * FROM users WHERE email = %s AND password = %s", (email, password))
        user = cursor.fetchone()
        
        if user:
            return {"success": True, "message": "Login successful!"}
        else:
            return {"success": False, "message": "Invalid email or password."}
    except Error as e:
        return {"success": False, "message": f"Error: {e}"}
    finally:
        cursor.close()
        connection.close()
