import sqlite3

con = sqlite3.connect("jarvis.db")
cursor = con.cursor()


# query = "INSERT INTO sys_command VALUES (null,'WINWORD','C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.exe')"
# cursor.execute(query)
# con.commit()

# query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES (null,'canva','https://www.canva.com/')"
# cursor.execute(query)
# con.commit()


# query = "INSERT INTO sys_command VALUES (null,'code','C:\\Users\\DELL\\AppData\\Local\\Programs\\Microsoft VS Code\\CODE.exe')"
# cursor.execute(query)
# con.commit()


app_name = "code"
cursor.execute('SELECT path FROM sys_command WHERE name In (?)', (app_name,))
results = cursor.fetchall()
print(results[0][0])