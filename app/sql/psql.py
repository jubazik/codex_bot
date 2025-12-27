import sqlite3

from pathlib import Path

BASE_DIR = Path(__file__).parent
path_to_db = BASE_DIR / '../database.db'


# status_payment=False, date_joined=datetime.date.today()
class Database:
    def __init__(self, path_to_db):
        self.path_to_db = path_to_db
        self.connection = sqlite3.connect(path_to_db, check_same_thread=False)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        with self.connection:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY,
                        first_name TEXT,
                        last_name TEXT,
                        status_payment BOOLEAN,
                        date_joined DATE
                        )
                """)
            print("Таблица 'users'  проверена/создана")
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS categories (
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        description TEXT,
                        photo_url TEXT
                        )
                """)

            print("Таблица 'categories'  проверена/создана")
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS products (
                        id INTEGER PRIMARY KEY,
                        category_id INTEGER,
                        name TEXT NOT NULL,
                        description TEXT,
                        price INTEGER,
                        photo_url TEXT,
                        FOREIGN KEY (category_id) REFERENCES categories (id)
                        )
                """)
            print("Таблица 'products'  проверена/создана")

    def get_category_id(self, id):
        with self.connection:
            self.cursor.execute(f"SELECT * FROM  categories id = ?", (id,) )

    def new_user(self, id, first_name, last_name=None, ):
        with self.connection:
            return self.cursor.execute(f"INSERT INTO users (id, first_name, last_name) VALUES (?, ?, ?)",
                                       (id, first_name, last_name))

    def delete_user(self, id):
        with self.connection:
            return self.cursor.execute(f"DELETE FROM users WHERE {id} = ?", (id,))

    def get_user(self, user_id):
        """Получает пользователя по ID, преобразует 'None' в None"""
        with self.connection:
            self.cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
            row = self.cursor.fetchone()

            if row:
                # Преобразуем строку 'None' в None
                row_list = list(row)
                for i, value in enumerate(row_list):
                    if value == 'None' or value == 'null' or value == '':
                        row_list[i] = None
                return tuple(row_list)
            return None

    def get_users(self):
        user = []
        with self.connection:
            users = self.cursor.execute("SELECT * FROM users")
            for item in users.fetchall():
                user.append(item)

            return user


# class Tables:
#     def __init__(self, path_to_db):
#         self.connection = sqlite3.connect(path_to_db, check_same_thread=False)
#         self.cursor = self.connection.cursor()
#
#     def insert_user(self):
#         with self.connection:
#             return self.cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, first_name TEXT , last_name TEXT)")
#
#     def close_connection(self):
#         with self.connection:
#             return self.connection.close()
#

#
# tables = Tables(path_to_db)
# tables.insert_user()
#
# #
database = Database(path_to_db)
# print(users.get_all_users())
# print(users.get_users())
