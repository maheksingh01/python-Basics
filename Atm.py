class Atm:
    
    #constructor
    
    def __init__(self):
        
        self.pin = ""
        self.balance = 0
        
        self.menu()
    
    def menu(self):
        user_input = input("""
                           Hello how would you like to proceed??
                           1. Enter 1 to create PIN
                           2. Enter 2 to Deposit
                           3. Enter 3 to Withdraw
                           4. Enter 4 to Check Balance
                           5. Enter 5 to EXIT
                           """)
        if user_input == "1":
            print("Create PIN")
        elif user_input == "2":
            print("Deposit")
        elif user_input == "3":
            print("Withdraw")
        elif user_input == "4":
            print("Check Balance")
        elif user_input == "5":
            print("EXIT")
        else:
            print("Invalid Input")