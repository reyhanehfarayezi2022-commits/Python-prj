import time
class Patient:
    def __init__(self , fname : str, lname : str, age : int , patiend_id : int , balance : int ):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.patient_id = patiend_id
        self.balance = balance
        self.p_file = "list of patients.txt"

        self.bill_pay_times = 0
        self.charged_times = 0

    def services(self):
        choice = str(input("\n\t* Enter : ( Show Info / Add Charge / Pay Bill / check Balance / Exit )"))
        if(choice == "Show Info"):
            time.sleep(1.5)
            return self.show_info()
        
        elif(choice == "Add Charge"):
            time.sleep(1.5)
            return self.add_charge()
        
        elif(choice == "Pay Bill"):
            time.sleep(1.5)
            return self.pay_bill()
        
        elif(choice == "Check Balance"):
            time.sleep(1.5)
            return self.check_balance()
        
        elif(choice == "Exit"):
            time.sleep(1.5)
            return self.exit()
        
        else:
            time.sleep(1.5)
            print(f"\n\t *** {choice} was an incorrect choice. try again. *** ")
            time.sleep(3.5)
            return self.services()

    def login(self):

        print("-=-=-=-=-=-=-="*10)
        print("-=-=-=-=-=-=-="*4 + " Enter Info : " + "-=-=-=-=-=-=-="*5)
        time.sleep(1.5)
        username = str(input("\n***\tEnter Username :\t"))
        print("-=-=-=-=-=-=-="*10)
        time.sleep(1.5)
        enter_age = int(input("\n***\tEnter age :\t"))
        print("-=-=-=-=-=-=-="*10)
        time.sleep(1.5)
        enter_pi = int(input("\n***\tEnter patient id :\t"))
        print("-=-=-=-=-=-=-="*10)

        if (username == str(self.fname + " " + self.lname)) and (enter_age == self.age) and ( enter_pi == self.patient_id):
            time.sleep(1.5)
            print("-=-=-=-=-=-=-="*10)    
            print("\n***\tSuccessful Login\t***")
            time.sleep(1.5)
            self.services()
        else:
            while(username != str(self.fname + " " + self.lname)) or (enter_age != self.age) or ( enter_pi != self.patient_id):
                print("\n***\tUnsuccessful Login\t***")
                time.sleep(1.5)
                self.login()


    def show_info(self):
        print("-=-=-=-=-=-=-="*10)
        print("\n***\t*** Info : ***\t***")

        info = {"First name " : [self.fname] ,
                 "Last name" : [self.lname] ,
                   "Age" : [self.age],
                   "Patient ID" : [self.patient_id] ,
                   "Balance" : [self.balance]
                   }
        print(info)
        print("-=-=-=-=-=-=-="*10)
        time.sleep(1.5)
        self.services()

    def add_charge(self):
        print("-=-=-=-=-=-=-="*10)
        print("\n***\t*** Amount : ***\t***")

        charge = int(input("Amount : \t"))
        self.balance += charge
        self.charged_times += 1

        print(f"\n***\t Balance : {self.balance} \n***\t Amount : {charge}")
        print("-=-=-=-=-=-=-="*10)
        time.sleep(1.5)
        self.services()
        
    def pay_bill(self):
        print("-=-=-=-=-=-=-="*10)
        print("\n***\t*** Pay Bills : ***\t***")

        time.sleep(1.5)

        bills = int(input(f"Pay :\t"))
        self.balance = self.balance - bills
        self.bill_pay_times += 1

        time.sleep(1.5)

        print(f"\n***\t Balance : {self.balance} \n***\t Payed : {bills}$")
        print("-=-=-=-=-=-=-="*10)
        time.sleep(1.5)
        self.services()

    def check_balance(self):
        print("-=-=-=-=-=-=-="*10)
        b_info = f"Balance : {self.balance}"
        print(b_info)
        print("-=-=-=-=-=-=-="*10)
        time.sleep(1.5)
        self.services()

    def save_info(self):
        with open(self.p_file , "w") as file:
            patients = file.write(str(list_of_patients))
        return
    
    def exit(self):
        time.sleep(1.5)
        self.save_info()
        print("Done")
        exit

print("-=-=-=-=-=-=-="*10)
count = int(input("\n\t*** Enter Number of Patients :\t"))
list_of_patients = {}
for i in range(1 , count + 1):
    list_of_patients.setdefault(f"patient{i}" , Patient(str(input(f"\npatient{i} First Name : ")) , str(input(f"\npatient{i} Last Name : ")) , int(input(f"\npatient{i} Age : ")) , int(input(f"\npatient{i} Patient ID : ")) , str(input(f"\npatient{i} Balance : "))))

for i in range(1 , count + 1):
   print(list_of_patients[f"patient{i}"].login())
   