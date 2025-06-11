import csv
import sqlite3

con = sqlite3.connect("chanakya.db")
cursor = con.cursor()

query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name varchar(100), path varchar(1000))"
cursor.execute(query)

# query = "INSERT INTO sys_command VALUES (null,'one note','C:\\Program Files\\Microsoft Office\\root\\Office16\\ONENOTE.exe')"
# cursor.execute(query)
# conn.commit()

query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name varchar(100), path varchar(1000))"
cursor.execute(query)

# query = "INSERT INTO web_command VALUES (null,'youtube','https://www.youtube.com/')"
# cursor.execute(query)
# conn.commit()

cursor.execute('''CREATE TABLE IF NOT EXISTS dkcontacts1 (id integer primary key, name VARCHAR(200), mobile_no VARCHAR(255), email VARCHAR(255) NULL)''')

desired_columns_indices = [0, 1]

# # Read data from CSV and insert into SQLite table for the desired columns
# with open('dkcontacts1.csv', 'r', encoding='utf-8') as csvfile:
#     csvreader = csv.reader(csvfile)
#     for row in csvreader:
#         selected_data = [row[i] for i in desired_columns_indices]
#         cursor.execute(''' INSERT INTO dkcontacts1 (id, 'name', 'mobile_no') VALUES (null, ?, ?);''', tuple(selected_data))

# # # Commit changes and close connection
# con.commit()
# con.close()

# query = 'Sam'
# query = query.strip().lower()

# cursor.execute("SELECT mobile_no FROM dkcontacts1 WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
# results = cursor.fetchall()
# print(results[0][0])