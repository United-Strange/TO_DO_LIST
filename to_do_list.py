import sqlite3
import time

def welcome():
    print("please press any botton to continue...")
    print("for watching your tasks please write 1 ")
    print("for adding new task to your plan please write 2 ")
    print("for Delete the task press 3")
    print("EXIT 4")
    user_request = int(input())

def adding_task():
    new_task = input("write your task: ")
    task_time = time.localtime
    ### add the task to SQLITE3
    print(f"your task has succesfully added to your list in this {task_time}")


def deleting_task():
    loop_trying = True
    #SQL have yo show the all tasks
    while loop_trying:
        try:
            delete_id_request = int(input("please write the task id that you want to delete: "))
            loop_trying = False
        except:
            print("please write a VALID NUMBER !")
            loop_trying = True
    #SQL have to delete that id
def show_all_tasks():
    pass
    #SQL HAVE TO SHOW ALL TASKS

print("welcome to TO DO LIST !!!")
main_loop = True
while main_loop:
    user_request = welcome()
    if user_request == 1:
        show_all_tasks
    elif user_request == 2:
        adding_task
    elif user_request == 3:
        deleting_task