from getpass import getpass
print("=====WELCOM TO DISTAL BANK=====")
login=getpass("ENTER BANK ID=")
print("ID is hidden, type and press enter")
if login=="125":
 class bank:
    def __init__(self,name,balance,account):
        self.name=name
        self.balance=balance
        self.account=account
        self.pasbook=[]
    def creat(self):
        print("NAME \t\t BALANCE \tACCOUNT NUMBER")
        print(f"{self.name} \t\t{self.balance}\t\t{self.account}")

    def display(self):
            if account==self.account:
                 print("NAME \t\t BALANCE \tACCOUNT NUMBER")
                 print(f"{self.name} \t\t{self.balance}\t\t{self.account}")
            else:
                print("WRONG ACCOUNT NUMBER PLEASE TRY AGAIN")
     
    def withdraw(self):
        amount=int(input("enter withdraw amount="))
        self.pasbook.append(f"TODAY WITHDRAW=={self.account}")
        if amount<=self.balance:
            self.balance-=amount 
            print("NAME \t\t BALANCE \tACCOUNT NUMBER")
            print(f"{self.name} \t\t{self.balance}\t\t{self.account}")
        else:
            print("not posible")

    def deposit(self):
        amount=int(input("enetr deposit amount="))
        self.pasbook.append(f"TODAY DEPOSIT={self.account}")
        if amount<0 :
            print("not posible")
        else:
            self.balance+=amount
            print("NAME \t\t BALANCE \tACCOUNT NUMBER")
            print(f"{self.name} \t\t{self.balance}\t\t{self.account}")
    def pasbooks(self):
            for i in self.pasbook:
                print(i)

 mylist=[]
 while True:
    m=int(input("1 CREATE BANK ACCOUNT\n2 DEPOSIT AMOUNT\n3 WITHDRAW AMOUNT\n4 CHECK BALANCE\n5 CHECK PASBOOK\n6 UPDATE ACOUNT\n7 DELET ACCOUNT\n 8 EXIT BANK\n ENTER YOUR CHOISE="))
    if m==1:
        name=input("ENTER YOUR NAME=")
        balance=int(input("ENTER YOUR BALANCE="))
        account=int(input("ENTER YOUR ACCOUNT NUMBER="))
        if account<0:
            print(" CEREAT ACCOUNT NUMBER IS WRONG")
            break
        else:
          s1=bank(name,balance,account)
          mylist.append(s1)
          s1.creat()

    elif m==2:
        count=0
        while count<3:
            account=int(input("ENTER YOUR ACCOUNT NUMBER="))
            for i in mylist:
                if  i.account==account:
                   i.deposit()
                   break
            else:
                count+=1
                print(" WRONG ACCOUNT NUBER PLEASE TRY AGAIN")
                continue
            break
        if count==3:
         print("LOCK YOUR ACCOUNT PLEASE CONTACT THE BANK")
         print("=====THANKS TO MY DISTAL BANK HOLDER=====")
    elif m==3:
        count=0
        while count<3:
            account=int(input("ENTER YOUR ACCOUNT NUMBER="))
            for i in mylist:
                if i.account==account:
                   i.withdraw()
                   break
            else:
                count+=1
                print(" WRONG ACCOUNT NUMBER PLEASE TRY AGAIN")
                continue
            break
        if count==3:
          print("LOCK YOUR ACCOUNT PLEASE CONTACT THE BANK")
          print("=====THANKS TO MY DISTAL BANK HOLDER =====")
    elif m==4:
        count=0
        while count<3:
            account=int(input("ENTER YOUR ACCOUNT NUMBER="))
            for i in mylist:
                if i.account==account:
                    i.display()
                    break
            else:
                count+=1
                print(" WRONG ACCOUNT NUMBER PLEASE TRY AGAIN")
                continue
            break
        if count==3:
            print("LOCK YOUR ACCOUNT PLEASE CONTACT THE  BANK")
            print("=====THANKS MY DISTAL BANK HOLDER===== ")
    elif m==5:
        count=0
        while count <3:
            account=int(input("ENTER YOUR ACCOUNT NUMBER="))
            for i in mylist:
                if i.account==account:
                  i.pasbooks()
                  break
            else:
                count+=1
                print(" WRONG ACCOUNT NUMBER PLEASE TRY AGAIN")
                continue
            break
        if count==3:
            print("LOCK YOUR ACCOUNT PLEASE CONTACT BANK")


    elif m==6:
        count=0
        while count<3:
            account=int(input("ENTER ACCOUNT NUMBER="))
            for i in mylist:
                if i.account==account:
                    name=input("ENTER UPDATE YOUR NAME=")
                    account=int(input("ENTER UPDATE YOUR ACCOUNT NUMBER="))
                    i.name=name
                    i.account=account
                    i.display()
                    print("UPDATE ACCOUNT SUCCESSFUL")
                    break
            else:
                print("WRONG YOUR ACCOUNT NUMBER")
                continue
            break
        if count==3:
            print("LOCK YOUR ACCONT PLEASE CONTACT THE  BANK")
            print("=====THANKS MY DISTAL BANK HOLDER===== ")
    elif m==7:
        count=0
        while count<3:
            acc=int(input("ENTER DELET ACCOUNT NUMBER="))
            for i in mylist:
                if i.account==acc:
                    mylist.remove(i)
                    print("DELETED ACCOUNT SUCCESSFUL")
                    break
            else:
                count+=1
                print("WRONG ACCOUNT NUMBER PLEASE TRY AGAIN")
                continue
            break
        if count==3:
           print("LOCK YOUR ACCOUNT PLEASE CONTACT THE BANK")

    elif m==8:
         print("===THANKS SBI COUNT===")
         break

else:
    print("PLEASE LOGIN BANK THEN WORK")