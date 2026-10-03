task = {}
def main():
    print("Welcome to ToDoList! | Add tasks:1, Remove tasks:2, View:3, Reset:4 , Exit: 5")
    def resettask():
       global task
       task = {}
       main()
    def addtask():
        while True:
          try: 
            n = int(input("How many tasks do you want to add:"))
            break
          except ValueError: 
             print("Enter a whole number: ")
        for i in range(n):
            print(f"{i}__")
            key = input("Enter the topic/title:")
            value = input("Enter the subject of that title/topic:")
            task[key] = value     
        main()    
    def viewtask():
        print(task)
        main()  
    def removetask():
       print(task)
       key = input("Enter the Topic/Title to remove:")
       removed = task.pop(key, None)
       if removed!= None:
          print(f"Successfully removed {removed}")
       else:
          print(f"Topic '{removed}' not found.")
       main()

    do = int(input(":"))
    if do == 1:
        addtask()     
    elif do ==3:
       viewtask()
    elif do == 2:
       removetask()
    elif do ==4:
       resettask()  
    else:
       exit
main()             

