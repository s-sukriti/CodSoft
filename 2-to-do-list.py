class ToDoList:
    tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            print("\nYour Current To-Do List:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")

    def complete_task(self, index):
        if not self.tasks:
            print("\nNo tasks found.")
        elif 1 <= index <= len(self.tasks):
            completed_task = self.tasks.pop(index - 1)
            print(f"\nTask '{completed_task}' marked as completed.")
        else:
            print("Invalid task index.")

def main():
    to_do_list = ToDoList()

    while True:
        print("\n----------------------------To-Do List--------------------------------")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter task: ")
            to_do_list.add_task(task)

        elif choice == '2':
            to_do_list.view_tasks()

        elif choice == '3':
            if not to_do_list.tasks:
                print("No tasks found.")
            else:
                to_do_list.view_tasks()
                index = int(input("Enter index of the task to mark as completed: "))
                to_do_list.complete_task(index)

        elif choice == '4':
            print("Exited.")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
