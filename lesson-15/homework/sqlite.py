#1
with sqlite3.connect('database.db') as connection:
    cursor = connection.cursor()
    query = 'CREATE TABLE Roster(Name TEXT, Species TEXT, Age INT);'
    cursor.execute('DROP TABLE IF EXISTS Roster')
    result = cursor.execute(query)
#2
