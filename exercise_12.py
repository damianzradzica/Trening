import argparse
from mysql import connector


def set_options():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--cinema",
                        action="store", dest="cinema",
                        help="Cinema's name")
    parser.add_argument("-a", "--address",
                        action="store", dest="address",
                        help="Write the correct address of the cinema")
    parser.add_argument("-n", "--new", dest="new", action='store_true',
                        help="Add next cinema")
    parser.add_argument("-d", "--delete",
                        action="store_true", dest="delete",
                        help="Delete the cinema")
    parser.add_argument("-s", "--search",
                        action="store_true", dest="search",
                        help="Searching option")
    options = parser.parse_args()
    return options


def solution(options):
    cnx = connector.connect(
        user='root',
        password='coderslab',
        host='localhost',
        database='cinema1_db'
    )

    cursor = cnx.cursor()

    # Dodawanie nowego kina
    sql1 = '''
    INSERT INTO Cinemas VALUES (0, "{}", "{}");
    '''.format(options.cinema, options.address)

    # Usuwanie kina
    sql2 = '''
    DELETE FROM Cinemas WHERE name="{}" AND adress = "{}";
    '''.format(options.cinema, options.address)

    # Wyświetlanie kina
    sql3 = '''
    SELECT * FROM Cinemas WHERE name="{}";
    '''.format(options.cinema)

    try:
        if options.new:
            if options.address and options.cinema:
                cursor.execute(sql1)
                cnx.commit()
                print(sql1)
            else:
                raise ValueError("Za mało danych")
        elif options.delete:
            if options.address and options.cinema:
                cursor.execute(sql2)
                cnx.commit()
                print(sql2)
            else:
                raise ValueError("Podaj także adres i nazwę kina")
        elif options.search:
            if options.cinema:
                cursor.execute(sql3)
                for i in cursor:
                    print(i)
            else:
                raise ValueError("Podaj także nazwę kina")

    finally:
        cursor.close()
        cnx.close()


if __name__ == "__main__":
    solution(set_options())