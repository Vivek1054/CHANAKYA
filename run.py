# import multiprocessing
# import subprocess

# # To run Jarvis
# def startChanakya():
#         # Code for process 1
#         print("Process 1 is running.")
#         from main import start
#         start()

# # To run hotword
# def listenHotword():
#         # Code for process 2
#         print("Process 2 is running.")
#         from engine.features import hotword
#         hotword()


#     # Start both processes
# if __name__ == '__main__':
#         p1 = multiprocessing.Process(target=startChanakya)
#         p2 = multiprocessing.Process(target=listenHotword)
        
#         p1.start()
#         p2.start()
#         p1.join()

#         if p2.is_alive():
#             p2.terminate()
#             p2.join()

#         print("system stop")






# import multiprocessing
# import subprocess
# from database import connect_db

# # To run Jarvis
# def startChanakya():
#     print("Process 1 is running.")
#     from main import start
#     start()

# # To run hotword
# def listenHotword():
#     print("Process 2 is running.")
#     from engine.features import hotword
#     hotword()

# if __name__ == '__main__':
#     # Step 1: Connect and initialize database
#     print("Initializing database...")
#     connect_db()
#     print("Database ready.")

#     # Step 2: Start both processes
#     p1 = multiprocessing.Process(target=startChanakya)
#     p2 = multiprocessing.Process(target=listenHotword)

#     p1.start()
#     p2.start()

#     p1.join()

#     if p2.is_alive():
#         p2.terminate()
#         p2.join()

#     print("System stopped.")













# import eel
# import mysql.connector



# import multiprocessing
# import subprocess


# # To run Jarvis
# def startChanakya():
#     print("Process 1 is running.")
#     from main import start
#     start()

# # To run hotword
# def listenHotword():
#     print("Process 2 is running.")
#     from engine.features import hotword
#     hotword()

# if __name__ == '__main__':


        
#     # MySQL Database connection
#     def get_db_connection():
#         conn = mysql.connector.connect(
#             host="localhost",  # Host of your MySQL server
#             user="root",       # Your MySQL username
#             password="root",  # Your MySQL password
#             database="jarvis_db"  # Name of your database
#         )
#         return conn

#     # Login function
#     @eel.expose
#     def login(username, password):
#         conn = get_db_connection()
#         cursor = conn.cursor(dictionary=True)

#         cursor.execute("SELECT * FROM users WHERE email = %s", (username,))
#         user = cursor.fetchone()
#         conn.close()

#         if user and user['password'] == password:
#             return {"success": True}
#         else:
#             return {"success": False, "message": "Invalid username or password"}

#     # Register function
#     @eel.expose
#     def register(name, email, password):
#         conn = get_db_connection()
#         cursor = conn.cursor()

#         # Check if user already exists
#         cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
#         existing_user = cursor.fetchone()

#         if existing_user:
#             conn.close()
#             return {"success": False, "message": "User already exists"}

#         # Insert new user
#         cursor.execute("INSERT INTO users (name, email, password) VALUES (%s, %s, %s)", (name, email, password))
#         conn.commit()
#         conn.close()
#         return {"success": True}

#     # Start Eel app
#     def start_app():
#         eel.start('login.html', size=(800, 600))  # Set window size and start login page

    
    
#     ################
    
#     # Step 2: Start both processes
#     p1 = multiprocessing.Process(target=startChanakya)
#     p2 = multiprocessing.Process(target=listenHotword)

#     p1.start()
#     p2.start()

#     p1.join()J
#     if p2.is_alive():
#         p2.terminate()
#         p2.join()

#     print("System stopped.")



import eel
import mysql.connector
import os
import multiprocessing
import subprocess
import eel

from engine.features import *

from engine.command import *





# Initialize Eel app
eel.init('www')  # 'web' folder contains HTML, CSS, and JS files






def startJarvis():
        # Code for process 1
        print("Process 1 is running.")
        from main import start
        start()

# To run hotword
def listenHotword():
        # Code for process 2
        print("Process 2 is running.")
        from engine.features import hotword
        hotword()




# MySQL Database connection
def get_db_connection():
    conn = mysql.connector.connect(
        host="localhost",  # Host of your MySQL server
        user="root",       # Your MySQL username
        password="root",  # Your MySQL password
        database="jarvis_db"  # Name of your database
    )
    return conn

# Login function    
@eel.expose
def login(username, password):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM users WHERE email = %s", (username,))
    user = cursor.fetchone()
    conn.close()

    if user and user['password'] == password:
        return {"success": True}
    else:
        return {"success": False, "message": "Invalid username or password"}

# Register function
@eel.expose
def register(name, email, password):
    conn = get_db_connection()
    cursor = conn.cursor()

    # Check if user already exists
    cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
    existing_user = cursor.fetchone()

    if existing_user:
        conn.close()
        return {"success": False, "message": "User already exists"}

    # Insert new user
    cursor.execute("INSERT INTO users (name, email, password) VALUES (%s, %s, %s)", (name, email, password))
    conn.commit()
    conn.close()
    return {"success": True}

# Start Eel app
# def start_app():
#     eel.init("www")

#     PlayAssistantSound()
#     eel.start('home.html', size=(800, 600))  # Set window size and start login page

if __name__ == "__main__":
    # start_app()
    
    #############
    
    p1 = multiprocessing.Process(target=startJarvis)
    p2 = multiprocessing.Process(target=listenHotword)
    
    p1.start()
    p2.start()
    p1.join()

    if p2.is_alive():
        p2.terminate()
        p2.join()

    print("system stop")

