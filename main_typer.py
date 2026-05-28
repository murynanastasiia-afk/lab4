import sys
import typer
import controller
from main_repl import repl

typer_app = typer.Typer(help="Todo CLI через typer (альтернатива argparse і click).")

@typer_app.command()
def add(text: list[str] = typer.Argument(None)):
    if text:
        controller.add_todo(" ".join(text))
        print("Успішно виконано!")
    else:
        print("Введіть текст завдання")

@typer_app.command()
def show():
    for i, t in enumerate(controller.get_all_todos()):
        print(f"{i+1}. {t.strip()}")

@typer_app.command()
def edit(number: int):
    print("Редагування через CLI недоступне. Скористайтеся WEB інтерфейсом.")

@typer_app.command()
def complete(number: int):
    try:
        controller.finish_todo(number - 1)
        print("Успішно виконано!")
    except IndexError:
        print("Не вірний номер тудушки")

@typer_app.command()
def results():
    for t in controller.get_archived_todos():
        print(f" {t.strip()}")

@typer_app.command()
def print_pdf():
    controller.generate_pdf_report()
    print("Звіт успішно збережено в папку reports! Успішно виконано!")

def main():
    if len(sys.argv) == 1:
        repl()
    else:
        typer_app()

if __name__ == '__main__':
    main()
