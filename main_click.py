import click
import controller
from main_repl import repl

@click.group(help="Todo CLI start")
def click_cli():
    pass

@click_cli.command("add")
@click.argument("text", nargs=-1)
def click_add(text):
    if text:
        controller.add_todo(" ".join(text))
        print("Успішно виконано!")
    else:
        print("Введіть текст завдання")

@click_cli.command("show")
def click_show():
    for i, t in enumerate(controller.get_all_todos()):
        print(f"{i+1}. {t.strip()}")
    print("Успішно виконано!")

@click_cli.command("edit")
@click.argument("number", type=int)
def click_edit(number):
    print("Редагування через CLI недоступне. Скористайтеся WEB інтерфейсом.")

@click_cli.command("complete")
@click.argument("number", type=int)
def click_complete(number):
    try:
        controller.finish_todo(number - 1)
        print("Успішно виконано!")
    except IndexError:
        print("Не вірний номер тудушки")

@click_cli.command("results")
def click_results():
    for t in controller.get_archived_todos():
        print(f"{t.strip()}")
    print("Успішно виконано!")

@click_cli.command("print")
def click_print():
    controller.generate_pdf_report()
    print("Успішно виконано!")

@click_cli.command("repl")
def click_repl():
    repl()

if __name__ == "__main__":
    click_cli()
