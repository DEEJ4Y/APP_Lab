import sqlite3
import datetime

conn = sqlite3.connect("./jobsDB.db")
cursor = conn.cursor()
defaultTableName = 'jobs'
jobHistoryTableName = 'jobHistory'


def createTable():
    command = """
    CREATE TABLE IF NOT EXISTS {defaultTableName} (
        id INTEGER PRIMARY KEY,
        title TEXT,
        minSalary INTEGER,
        maxSalary INTEGER,
        UNIQUE(id,title,minSalary,maxSalary)
        );
    """.format(defaultTableName=defaultTableName)
    cursor.execute(command)


def createJobHistoryTable():
    command = """
    CREATE TABLE IF NOT EXISTS {defaultTableName} (
        id INTEGER PRIMARY KEY,
        employeeId INTEGER NOT NULL UNIQUE,
        jobId INTEGER,
        departmentId INTEGER,
        startDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        endDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(jobId) REFERENCES jobs(id)
        );
    """.format(defaultTableName=jobHistoryTableName)
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


def insertJob(title: str, minSalary: int, maxSalary: int):
    id = getId(defaultTableName)
    command = f'INSERT INTO {defaultTableName} VALUES ({id}, "{title}", {minSalary}, {maxSalary});'
    cursor.execute(command)


def insertJobHistory(employeeId: int, jobId: int, departmentId: int):
    id = getId(jobHistoryTableName)
    command = f'INSERT INTO {jobHistoryTableName} VALUES ({id}, {employeeId}, {jobId}, {departmentId}, "{getCurrentTimestamp()}", "{getCurrentTimestamp()}");'
    cursor.execute(command)


def getCurrentTimestamp():
    return datetime.datetime.now().replace(microsecond=0).isoformat()


def deleteJobById(jobId):
    command = f'DELETE FROM {defaultTableName} WHERE id = \'{jobId}\';'
    cursor.execute(command)


def main():
    createTable()
    # insertJob("A mauvaix job", 5000, 7000)
    # insertJob("A good job", 10000, 15000)
    # insertJob("A great job", 15000, 20000)

    createJobHistoryTable()
    # insertJobHistory(1, 1, 1)
    # insertJobHistory(2, 3, 2)
    # insertJobHistory(3, 2, 3)

    displayAll(defaultTableName, None)
    displayAll(jobHistoryTableName, None)

    conn.commit()
    conn.close()


main()
