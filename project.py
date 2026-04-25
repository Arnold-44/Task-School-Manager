from tabulate import tabulate
import json, sys, argparse

#la classe
class Task:
    def __init__(self, title, category, priority = 3, completed = False):
        self.title = title
        self.category = category
        self.priority = priority
        self.completed = completed

    #methode d'affichage 
    def __str__(self):
        status = "✅" if self.completed else "❌"
        return f"{status} [{self.category}] {self.title} (Prio: {self.priority})"
    
    #transforme un objet en dictionnaire json
    def to_dict(self):
        return {
            "title": self.title,
            "category": self.category,
            "priority": self.priority,
            "completed": self.completed
        }
    
    # prend un dictionnaire (lu depuis le fichier JSON) et recrée un objet Task tout propre
    @classmethod
    def from_dict(cls, data):
        #extraction/ recuperation des donnees
        return cls(
            title = data["title"],
            category = data["category"],
            priority = data["priority"],
            completed = data["completed"]
        )
        


"""fonction globale """
#add_task
def add_task(tasks, title, category, priority):
    #creation d'une tache
    new_task = Task(title, category, priority)

    #ajout 
    tasks.append(new_task)

    return tasks

# remove_task
def remove_task(tasks, i):
    try:
        #on commence a 1 et non a 0
        ajust_i = i - 1

        #supprime la tache
        tasks.pop(ajust_i)

        return tasks
    except IndexError:
        print("Error: index not found")

        return tasks

# format_tasks
def format_tasks(tasks):
    if not tasks:
        return "No tasks found"
    
    #creation de la liste pour tabulate
    table_data = []

    for i, task in enumerate(tasks, start= 1):
        #extraction des donnees
        status = "✅" if task.completed else "❌"
        table_data.append([i, task.title, task.category, task.priority, status])

    #definit l'entete
    header = ["ID", "Title", "Category", "Priority", "Status"]

    #retourne le tableau formate
    return tabulate(table_data, headers=header, tablefmt="grid")

""" Fonction de gestion de fichiers"""
#sauvegarder une tache
def save_tasks(tasks, filename="tasks.json"):
    list_task = [task.to_dict() for task in tasks]
    
    #ecrit dans le fichier
    with open(filename, "w") as file:
        json.dump(list_task, file, indent = 4)


#charger une tache
def load_tasks(filename="tasks.json"):
    try:
        with open(filename, "r") as file:
            #recupere la liste
            list_task = json.load(file)

            #transforme en dictionnaire d'objet
            return [Task.from_dict(data) for data in list_task]
    
    except FileNotFoundError:
        return []



#fonction principale
def main():
    #recupere les donnees
    tasks = load_tasks()

    #configure argparse
    parser = argparse.ArgumentParser(description="Task-School-Manager: A professional task manager students")

    #ajout des arguments
    parser.add_argument("-a", "--add", help="Add a new task(provider title)")
    parser.add_argument("-c", "--cat", default="General", help="Category of the task")
    parser.add_argument("-p", "--prio", type=int, default=3, help="Priority (1: High, 3: Low)")
    parser.add_argument("-l", "--list", action="store_true", help="Display all tasks")
    parser.add_argument("-d", "--delete", type=int, help="Delete a task by the ID")
    parser.add_argument("-f", "--finish", type=int, help="Mark a task as completed by it's ID")
   
    args = parser.parse_args()

    #decision
    if args.add:
        add_task(tasks, args.add, args.cat, args.prio)
        save_tasks(tasks)
        print("Task added successfully!")

    elif args.list:
        print(format_tasks(tasks))
    
    elif args.delete:
        tasks = remove_task(tasks, args.delete)
        save_tasks(tasks)
        print(f"Task {args.delete} deleted")
    
    elif args.finish:
        #pour cocher une tache
        if 0 < args.finish <= len(tasks):
            tasks[args.finish - 1].completed = True
            save_tasks(tasks)
            print(f"Task {args.finish} completed! ✅")
        else:
            print("Invalid ID")

    else:
        #aucun argument
        parser.print_help()

if __name__ == "__main__":
    main()
