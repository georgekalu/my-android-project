import os

TODO_FILE = "todos.txt"

def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as f:
            return [line.strip() for line in f.readlines()]
    return []

def save_tasks(tasks):
    with open(TODO_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def show_tasks(tasks):
    if not tasks:
        print("📭 Your to-do list is empty!")
        return
    print("\n📋 Your To-Do List:")
    for i, task in enumerate(tasks, 1):
        status = "✅" if "[DONE]" in task else "⭕"
        print(f"{i}. {status} {task.replace('[DONE]', '').strip()}")

print("📝 To-Do List Manager")
print("====================\n")

tasks = load_tasks()

while True:
    print("\n" + "="*30)
    print("1. Add new task")
    print("2. View tasks")
    print("3. Mark task as done")
    print("4. Delete task")
    print("5. Exit")

    choice = input("\nEnter your choice (1-5): ")

    if choice == "1":
        task = input("Enter new task: ").strip()
        if task:
            tasks.append(task)
            save_tasks(tasks)
            print("✅ Task added!")
    elif choice == "2":
        show_tasks(tasks)
    elif choice == "3":
        show_tasks(tasks)
        if tasks:
            try:
                idx = int(input("\nEnter task number to mark as done: ")) - 1
                if 0 <= idx < len(tasks) and "[DONE]" not in tasks[idx]:
                    tasks[idx] = "[DONE] " + tasks[idx]
                    save_tasks(tasks)
                    print("✅ Task marked as done!")
                else:
                    print("Invalid or already done.")
            except:
                print("Please enter a valid number.")
    elif choice == "4":
        show_tasks(tasks)
        if tasks:
            try:
                idx = int(input("\nEnter task number to delete: ")) - 1
                if 0 <= idx < len(tasks):
                    deleted = tasks.pop(idx)
                    save_tasks(tasks)
                    print(f"🗑️ Deleted: {deleted}")
                else:
                    print("Invalid number.")
            except:
                print("Please enter a valid number.")
    elif choice == "5":
        print("\nGoodbye! Your tasks have been saved. 💪")
        break
    else:
        print("Invalid choice! Please enter 1-5.")

    input("\nPress Enter to continue...")
