#1  ToDo List Application
class Task:
    def __init__(self, title, description, due_date, status = "Incomplete"):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def __str__(self):
        return f'{self.title}, {self.description}, {self.due_date}, {self.status}'

    def mark_complete(self):
        self.status ='Completed'

class ToDoList:
    
    def __init__(self):
        self.list_of_tasks = []

    def add_task(self, task: Task):
        self.list_of_tasks.append(task)
        print(f"\nNew task'{task.title}' was created")

    def complete_task(self, index):
        self.list_of_tasks[index-1].mark_complete()
        print(f"\nTask '{self.list_of_tasks[index-1].title}' was marked complete")

    def list_all(self):
        if self.list_of_tasks:
            for index, task in enumerate(self.list_of_tasks):
                print(f"{index+1}. {task}")
        else:
            print("\nThere are no tasks in your to-do list, yet.")
        
    def list_incomplete(self):
        for index, task in enumerate(self.list_of_tasks):
            if task.status == 'Incomplete':
                print(f"{index}. {task}")
        else:
            print("\nYou don't have any uncompleted tasks")


def print_menu():
    print('\nTo-Do List Menu: ')
    print('1. Add a task')
    print('2. Mark a task as complete')
    print('3. List all tasks')
    print('4. Display incomplete tasks')  
    print('5. Exit')  

def main():
    task1 = Task('Reading', 'Finishing 13th chapter of "Demon haunted world"', '2025-06-05', 'Incomplete')
    To_Do = ToDoList()
    To_Do.add_task(task1)


    while True:
        
        print_menu()
        choice = input('Enter your choice (1-5): ')

        if choice == '1':
            title = input('Please, enter the title of your task: ')
            description = input('Please, enter the description of your task: ')
            due_date = input('Please, enter the deadline of your task: ')
            new_task = Task(title, description, due_date)
            To_Do.add_task(new_task)

        elif choice == '2':
            print('\n')
            To_Do.list_all()
            print('\n')
            ind = int(input('Select the number of the task you want to mark as complete: '))
            To_Do.complete_task(ind)

        elif choice == '3':
            print('\nYour tasks:')
            To_Do.list_all()

        elif choice == '4':
            print('\nIncomplete tasks:')
            To_Do.list_incomplete()

        elif choice == '5':
            print('\nGoodbye!\n')
            break
        
        else:
            print('Invalid choice')

if __name__=="__main__":
    main()
