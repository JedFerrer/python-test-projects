class TodoApp:

    def __init__(self):
        self.todo_list = []

    def add(self):
        todo = input('Enter a todo list: ')
        self.todo_list.append(todo)

    def edit(self):
        self.view()
        try:
            index = input(
                'Enter the number of todo that you want to edit: ')
            index = int(index) - 1
            self.todo_list[index] = input(
                f"Edit value (current: {self.todo_list[index]}): ") or self.todo_list[index]
            print("Task Edited!")
        except:
            print("Invalid task number.")

    def view(self):
        print('--------TODO LIST--------')
        if not self.todo_list:
            print("No tasks available.")
        for index, todo in enumerate(self.todo_list):
            print(f"{index + 1}) {todo}")

    def delete(self):
        self.view()
        try:
            index = input(
                'Enter the number of todo that you want to delete: ')
            index = int(index) - 1
            self.todo_list.pop(index)
            print("Task deleted!")
        except:
            print("Invalid task number.")

    def run(self):
        print('--------TODO App 2025-------- \n')
        while True:
            choice = input(
                "Options: (A)dd, (V)iew, E(dit), (D)elete, (Q)uit: ")
            choice = choice.lower().strip()

            if choice == 'a':
                self.add()
            elif choice == 'e':
                self.edit()
            elif choice == 'v':
                self.view()
            elif choice == 'd':
                self.delete()
            elif choice == 'q':
                break
            else:
                print("Invalid choice!")


# Run TodoApp
if __name__ == "__main__":
    TodoApp().run()
