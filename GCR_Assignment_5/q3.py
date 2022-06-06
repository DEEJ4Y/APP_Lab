import sqlite3

conn = sqlite3.connect("./courseDB.db")
cursor = conn.cursor()
defaultTableName = 'products'
ordersTableName = 'orders'


def createTable():
    command = """
    CREATE TABLE IF NOT EXISTS {defaultTableName} (
        id INTEGER PRIMARY KEY,
        name TEXT,
        supplierId INTEGER,
        unitPrice INTEGER
        );
    """.format(defaultTableName=defaultTableName)
    cursor.execute(command)


def createOrdersTable():
    command = """
    CREATE TABLE IF NOT EXISTS {defaultTableName} (
        id INTEGER PRIMARY KEY,
        productId INTEGER,
        quantity INTEGER,
        FOREIGN KEY(productId) REFERENCES products(id)
        );
    """.format(defaultTableName=ordersTableName)
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


def insertProduct(
    name, supplierId, unitPrice
):
    id = getId(defaultTableName)
    command = f'INSERT INTO {defaultTableName} VALUES ({id}, "{name}", {supplierId}, {unitPrice});'
    cursor.execute(command)


def insertOrder(
    productId, quantity
):
    id = getId(ordersTableName)
    command = f'INSERT INTO {ordersTableName} VALUES ({id}, {productId}, {quantity});'
    cursor.execute(command)


def main():
    createOrdersTable()
    createTable()

    displayAll(defaultTableName, None)
    displayAll(ordersTableName, None)

    # insertProduct("Product 1", 234, 29)
    # insertProduct("Product 2", 3485, 19)
    # insertProduct("Product 3", 1234, 39)

    # insertOrder(1, 3)
    # insertOrder(2, 2)
    # insertOrder(3, 4)

    conn.commit()
    conn.close()


main()
