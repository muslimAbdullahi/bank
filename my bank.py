#-*-coding:utf8;-*-
#qpy:conso
import time
def exit_home():
    time.sleep(0.95)
    print("Thanks for visiting Abcoder bank")
    exit()
    
print("_________Welcome to Abcoder Bank________")
time.sleep(0.95)
print("_________________________________")
time.sleep(0.95)
print("1:Create account\n2: Check balance \n 3:Withdraw\n4:Buy Airtime\n5:exit")
enter_number=int(input("Enter number"))
acc_bal="0"
def create_account():
    if enter_number== 1:
        first_name=input(" what your surname:")
        time.sleep(0.95)
        last_name=input(" what your name:")
        time.sleep(0.95)
        total_name= first_name +"  "+last_name
        create_pin=int(input(" create bank pin:"))
        print( f" mrs" +total_name+" " +"your bank pin is"+" "+str(create_pin))
        acc_number="0153573366"
        print("Wait a while for your account number")
        time.sleep(1.25)
        print(f"Your account number is"+" "+acc_number)
        create_account()
        back=int(input(" press 5 to exit:"))
        if back ==5:
          exit_home()
    elif enter_number==2:
        def check_bal():
            your_bal=int(input("enter your acc pin"))
            if your_bal== create_pin:
                print(acc_number+" "+"is emoty")
            else:
                print("you dont have account with us")
            check_bal()

          
            
	 

    
    
