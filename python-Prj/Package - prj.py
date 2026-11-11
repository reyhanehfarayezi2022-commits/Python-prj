import time

class Package:
    def __init__(self , sender , reciver , tracking_code , weight , status):
        self.sender = sender
        self.reciver = reciver
        self.tracking_code = tracking_code
        self.weight = weight
        self.status = status
        self.cost = "0"

    def select_services(self):
        print("-+-+-+-+-+-+"*10)
        time.sleep(2)
        select = str(input("\nEnter : ( Show Info / Change Status / Calculate Cost / Exit )"))
        print("-+-+-+-+-+-+"*10)
        if select == "Show Info":
            time.sleep(2)
            return self.show_info()
        elif select == "Change Status":
            time.sleep(2)
            return self.change_status()
        elif select == "Calculate Cost":
            time.sleep(2)
            return self.calculate_cost()
        elif select == "Exit":
            time.sleep(2)
            return self.exit()
        else:
            time.sleep(2)
            print("\nInvalid Choice. Try Again.")
            for i in range(0,4):
                time.sleep(1)
                print((".\t" + "*\t")*7)
            return self.select_services()
        
    def show_info(self):
        time.sleep(2)
        print("-+-+-+-+-+-+\t"*3 + " Info " + "\t-+-+-+-+-+-+"*3)
        info = {"Sender" : self.sender,
                "Reciver" : self.reciver,
                "Tracking Code" : self.tracking_code,
                "Weight" : self.weight,
                "Status" : self.status,
                "Cost" : self.cost}
        time.sleep(1)
        print(f"\n{info}")
        for i in range(0,4):
            time.sleep(1)
            print((".\t" + "*\t")*7)
        return self.select_services()
    
    def change_status(self):
        print("-+-+-+-+-+-+\t"*3 + " Status Change : " + "\t-+-+-+-+-+-+"*3)
        new_status = str(input("\n***\tchange status :\t( registered , sent , in_transit , delivered , canceled , Exit )\t"))

        time.sleep(2)

        if self.status == "registered" and (new_status == "sent" or new_status == "in_transit" or new_status == "cancelled" or new_status == "cancelled"):
            self.status = new_status
        elif self.status == "sent" and (new_status == "in_transit" or new_status == "delivered" or new_status == "cancelled" ):
            self.status = new_status
        elif self.status == "in_transit" and (new_status == "delivered" or new_status == "cancelled"):
            self.status = new_status
        elif new_status == "Exit":
            return self.select_services()
        else:
            print("\n***\tInvaid Status.Try Again.")
            return self.change_status()
        
        print(f"\nStatus : {self.status}")
        for i in range(0,4):
            time.sleep(1)
            print((".\t" + "*\t")*7)
        return self.select_services()
        
    def calculate_cost(self):
        kg = 1000
        if self.weight > 0 and self.weight < 500:
            self.cost = f"50000 t"
        elif self.weight >= 500 and self.weight < 1 * kg:
            self.cost = f"70000 t"
        elif self.weight >= 1 * kg and self.weight < 2 * kg:
            self.cost = f"100000 t"
        elif self.weight >= 2 * kg and self.weight < 5 * kg:
            self.cost = f"150000 t"
        elif self.weight >= 5 * kg:
            self.cost = f"200000 t"
        else:
            print("Invalid Weight.")

        print(f"\n**\tWeight : {self.weight}\n**\tCost : {self.cost}")
        time.sleep(3)
        for i in range(0,4):
            time.sleep(1)
            print((".\t" + "*\t")*7)
        return self.select_services()
            
    def exit(self):
        print("\n\t*** \tExited\t ***")
        time.sleep(3)
        return "\t***"*30
p1 = Package("Reyhaneh Farayezie" , "Elaheh Farayezie" , 1001 , 5 , "sent")
print(p1.select_services())