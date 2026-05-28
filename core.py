from functions import get_todos, write_todos, get_todos_done, write_todos_done
import time
def add_todo(task, count, date):
         try:
                if not isinstance(count, int) and date<time.strftime('%d%m'):
                   raise ValueError("Невірний тип count або застаріла дата")
                new_todo = f"{date} {task} 0/{count}\n"
                todos=get_todos()
                todos.append(new_todo)
                write_todos(todos)
                return True
         except IndexError:
                 print("Введено у невірному форматі")
                 return False
def show_results(user_action=None):
         todos=get_todos_done()
         if not todos:
                  print("Список порожній")
         else:
                  for index, item in enumerate(todos):
                           row=f"{index+1}--{item.strip('\n')}"
                           print(row)
         return True
def show_todos(user_action=None):
         todos=get_todos()
         for index, item in enumerate(todos):
                  row=f"{index+1}--{item.strip('\n')}"
                  print(row)
         return True
def edit_todo(number, new_task, new_count, new_date):
         try:
                  todos = get_todos()
                  number=int(number)
                  if number<0 or number>=len(todos):
                           print("Невірний номер завдання")
                           return True
                  todos[number] = f"{new_date} {new_task} 0/{new_count}\n"
                  write_todos(todos)
         except IndexError:
                  print("Сталася помилка")
         return True
def complete(number):
         try:
                  todos = get_todos()
                  if number<0 or number>= len(todos):
                           raise IndexError
                  todo = todos[number].strip()
                  parts = todo.rsplit(' ', 1)
                  task = parts[0]
                  counts = parts[1]
                  current, goal = counts.split('/')
                  new_current = int(current) + 1
                  int_goal = int(goal)
                  new_todo = f"{task} {new_current}/{int_goal}\n"

                  if new_current == int_goal:
                           message=f"\tЗавдання '{task}' було успішно виконане!"
                           print(message)
                           todos.pop(number)
                                

                           done_todos = get_todos_done()
                           done_todos.append(new_todo)
                           write_todos_done(done_todos)
                  else:
                           todos[number] = new_todo
                  write_todos(todos)

         except IndexError:
                  print("Невірний номер завдання")
         return True
def do_exit(user_action=None):
        return False


                 
                              

         