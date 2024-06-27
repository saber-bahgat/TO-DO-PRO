# IMPORT SQLITE3
import sqlite3
from datetime import datetime

# CONNECTING WITH DB
conn = sqlite3.connect("to_do_pro.db")
cur = conn.cursor()
cur.execute("""
    CREATE TABLE IF NOT EXISTS tasks(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT NOT NULL,
        status TEXT NOT NULL,
        deadline DATE NOT NULL
    )
""")
conn.commit()
conn.close()

# FUNCTIONS...
def add_task(task, deadline):
    conn = sqlite3.connect("to_do_pro.db")
    cur = conn.cursor()
    formatted_deadline = format_date(deadline)
    cur.execute("INSERT INTO tasks (task, status, deadline) VALUES (?, ?, ?)", (task, 'Incomplete', formatted_deadline))
    conn.commit()
    conn.close()

def format_date(user_date):
    # تحويل التاريخ إلى تنسيق SQLite المناسب
    formatted_date = datetime.strptime(user_date, '%d/%m/%Y').strftime('%Y-%m-%d')
    return formatted_date

def show_task():
    conn = sqlite3.connect("to_do_pro.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks")
    tasks = cur.fetchall()
    conn.close()
    return tasks

def edit_tasks(edit_task, edit_deadline, task_id):
    conn = sqlite3.connect("to_do_pro.db")
    cur = conn.cursor()
    cur.execute("UPDATE tasks SET task = ?, deadline = ? WHERE id = ?", (edit_task, edit_deadline, task_id))
    conn.commit()
    conn.close()

def complete_task(task_id):
    conn = sqlite3.connect("to_do_pro.db")
    cur = conn.cursor()
    cur.execute("UPDATE tasks SET status = ? WHERE id = ?", ('Complete', task_id))
    conn.commit()
    conn.close()

def delete_task(task_id):
    conn = sqlite3.connect("to_do_pro.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()


def main():
    print("Welcome to To-Do Pro!")
    while True:
        print("1. Add Task")
        print("2. Edit Task")
        print("3. Show Tasks")
        print("4. Complete Task")
        print("5. Delete Task")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            while True:
                print("-"*15)
                print("# Add Task!")
                task = input("Enter your task: ")
                deadline = input("Enter the task deadline (DD/MM/YYYY): ")
                if task and deadline:
                    add_task(task, deadline)
                    print("Task added successfully!")
                    break
                else:
                    print("Please add a correct task and deadline, try again!!")
                    continue

        elif choice == '2':
            while True:
                print("-"*15)
                print("# Edit Task!")
                task_id = int(input("Enter Task ID to Edit: "))
                edit_task = input("Enter the new task: ")
                edit_deadline = input("Enter the new deadline (DD/MM/YYYY): ")
                if edit_task and edit_deadline:
                    edit_tasks(edit_task, edit_deadline, task_id)
                    print("Task edited successfully!")
                    break
                else:
                    print("Please add a correct task and deadline, try again!!")
                    continue

        elif choice == '3':
            print("-"*15)
            print("# Show Tasks!")
            tasks = show_task()
            for task in tasks:
                print(f"[{task[0]}] {task[1]} | Deadline: {task[3]} | Status: {task[2]}")
            print("-"*15)

        elif choice == '4':
            print("-"*15)
            print("# Complete Task!")
            task_id = int(input("Enter Task ID to Complete: "))
            complete_task(task_id)
            print("Task completed successfully...")
            input("Press enter to return.........")
            print("-"*15)

        elif choice == '5':
            print("-"*15)
            print("# Delete Task!")
            task_id = int(input("Enter Task ID to Delete: "))
            delete_task(task_id)
            print("Task deleted successfully...")
            input("Press enter to return.......")
            print("-"*15)

        elif choice == '6':
            print("Thanks for trying To-Do Pro, Have a nice day!")
            break

        else:
            print("Invalid choice. Please try again.")

# RUNNING CODE
if __name__ == '__main__':
    main()
