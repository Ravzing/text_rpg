import csv
import re
import sys
import os

from game_menu import Menu
from characters_info import Character

storage = "account.csv"

class AccountRegistry:
    def __init__(self):
        self.characters_name = []
        self.username = []
        self.password = []
        self.storage = storage
        self.load_accounts()
        self.game_menu = Menu(self)
        
    def load_accounts(self):
        try:
            with open(self.storage, mode='r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) == 3:
                        self.username.append(row[0])
                        self.password.append(row[1])
                        self.characters_name.append(row[2])
        except FileNotFoundError:
            print(f"File {self.storage} not found. Creating a new one.")
            with open(self.storage, mode='w', newline='') as file:
                pass
        
    def save_account(self, username, password, character_name):
        file_exists = os.path.exists(self.storage)
        with open(self.storage, mode='a', newline='') as file: 
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(["username", "password", "character_name"])
            writer.writerow([username, password, character_name])
          
    def register(self):
        new_username = self.get_unique_username()
        new_password = self.get_validation("Enter your password: ")
        new_character_name = self.get_unique_characters_name()
        self.username.append(new_username)
        self.password.append(new_password)
        self.characters_name.append(new_character_name)
        self.save_account(new_username,new_password,new_character_name)
        print("Account created successfully!")
        new_character = Character(new_character_name)
        new_character.save_to_csv()
        
    def is_valid_input(self, validation):
        pattern = r'^[a-zA-Z0-9_]+$'
        return re.match(pattern, validation)

    def get_unique_username(self):
        while True:
            new_username = self.get_validation("Enter your username: ")
            if new_username not in self.username:
                return new_username
            print("Username already exists! Please try again.")
    
    def get_unique_characters_name(self):
        while True:
            new_character_name = self.get_validation("Enter your character's name: ")
            if new_character_name not in self.characters_name:
                return new_character_name
            print("Character name already exists! Please try again.")
    
    def get_validation(self, prompt):
        while True:
            value = input(prompt)
            if self.is_valid_input(value):
                return value
            else:
                print("Invalid input. Please avoid spaces, commas, and special characters.")
        
        
    def login(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if username in self.username:
            index = self.username.index(username)
            if self.password[index] == password:
                print("Login successful!")
                character_name = self.characters_name[index] 
                player_character = Character.load_character(character_name)
                if player_character:
                    self.game_menu.open_game_menu(player_character)
                return 
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
                print("Thanks for playing till next time!")
                sys.exit()
            else:
                print("Invalid choice!")