import sqlite3

conn = sqlite3.connect("./recipesDB.db")
cursor = conn.cursor()
defaultTableName = 'recipes'


def createTable():
    command = """
    CREATE TABLE IF NOT EXISTS {defaultTableName} (
        id INTEGER PRIMARY KEY,
        name TEXT,
        description TEXT,
        category_id INTEGER,
        chef_id TEXT,
        created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """.format(defaultTableName=defaultTableName)
    cursor.execute(command)


def getAll(tableName):
    command = f'SELECT * FROM {tableName};'
    print(command)

    cursor.execute(command)
    retval = cursor.fetchall()

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


def insertRecipe(name, desc, categoryId, chefId):
    id = getId('recipes')
    command = f'INSERT INTO recipes VALUES ({id}, "{name}", "{desc}", "{categoryId}", "{chefId}", null);'
    cursor.execute(command)


def getChinese():
    command = f'SELECT * FROM {defaultTableName} WHERE description = \'Chinese\';'
    print(command)

    cursor.execute(command)
    retval = cursor.fetchall()

    return retval


def getRecipesByChefId(chefId):
    command = f'SELECT * FROM {defaultTableName} WHERE chef_id = \'{chefId}\';'
    print(command)

    cursor.execute(command)
    retval = cursor.fetchall()

    return retval


def getRecipesThatStartWithSomething(something):
    command = f'SELECT * FROM {defaultTableName} WHERE name LIKE \'{something}%\';'

    cursor.execute(command)
    retval = cursor.fetchall()

    return retval


def main():
    createTable()
    # insertRecipe("Spring rolls", "Chinese",
    #              "asj298347fjahsdfkja", "A1")
    # displayAll("recipes", None)
    # displayAll('recipes', getChinese())
    # displayAll('recipes', getRecipesByChefId('D1'))
    # displayAll('recipes', getRecipesThatStartWithSomething("p"))
    conn.commit()
    conn.close()


main()
