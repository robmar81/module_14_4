import sqlite3



def initiate_db():
    connection = sqlite3.connect("Products.db")
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products(
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT,
        price INTEGER NOT NULL
        )
        ''')
    products = [
        ('Витамины группы В', 'Для повышения жизненного тонуса, улучшения состояния нервной системы', 100),
        ('Витамин С', 'Необходим человеку для поддержания жизнедеятельности. ', 200),
        ('Витамин Д-3', 'Укрепляет иммунитет, улучшает обмен веществ.', 300),
        ('Витамин Е', 'Важен для здоровья кожи и органов зрения.', 400)
    ]

    cursor.executemany('INSERT OR IGNORE INTO Products(title, description, price) VALUES(?, ?, ?)', products)

    connection.commit()
    connection.close()



def get_all_products():
    connection = sqlite3.connect("Products.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Products")
    products = cursor.fetchall()
    connection.commit()
    connection.close()
    return products




if __name__ == "__main__":
    initiate_db()
