import sqlite3
# 1
# connecting to the database(creating if doesn't exist) using context manager for it to automatically commit changes and close the connection when done
with sqlite3.connect('database.db') as connection:
    cursor = connection.cursor()  # defining a cursor
    cursor.execute('DROP TABLE IF EXISTS Roster')
    # assgning a query to create a table to a variable
    create = 'CREATE TABLE Roster(Name TEXT, Species TEXT, Age INT);'
    # executing a query that drop the table 'Roster' if it exists
    cursor.execute('DROP TABLE IF EXISTS Roster')
    result = cursor.execute(create)  # Executing our create query
# 2

    values = [
        ('Benjamin Sisko', 'Human', 40),
        ('Jadzia Dax', 'Trill', 300),
        ('Kira Nerys', 'Bajoran', 29)
    ]  # Values to be inserted

    # insert command using placeholders to insert multiple values
    cursor.executemany("INSERT INTO Roster VALUES(?,?,?)", values)
# 3

    update = '''
    UPDATE Roster
    SET Name = 'Ezri Dax'
    WHERE Name = 'Jadzia Dax';
    '''  # update statement
    cursor.execute(update)
# 4

    select = '''
    SELECT Name, Age
    FROM Roster
    WHERE Species = 'Bajoran';
    '''
    result = cursor.execute(select).fetchall(
    )  # queries all values in the table and then, assigns them to a variable
print(result)  # prints the values from previous line
