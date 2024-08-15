import time

class Task:
    date = time.strftime('%d-%m-%Y', time.localtime())
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.date = Task.date

    def __str__(self):
        return f"{self.name} - {self.description} - {self.date}"

class TodoList:
    def __init__(self, file_path):
        self.tasks:list[Task] = []
        with open(file_path, 'r') as f:
            for line in f.readlines()[2:]:
                name, description, date = line.strip().split('||')
                self.tasks.append(Task(name, description))

    def add_task(self, task:Task):
        self.tasks.append(task)
        with open(file_path, 'a') as f:
            f.write(f"{task.name}||{task.description}||{task.date}\n")

    def remove_task(self, task):
        for i, t in enumerate(self.tasks):
            if t.name == task:
                self.tasks.pop(i)
                break
        else:
            print('Task not found!')

        with open(file_path, 'w') as f:
            f.write('--Name--||--Description--||--Date--\n\n')
            for task in self.tasks:
                f.write(f"{task.name}||{task.description}||{task.date}\n")

    def update_task(self, task):
        for i, t in enumerate(self.tasks):
            if t.name == task:
                self.tasks[i].name = input('Enter new name: ')
                self.tasks[i].description = input('Enter new description: ')
                self.tasks[i].date = Task.date
                break
        else:
            print('Task not found!')

        with open(file_path, 'w') as f:
            f.write('--Name--||--Description--||--Date--\n\n')
            for task in self.tasks:
                f.write(f"{task.name}||{task.description}||{task.date}\n")

    def display_tasks(self):
        for task in self.tasks:
            print(task)

file_path = 'tasks.csv'
with open (file_path, 'a+') as f:
    if f.tell() <= 0:
        f.write('--Name--||--Description--||--Date--\n\n')

if __name__ == '__main__':
    while True:
        print('1. Add task')
        print('2. Remove task')
        print('3. Update task')
        print('4. Display tasks')
        print('5. Exit')

        choice = int(input('Enter your choice: '))
        todo_list = TodoList(file_path)

        if choice == 1:
            name = input('Enter task name: ')
            description = input('Enter task description: ')
            task = Task(name, description)
            todo_list.add_task(task)

        elif choice == 2:
            task = input('Enter task name to remove: ')
            todo_list.remove_task(task)

        elif choice == 3:
            task = input('Enter task name to update: ')
            todo_list.update_task(task)

        elif choice == 4:
            todo_list.display_tasks()

        elif choice == 5:
            break

        else:
            print('Invalid choice!')