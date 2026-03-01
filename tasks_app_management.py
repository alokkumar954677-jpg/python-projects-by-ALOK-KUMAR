def task():
    tasks=[]
    print("==========TODY TASK MANAGEMENT APP========")
    today=int(input("how many tasks="))
    for i in range(1,today+1):
        name=input(f"enter task name=")
        tasks.append(name)
    print(f"======today task======= \n{tasks}")
    while True:
        oprition=int(input(f"enter 1-add\n2-updated\n3-delet\n4-viwe\n5-exit\n"))
        if oprition==1:
          add=input("enter add  task=")
          tasks.append(add)
          print(f"your task is add succesfully={tasks}")
        elif oprition==2 :
            updated=input('enter task to updeted=')
            if updated in tasks:
                up=input("enter nwe task today=")
                a=tasks.index(updated)
                tasks[a]=up
                print(f"updeted task is succesfully={tasks}")
        elif oprition==3:
            delet=input('enter you delet task=')
            if delet in tasks :
                re=tasks.index(delet)
                del tasks[re]
                print(f"delet your task is succesfully={tasks} ")
        elif oprition==4:
            print(f"today total tasks{tasks}")
        elif oprition==5:
            print('*******TODAY TASK TO COLESD ******')
            break
        else:
            print("enter tasks is inviled")

task()