FILEPATH =r"input.txt"
FILEPATH2 =r"output.txt"
def get_todos(filepath = FILEPATH):
         with open(filepath, 'r', encoding='utf-8') as f:
                 todos_local=f.readlines()
         return todos_local
def write_todos(todos_arg, filepath=FILEPATH):
         with open(filepath, 'w', encoding='utf-8') as file:
                 file.writelines(todos_arg)
def get_todos_done(filepath = FILEPATH2):
         with open(filepath, 'r', encoding='utf-8') as f:
                 todos_local=f.readlines()
         return todos_local
def write_todos_done(todos_arg, filepath=FILEPATH2):
         with open(filepath, 'w', encoding='utf-8') as file:
                 file.writelines(todos_arg)