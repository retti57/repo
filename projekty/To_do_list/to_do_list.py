""" THIS MODULE IS AN APP EXECUTOR. Run this via commandline """
from sys import argv
from sqlite3 import OperationalError
from main import main
from application import App


if __name__ == '__main__':
    if len(argv) == 2 and argv[1] == 'db_init':
        app = App()
        app.init_db()
    elif len(argv) == 2 and argv[1] == 'update_status':
        app = App()
        app.update_db_records()
    elif len(argv) == 2 and argv[1] == 'delete_all':
        app = App()
        app.delete_db_records()
    elif len(argv) == 3 and argv[1] == 'delete_one':
        app = App()
        app.delete_task(argv[2])
    elif len(argv) == 2 and argv[1] == 'add_column':
        app = App()
        app.add_column_to_db()

    else:
        try:
            main()
        except OperationalError as e:
            print(e)
            app = App()
            app.init_db()
