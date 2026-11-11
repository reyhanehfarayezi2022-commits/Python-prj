class Bank_Account :
    def __init__(self, fname , lname , password , Initial_balance , Account_type , Account_ID , age , Balance):
        self.fname = fname
        self.lname = lname
        self.password = password
        self.Initial_balance = Initial_balance
        self.Account_type = Account_type
        self.Account_ID = Account_ID
        self.age = age
        self.Balance = Balance


    def service(self):
        services = str(input("\n\tServices \t( Amount / Edit info / Check info / Exit ):\t"))
        if services == "Amount":
            return self.amount_setting()
        elif services == "Edit info":
            return self.edit()
        elif services == "Check info":
            return self.display2()
        elif services == "Exit":
            return self.exit()
        else:
            print("\n\t*** Try again ***")
            return self.service()
        
    def user_entry(self):
        username = f"{self.fname} {self.lname}"
        user = str(input("\nEnter Username : \t"))
        psw = int(input("\nEnter Password : \t"))

        import time
        time.sleep(2)

        if (username == user) & (psw == self.password):
            time.sleep(2)
            print("\t===========\t"*2 + "Successful Login" + "\t===========\t"*2)
            time.sleep(3)
            for i in range (0,10):
                print("\n\t*\t*\t*"*10)
            self.display()
            print("*=*=*="*14)
            time.sleep(3)

            for i in range(0,4):
                print("\t===\t===\t==="*4)
                time.sleep(1.5)

            self.service()
            
        else:
            while(user != username ) or (psw != self.password):
                print("\t===========\t"*2 + "Unsuccessful Login" + "\t===========\t"*2)
                time.sleep(3)
                for i in range (0,10):
                    print("\t*\t*\t*"*14)
                    self.user_entry()
            

    def edit(self):
        choice = str(input(" fname \n lname \n password \n Initial_balance \n Account_type \n Account_ID \n age \n Balance :\t"))
        if choice == "fname":
            self.fname = str(input("\n Edit first name : \t"))
        elif choice == "lname":
            self.lname = str(input("\n Edit last name : \t"))
        elif choice == "password":
            self.password = int(input("\n Edit password : \t"))
        elif choice == "Initial balance":
            self.Initial_balance = int(input("\n Edit initial balance : \t"))
        elif choice == "Account type":
            self.Account_type = str(input("\nEdit account type : \t"))
        elif choice == "Account_ID":
            self.Account_ID = int(input("\nEdit account id : \t"))
        elif choice == "age":
            self.age = int(input("\nEdit age : \t"))
        elif choice == "Balance" :
            self.Balance == int(input("\nEdit Balance : \t"))
        else:
            print("\n\t*** Try again ***")
            self.edit()
        self.service()

        

    def amount_setting(self):
        choice = str(input("\n * deposit \t * withdraw \t ?"))
        if choice == "deposit":
            return self.deposit()
        elif choice == "withdraw":
            return self.withdraw()
        

    def deposit(self):
        self.amount = 0
        self.amount = int(input("\n*\tEnter amount :\t"))
        self.Balance += self.amount
        print(f" deposit amount : \t{self.amount}")
        print(f"Balance : \t{self.Balance}")
        self.service()

    def withdraw(self):
        self.amount = 0
        self.amount = int(input("\n*\tEnter amount :\t"))
        self.Balance -= self.amount
        print(f"\n*\twithdraw amount : \t{self.amount}")
        print(f"\n*\tBalance : \t{self.Balance}")
        self.service()

    def display(self):
        display_balance = {
            "initial balance " : [self.Initial_balance],
            "balance " : [self.Balance],
            "Account ID " : [self.Account_ID],
            "Account Type " : [self.Account_type]
        }
        print(display_balance)

    
    def display2(self):
        display_balance = {
            "initial balance " : [self.Initial_balance],
            "balance " : [self.Balance],
            "Account ID " : [self.Account_ID],
            "Account Type " : [self.Account_type]
        }
        print(display_balance)
        self.service()

    
    def exit(self):
        print("\t***\t***\t***"*6)
        print("\t***\t***\t***"*6)
        print("\t***\t***\t***"*6)
server1 = Bank_Account("Reyhaneh", "Farayezie" , 1364442051 , 4000000 , "normal" , 404311194 , 19 , 4000000)
print(server1.user_entry())