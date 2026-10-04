import sqlite3
import time

def welcome():
    print("please press any botton to continue...")
    print("for watching your tasks please write 1 ")
    print("for adding new task to your plan please write 2 ")
    print("for Delete the task press 3")
    print("EXIT 4")
    print("for mark your task as done write 5")
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
    connect = sqlite3.connect("to_do_list.db")
    cursor = connect.cursor()
    
    
    cursor.execute("""
                CREATE TABLE IF NOT EXISTS list (
                    id INTEGER PRIMARY KEY,
                    task TEXT,
                    is_done TEXT
                    )
                """)
    connect.commit()
    return cursor, connect
    
    
    
def adding_task(cursor, connect, is_doneyet="no"):
    new_task = input("write your task: ")
    cursor.execute("INSERT INTO list (task, is_done) VALUES (?,?)", (new_task, is_doneyet))
    print(f"your task has succesfully added to your list")
    connect.commit()


def deleting_task(cursor, connect):
    loop_trying = True
    print(show_all_tasks(cursor))
    
    while loop_trying:
        try:
            delete_id_request = int(input("please write the task id that you want to delete: "))
            cursor.execute("DELETE FROM list WHERE id = ?", (delete_id_request,))
            if cursor.rowcount > 0:
                connect.commit()
                loop_trying = False
                print(f"you have succesfully deleted the {delete_id_request} id")
            else:
                print("this id does not exist!")
        except:
            print("please write a VALID NUMBER !")
            
    
def show_all_tasks(cursor):
    result = cursor.execute("SELECT * FROM list")
    rows = result.fetchall()
    tasks = []
    
    for row in rows:
        task = {"id" : row[0], "task" : row[1], "is_done" : row[2]}
        tasks.append(task)
        
    return tasks

def mark_as_done(cursor, connect):
    print(show_all_tasks(cursor))
    time.sleep(0.5)
    check = True
    while check:
        try:
            request = int(input("please write the task id that you would like to set as DONE: "))
            check = False
        except ValueError:
            print("please enter a valid number !")
            time.sleep(2)
    
    task_done = cursor.execute("SELECT task FROM list WHERE id =(?) ", (request,))
    
    result = task_done.fetchone()
    
    if result is None:
        print("sorry we coulnt find your id !")
        return
    
    cursor.execute("UPDATE list SET is_done = 'DONE' WHERE id =(?)", (request,))
    
    if cursor.rowcount > 0:
    
        connect.commit()
        
        print(f"you have succesfully DONE your {result[0]} task")
    else:
        print("sorry we couldn't found your id!")
    
    
    
    
    


print("welcome to TO DO LIST !!!")
cursor, connect = data_base_connection()
main_loop = True
while main_loop:
    user_request = welcome()
    if user_request == 1:
        tasks = show_all_tasks(cursor)
        print(tasks)
    elif user_request == 2:
        adding_task(cursor, connect)
    elif user_request == 3:
        deleting_task(cursor, connect)
    elif user_request == 4:
        main_loop = False
    elif user_request == 5:
        mark_as_done(cursor, connect)

