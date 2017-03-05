from mysql import connector


def solution():
    cnx = connector.connect(
        user='root',
        password='coderslab',
        host='localhost',
        database='exercises_db'
    )
    cursor = cnx.cursor()

    sql = '''CREATE DATABASE exercises_db'''

    cursor.execute(sql)

    cursor.close()
    cnx.close()


if __name__ == "__main__":
    solution()


def solution2():
    cnx = connector.connect(
        user='root',
        password='coderslab',
        host='localhost',
        database='exercises_db'
    )
    cursor = cnx.cursor()

    sql = '''CREATE TABLE Product
    (
    id int,
    name varchar(255),
    description varchar(255),
    price float(5, 2)
    );

    CREATE TABLE productsOrder
    (
    id int,
    description varchar(255)
    );

    CREATE TABLE Client
    (
    id int,
    name varchar(255),
    surname varchar(255)
    );'''

    try:
        cursor.execute(sql, multi=True)
    except ProgrammingError as e:
        print(e)

    cursor.close()
    cnx.close()