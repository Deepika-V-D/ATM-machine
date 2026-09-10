print("======ATM MECHINE========")
balance=10000
#set pin
#enter pin global , local

for i in range(1,5):
    pin=int(input("set your 4 digit pin:"))
    cor_pin = 1234 #1
    print("pin set successfully")
    #entered_pin=int(input("enter your pin:"))
    if pin== cor_pin:# pin == 1
        print("pin is correct")
        print("\n=====ATM MENU======")
        print("1.withdraw")
        print("2.depoist")
        print("3.checking balance")
        print("4.update pin")
        print("5.exit")
        choice=int(input("enter your choice:"))
        if choice==1:
             amount=int(input("enter your amount"))
             if amount<=balance:
                 balance -= amount# balance = balance - amount
                 print("current balance",balance)
             else:
                 print("insuffient balance")
        elif choice==2:
             amount=int(input("enter your amount"))
             if amount<=balance:# amount = 200, balance 10,000
                 balance=amount+balance
                 print("current balance",balance)
             else:
                 print("insuffient balance")
        elif choice==3:
             print("checking balance",balance)
        elif choice==4:
             new_pin=int(input("enter the  new pin"))
             #new_pin == pin
             cor_pin = new_pin # cor_pin = 1
             print(" pin change successfully")
        elif choice==5:
             print("thank you for using ATM")
             print("please collect your card")
             break
        else:
            print("invalid choice")
             
             
    else:
        print("pin incorrect")
        break
    
     

                 
        
