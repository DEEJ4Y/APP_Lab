import sqlite3

conn = sqlite3.connect("./moviesDB.db")
cursor = conn.cursor()
defaultTableName = 'movies'


def createTable():
    command = """
    CREATE TABLE IF NOT EXISTS {defaultTableName} (
        id INTEGER PRIMARY KEY,
        name TEXT,
        genre TEXT,
        language TEXT,
        rating INTEGER
        );
    """.format(defaultTableName=defaultTableName)
    cursor.execute(command)


def getAll(tableName):
    command = f'SELECT * FROM {tableName};'
    print(command)

    cursor.execute(command)
    retval = cursor.fetchall()

    return retval


def getOneById(tableName, id):
    command = f'SELECT * FROM {tableName} WHERE id = {id};'

    cursor.execute(command)
    retval = cursor.fetchone()

    return retval


def displayAll(tableName, data):
    if data is None:
        data = getAll(tableName)

    if len(data) == 0:
        print("EMPTY")
    else:
        for row in data:
            print(row)


def getId(tableName):
    data = getAll(tableName)
    return len(data) + 1


def insertMovie(name, genre, lang, rating):
    id = getId(defaultTableName)
    command = f'INSERT INTO {defaultTableName} VALUES ({id}, "{name}", "{genre}", "{lang}", {rating});'
    cursor.execute(command)


def updateMovieRatingById(movieId):
    data = getOneById(defaultTableName, movieId)
    rating = data[4]
    updatedRating = int(rating * 1.1)
    command = f'UPDATE {defaultTableName} SET rating = {updatedRating} WHERE id = \'{movieId}\';'
    print(command)

    cursor.execute(command)
    retval = cursor.fetchall()

    return retval


def deleteMovieRatingById(movieId):
    command = f'DELETE FROM {defaultTableName} WHERE id = \'{movieId}\';'
    cursor.execute(command)


def main():
    createTable()
    # insertMovie("A mauvaix movie", "oui", "French", 2)

    # updateMovieRatingById(3)

    # command = f'INSERT INTO {defaultTableName} VALUES (102, "NAME 102", "GONAN BE DELETED", "ENGLISHH", 100);'
    # cursor.execute(command)

    # deleteMovieRatingById(102)

    # command = f'SELECT * FROM {defaultTableName} WHERE rating > 3;'
    # cursor.execute(command)
    # data = cursor.fetchall()
    # displayAll(defaultTableName, data)

    displayAll("movies", None)
    conn.commit()
    conn.close()


main()
