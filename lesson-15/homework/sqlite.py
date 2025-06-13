#1
with sqlite3.connect('database.db') as connection:
    cursor = connection.cursor()
    create = 'CREATE TABLE Roster(Name TEXT, Species TEXT, Age INT);'
    cursor.execute('DROP TABLE IF EXISTS Roster')
    result = cursor.execute(create)
#2
with sqlite3.connect('database.db') as connection:
    cursor = connection.cursor()
    insert = '''
    INSERT INTO Roster VALUES
    ('Benjamin Sisko', 'Human', 40),
    ('Jadzia Dax', 'Trill', 300),
    ('Kira Nerys', 'Bajoran', 29);
    '''
    cursor.execute(insert)
#3
with sqlite3.connect('database.db') as connection:
    cursor = connection.cursor()
    update = '''
    UPDATE Roster
    SET Name = 'Ezri Dax'
    WHERE Name = 'Jadzia Dax';
    '''
    cursor.execute(update)
#4
with sqlite3.connect('database.db') as connnection:
    cursor = connection.cursor()
    select = '''
    SELECT Name, Age
    FROM Roster
    WHERE Species = 'Bajoran';
    '''
    result = cursor.execute(select).fetchall()
print(result)
