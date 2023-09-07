from application import App


def main():
    app = App()
    app.print_tasks()
    app.print_menu_guide()

    user_inp = input('Podaj numer z menu: ')
    try:
        if user_inp not in [str(x) for x in range(0, 5)]:
            raise ValueError

        match user_inp:
            case '1':
                task_title = input('Jakie zadanie dodać?: ').strip()
                app.add_task(task_title)
                main()
            case '2':
                print(" > Nie chcę nic usunąć, powrót (wpisz zero '0') < ")
                todo_id_task = int(input("Podaj numer zadania które chcesz skasować:\n> ").strip())

                if todo_id_task != 0:
                    app.update_status_of_finished_task(todo_id_task)
                print(f"{str(app.fetch_time_until_finished_task(todo_id_task) / 60).split('.')[0]} minut minęło")

                main()

            case '3':
                main()

            case '4':
                exit()
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
    except ValueError as e:
        print(("Podano niepoprawną wartość", e))
        main()

