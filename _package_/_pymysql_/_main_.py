import pymysql

db = pymysql.connect("localhost", "root", "admin", "test")
cursor = db.cursor()


def test_1():
    cursor.execute("SELECT VERSION()")
    data = cursor.fetchone()
    print("Database version ", data)


def test_2():
    try:
        cursor.execute("INSERT INTO user(name) VALUES ('Mac')")
        db.commit()
    except:
        db.rollback()


def test_3():
    try:
        cursor.execute("SELECT * FROM user")
        results = cursor.fetchall()
        for row in results:
            print(row[0], row[1])
    except:
        print("Error: unable to fecth data")


def test_4():
    try:
        cursor.execute("UPDATE user SET name = 'Bob' WHERE id = 1")
        db.commit()
    except:
        db.rollback()


def test_5():
    try:
        cursor.execute("DELETE FROM user WHERE id  = 1")
        db.commit()
    except:
        db.rollback()


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
    test_4()
    test_5()

db.close()
