import sys
import argparse
import controller
from main_repl import dispatch, repl

def build_parser():
    parser = argparse.ArgumentParser(
        prog='todo',
        description="Todo CLI App (argparse)"
    )
    sub = parser.add_subparsers(dest="command")

    p_add = sub.add_parser("add", help="Додати завдання")
    p_add.add_argument("text", nargs="+", help="Текст завдання")

    sub.add_parser("show", help="Показати список")

    p_edit = sub.add_parser("edit", help="Редагувати")
    p_edit.add_argument("number", type=int, help="Номер завдання")

    p_complate = sub.add_parser("complate", help="Виконати")
    p_complate.add_argument("number", type=int, help="Номер завдання")

    sub.add_parser("results", help="Показати результати")
    sub.add_parser("print", help="Надрукувати звіт у PDF")
    sub.add_parser("repl", help="Запустити через repl")
    return parser

def run_args(args):
    if args.command == "add":
        task_text = " ".join(args.text)
        dispatch(f"add {task_text}")
    elif args.command == "show":
        dispatch("show")
    elif args.command == "edit":
        dispatch(f"edit {args.number}")
    elif args.command == "complate":
        dispatch(f"complate {args.number}")
    elif args.command == "results":
        dispatch("results")
    elif args.command == "print":
        dispatch("print")
    elif args.command == "repl":
        repl()

def main():
    if len(sys.argv) == 1:
        repl()
        return
    parser = build_parser()
    args = parser.parse_args()
    run_args(args)

if __name__ == '__main__':
    main()