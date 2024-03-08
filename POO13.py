#Desenvolva um aplicativo de gerenciamento de tarefas
#em python. Crie duas classes, Tarefa e Projeto, com uma
#associação unidirecional. Permita que as tarefas sejam
#associadas a projetos e que você possa listar as tarefas

#de um projeto em particular.Desenvolva um aplicativo de gerenciamento de tarefas
#em python. Crie duas classes, Tarefa e Projeto, com uma
#associação unidirecional. Permita que as tarefas sejam
#associadas a aprojetos e que você possa listar as tarefas
#de um projeto em particular.

class Task:
    def __init__(self):
        self.list_task = [] 

    def add_task(self): # Adicionar tarefas:
        name = str(input("Enter name the Task:")) 
        description = str(input("Description task:"))
        quantity = int(input("Enter quantity of task:"))
        difficulty = int(input("Enter the difficulty of task:")) 
        add_tasks_info = {'name': name, 'description': description, 'quantity': quantity, 'difficulty': difficulty}
        self.list_task.append(add_tasks_info)

    def list_tasks(self): #Listas as tarefas:
        print("List task:")
        for task in self.list_task:
            print(task)
    
    def remove_tasks(self):#Removendo alguma tarefa:
        remove_task = str(input("Which task do you want to remove:"))
        for task in self.list_task:
            if task['name'] == remove_task:
                self.list_task.remove(task)
                print(f'Task "{remove_task}" removed successfully.')
                break
            else:
                print(f'Task "{remove_task}" not found.')


    def show_task_update(self):#Mostrando as tarefas atualizadas:
        show_task = input("You want to show all registered tasks[yes/no]:")
        if show_task.lower() == 'yes':
            print("Show Tasks:")
            print(self.list_task)
        elif show_task.lower() == 'no':
            print("The user does not want to show the completed tasks. ")
        else:
            raise ValueError("This option is invalid...")

    def priority_task(self):
        task_priority = input("Do you want priority task in list tasks [yes/no]:")
        if task_priority.lower() == 'yes':
            task_name = input("Enter the name of the task you want to prioritize: ")
            for task in self.list_task:
                if task['name'] == task_name:
                    print(f"The task: {task['name']} has priority.")
                    break
            else:
                print(f'Task "{task_name}" not found.')
        elif task_priority.lower() == 'no':
            print('The user does not have a priority task.')
        else:
            raise ValueError("This option is invalid...")
        

class Project:
    @classmethod
    def main_program_task(cls, task_instance):
        while True:
            print("TO DO LIST")
            print('''<-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=->
                Type (1) Add Task.
                Type (2) List Task.
                Type (3) Remove Task.
                Type (4) Show Task Update.
                Type (5) Priority Task.
                Type (0) Exit Program.
                <-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=->''')
            option = int(input("Enter a option:"))
            if option == 1:
                task_instance.add_task()
            elif option == 2:
                task_instance.list_tasks()
            elif option == 3:
                task_instance.remove_tasks()
            elif option == 4:
                task_instance.show_task_update()
            elif option == 5:
                task_instance.priority_task()
            elif option == 0:
                print("Exit program.")
                break
            else:
                raise ValueError("Choose the option 1-5. Try again...")
            
if __name__ == "__main__":
    task_instance = Task()
    Project.main_program_task(task_instance)