"""This module is responsible for all tasks with database"""
import sqlite3


class AppDB:

    def __init__(self):
        with sqlite3.connect('To_do_list.db') as db_connection:
            self.connection = db_connection
            self.cursor = self.connection.cursor()

    def init_db(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS todos(
                todo_id INTEGER PRIMARY KEY,
                title VARCHAR(100) NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                finished_at TIMESTAMP DEFAULT NULL,
                is_done INTEGER DEFAULT 0
            )""")

        self.connection.commit()

    def update_db_records(self):
        self.cursor.execute("SELECT COUNT(*) FROM todos;")  # liczba wierszy
        for num in range(self.cursor.fetchone()[0] + 1):
            self.cursor.execute('UPDATE todos SET is_done=0, finished_at=NULL WHERE todo_id=?', (num,))

        self.connection.commit()

    def delete_task(self, todo_id):
        self.cursor.execute('DELETE FROM todos WHERE todo_id=?', (todo_id,))
        self.connection.commit()

    def delete_db_records(self):
        self.cursor.execute('DELETE FROM todos')
        self.connection.commit()

    def add_column_to_db(self):
        self.cursor.execute('ALTER TABLE todos ADD COLUMN elapsed_time TIMESTAMP')
        self.connection.commit()

    def print_tasks(self):
        records = self.cursor.execute('SELECT todo_id, title, is_done FROM todos WHERE is_done=0')  #  pomiędzy SELECT a FROM można dać * co oznacza wszystko
        print('Zawartość listy:')

        for todo_id, title, _ in records:
            print(f'{todo_id}- {title}')

    def add_task(self, title: str):
        self.cursor.execute('INSERT INTO todos(title) VALUES (?)', (title,))
        self.connection.commit()
        print(f"Dodano do listy: {title}")

    def update_status_of_finished_task(self, todo_id: int):
        self.cursor.execute('UPDATE todos SET is_done=1, finished_at=CURRENT_TIMESTAMP WHERE todo_id=?', (todo_id,))
        self.connection.commit()
        print(f"Zakończono zadanie: {todo_id}.\n")

    def fetch_time_until_finished_task(self, todo_id):
        # TIMESTAMP zapisuje w sekundach od czasu unix
        self.cursor.execute(
            'SELECT strftime("%s", finished_at) - strftime("%s", created_at) AS diff FROM todos WHERE todo_id=?',
            (todo_id,))

        return self.cursor.fetchone()[0]


class App(AppDB):
    @staticmethod
    def print_menu_guide():
        instructions = [
            "Dodaj zadanie",
            "Zakończ zadanie",
            "Wyświetl zadania",
            "Zamknij",
        ]
        print('---------\n')
        for number, instruction in enumerate(instructions, 1):
            print(f'{number}. {instruction}')
        print('\n---------')


# 7. wyświetlać na przeglądarce