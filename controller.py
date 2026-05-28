import core
import functions

def get_all_todos():
    return functions.get_todos()

def get_archived_todos():
    return functions.get_todos_done()

def create_todo(task, count, date):
    return core.add_todo(task, count, date)

def update_todo(number, new_task, new_count, new_date):
    return core.edit_todo(number, new_task, new_count, new_date)

def finish_todo(number):
    return core.complete(number)

def generate_pdf_report(output_filename="reports/tasks_report.pdf"):
    
    import printer
    
    current_tasks = get_all_todos()
    archived_tasks = get_archived_todos()
    
    task_printer = printer.TaskPrinter(current_tasks, archived_tasks)
    task_printer.create_report(output_filename)
    return output_filename