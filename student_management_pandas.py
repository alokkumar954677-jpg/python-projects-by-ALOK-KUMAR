import pandas as pd 
student=[]
while True:
    choice=int(input("1 ADD STUDENT=\n 2 UPDATE STUDENT=\n 3 DELETE STUDENT=\n 4  VIEW STUDENT=\n 5 SEARCH STUDENT=\n 6 EXIT=\n ENTER YOUR CHOICE="))
    if choice==1:
          roll=int(input(" enter student roll number="))
          name=input("enter student name=")
          age=int(input("enter student age="))
          student.append((roll,name,age))
          print(" add student succssfully")
    elif choice==2:
        new=int(input("enter student roll number="))
        for i in range(len(student)):
            if student[i][0]==new:
                roll=int(input(" enter student roll number="))
                name=input("enter student name=")
                age=int(input("enter student age="))
                student[i]=(roll, name,age)
                print(" student update succssfully")
                break
        else:
            print("invalid student roll number")
    elif choice==3:
        delete=int(input("enter delete student roll number="))
        for i in student:
            if delete==i[0]:
                student.remove(i)
                print("student delete successfully")
                break
        else :
            print("enter student roll number invalid")
    elif choice==4:
        show=pd.DataFrame(student,columns=["STUDENT ROLL NUMBER",  "STUDENT NAME",  "STUDENT AGE"])
        print(show)
    elif choice==5:
        find=int(input("enter student roll number="))
        for i in student:
            if i[0]==find:
                print("roll numbwer=",i[0])
                print("student name=",i[1])
                print("student age=",i[2])
                break
        else :
            print(" invaild student roll number")
    elif choice==6:
        print("===thanks for use my code ===")
        break
