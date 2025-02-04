import csv

storage = "account.csv"

class AccountRegistry:
    def __init__(self):
        self.username = []
        self.password = []
        self.storage = storage
        self.load_accounts()
        
    def load_accounts(self):
        try:
            with open(self.storage, mode='r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) == 2:
                        self.username.append(row[0])
                        self.password.append(row[1])
        except FileNotFoundError:
            print(f"File {self.storage} not found. Creating a new one.")
            with open(self.storage, mode='w', newline='') as file:
                pass
        
    def save_account(self, username, password):
        with open(self.storage, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([username, password])
          
    def register(self):
        new_username = input("Enter your username: ")
        if new_username in self.username:
            print("Username already exists!")
            return
        new_password = input("Enter your password: ")
        self.username.append(new_username)
        self.password.append(new_password)
        self.save_account(new_username,new_password)
        print("Account created successfully!")
        
    def login(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if username in self.username and password in self.password:
            print("Login successful!")
        else:
            print("Invalid username or password.")
            
    def menu(self):
        while True:
            print("1. Register")
            print("2. Login")
            print("3. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.register()
            elif choice == "2":
                self.login()
            elif choice == "3":
                break
            else:
                print("Invalid choice!")
                

def main():
    account = AccountRegistry()
    account.menu()
if __name__ == "__main__":
    main()