import sqlite3


def initiate_db():
    connection = sqlite3.connect("not_telegram.db")
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    """)

    id = ['1', '2', '3', '4']
    title = ['Пилюля_1', 'Пилюля_2', 'Пилюля_3', 'Пилюля_4']
    description = ['Для мозга', 'Для почек', 'Для глаз', 'Для ног']
    price = ['100', '200', '300', '400']

    cursor.execute('INSERT INTO Products(id, title, description, price) VALUES (?, ?, ?, ?)',
                   (f'{id[0]}', f'{title[0]}', f'{description[0]}', f'{price[0]}'))
    cursor.execute('INSERT INTO Products(id, title, description, price) VALUES (?, ?, ?, ?)',
                   (f'{id[1]}', f'{title[1]}', f'{description[1]}', f'{price[1]}'))
    cursor.execute('INSERT INTO Products(id, title, description, price) VALUES (?, ?, ?, ?)',
                   (f'{id[2]}', f'{title[2]}', f'{description[2]}', f'{price[2]}'))
    cursor.execute('INSERT INTO Products(id, title, description, price) VALUES (?, ?, ?, ?)',
                   (f'{id[3]}', f'{title[3]}', f'{description[3]}', f'{price[3]}'))
    connection.commit()
    connection.close()

    connection = sqlite3.connect('not_telegram.db')
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            age INTEGER,
            balance INTEGER NOT NULL
        )
    ''')

    # for i in range(1, 11):
    #     username = f"User{i}"
    #     email = f"example{i}@gmail.com"
    #     age = i * 10
    #     balance = 1000
    #     cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?,?,?,?)", (username, email, age, balance))
    connection.commit()
    connection.close()


def get_all_products():
    connection = sqlite3.connect('not_telegram.db')
    cursor = connection.cursor()
    product_info = cursor.execute('SELECT * FROM Products')
    product_info = cursor.fetchall()
    return list(product_info)


def add_user(username, email, age):
    connection = sqlite3.connect('not_telegram.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO Users (username,email,age,balance) VALUES (?,?,?,?)',
                   (f'{username}', f'{email}', age, 1000))
    connection.commit()
    connection.close()


def is_included(username):
    connection = sqlite3.connect('not_telegram.db')
    cursor = connection.cursor()
    check_user = cursor.execute('SELECT * FROM Users WHERE username = ?', (username,))
    if check_user.fetchone() is None:
        return True
    else:
        return False

    connection.commit
    connection.close()
