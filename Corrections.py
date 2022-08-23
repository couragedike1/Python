import random as rd

#--- creating bank object
class GreyTrustBank():
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age
        self.account_num = rd.randrange(0000000000, 9999999999)
        self.acc_bal = 0 

    #- accessing class attributes
    @property
    def get_id(self):
        return self.id

    @property
    def get_name(self):
        return self.name

    @property
    def get_age(self):
        return self.age

    #- handling balance, deposit and withdraw
    def balance(self):
        return f"Your account balance is: ${self.acc_bal}\n"

    def deposit(self, value):
        self.acc_bal += int(value)
        print(f"Transaction Sucessful!\nBalance: ${self.acc_bal}\n")

    def withdraw(self, value):
        if self.acc_bal >= int(value):
            self.acc_bal -= int(value)
            print(f"Transaction Successful!\nBalance: ${self.acc_bal}\n")
        else:
            print(f"Insufficient Funds!\nCurrent Balance: ${self.acc_bal}\n")


#--- creating customer instance
print("* Hello! To register an account, please provide;\n- A Custom ID, Full Name & Age.\n")
user_id = input("Enter custom ID here: ")
user_name = input("Enter name here: ")
user_age = input("Enter age here: ")
customer = GreyTrustBank(user_id, user_name, user_age)
 

#--- bank menu function
print("* Welcome to GreyTrust Bank!\n")

›››def menu_gtb():
    while True:
        print("> ENTER 1 to view Account Details\n> ENTER 2 to Make a Deposit\n> ENTER 3 to Withdraw an amount\n> ENTER 4 to Check Account Balance\n> ENTER 0 to Exit!")
        user_input = int(input("Enter option here: "))

        if user_input == 1:
            print(f"- {customer.get_name}, Account: {customer.account_num}\n")

        elif user_input == 2:
            amount = input("Enter amount here: ")
            customer.deposit(amount)

        elif user_input == 3:
            amount = input("Enter amount here: ")
            customer.withdraw(amount)

        elif user_input == 4:
            print(customer.balance())

        elif user_input == 0:
            print("Thank you for banking with us!")
            break


#--- running program
menu_gtb()
