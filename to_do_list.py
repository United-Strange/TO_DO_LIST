import sqlite3
import time

def welcome():
    print("please press any botton to continue...")
    print("for watching your tasks please write 1 ")
    print("for adding new task to your plan please write 2 ")
    print("for Delete the task press 3")
    print("EXIT 4")
    loop = True
    while loop:
        try:
            user_request = int(input())
            loop = False
        except:
            print("please enter a valid number!")
            loop = True
    return user_request
            
def data_base_connection():
    con = sqlite3.connect("to_do_list.db")
    cur = con.cursor()
    
    
    cur.execute("""
                CREATE TABLE IF NOT EXISTS list (
                    id INTEGER PRIMARY KEY,
                    task TEXT,
                    is_done TEXT
                    )
                """)
    con.commit()
    return cur, con
    
    
    
def adding_task(cur, con, is_doneyet="no"):
    new_task = input("write your task: ")
    cur.execute("INSERT INTO list (task, is_done) VALUES (?,?)", (new_task, is_doneyet))
    print(f"your task has succesfully added to your list")
    con.commit()


def deleting_task(cur, con):
    loop_trying = True
    print(show_all_tasks(cur))
    
    while loop_trying:
        try:
            delete_id_request = int(input("please write the task id that you want to delete: "))
            cur.execute("DELETE FROM list WHERE id = ?", (delete_id_request,))
            if cur.rowcount > 0:
                con.commit()
                loop_trying = False
                print(f"you have succesfully deleted the {delete_id_request} id")
            else:
                print("this id does not exist!")
        except:
            print("please write a VALID NUMBER !")
            
    
def show_all_tasks(cur):
    result = cur.execute("SELECT * FROM list")
    rows = result.fetchall()
    tasks = []
    
    for row in rows:
        task = {"id" : row[0], "task" : row[1], "is_done" : row[2]}
        tasks.append(task)
        
    return tasks
    

print("welcome to TO DO LIST !!!")
cur, con = data_base_connection()
main_loop = True
while main_loop:
    user_request = welcome()
    if user_request == 1:
        tasks = show_all_tasks(cur)
        print(tasks)
    elif user_request == 2:
        adding_task(cur, con)
    elif user_request == 3:
        deleting_task(cur, con)
    elif user_request == 4:
        main_loop = False

