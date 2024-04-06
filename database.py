import sqlite3

conn = sqlite3.connect('UserData.db')

cursor = conn.cursor()

cursor.execute(""" 
CREATE TABLE IF NOT EXISTS Users(
    Id INTEGER NULL NULL PRIMARY KEY AUTOINCREMENT,
    Nane TEXT NOT NULL, 
    Email TEXT NOT NULL, 
    User TEXT NOT NULL, 
    Password TEXT NOT NULL
);
""")

print("Conectado com banco de dados!")

