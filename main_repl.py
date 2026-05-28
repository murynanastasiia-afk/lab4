import time
import controller

COMMANDS = {
    "add": lambda args: controller.add_todo(args) if args else print("Введіть текст завдання!"),
    "show": lambda args: [print(f"{i+1}. {t.strip()}") for i, t in enumerate(controller.get_all_todos())],
    "edit": lambda args: print("Для редагування використовуйте WEB."),
    "complate": lambda args: controller.finish_todo(int(args)-1) if args and args.isdigit() else print("Вкажіть номер"),
    "results": lambda args: [print(f"📁 {t.strip()}") for t in controller.get_archived_todos()],
    "print": lambda args: [controller.generate_pdf_report(), print("Звіт успішно збережено в папку reports!")],
    "exit": lambda args: False
}

def dispatch(user_action):
    user_action = user_action.strip()
    if not user_action:
        print("invalid input")
        return True

    parts = user_action.split(maxsplit=1)
    cmd = parts[0].lower()
    handler = COMMANDS.get(cmd)

    if handler is None:
        print("invalid input")
        return True

    args_to_pass = parts[1] if len(parts) > 1 else None

    try:
        should_continue = handler(args_to_pass)
        if should_continue is False:
            return False
        return True

    except (ValueError, TypeError):
        print("Ваша команда не зовсім зрозуміла")
        return True
    except IndexError:
        print("Не вірний номер тудушки")
        return True

def repl():
    now = time.strftime("%b %d %Y %H:%M:%S")
    print(now)
    while True:
        user_action = input("Type add, show, edit, complate, results or exit: ")
        if not dispatch(user_action):
            break

if __name__ == '__main__':
    repl()