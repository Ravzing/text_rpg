import csv
import re
import sys
import os

from game_menu import Menu
from characters_info import Character

STORAGE = "account.csv"
PATTERN = r"^[a-zA-Z0-9_]+$"


class AccountRegistry:
    def __init__(self):
        self.characters_name = []
        self.username = []
        self.password = []
        self.storage = STORAGE
        self.load_accounts()
        self.game_menu = Menu(self)

    def _write_csv_header(self, writer) -> None:
        writer.writerow(["username", "password", "character_name"])

    def _write_csv_row(self, writer) -> None:
        writer.writerow(
            [self.username[-1], self.password[-1], self.characters_name[-1]]
        )

    def _load_row(self, row) -> None:
        self.username.append(row[0])
        self.password.append(row[1])
        self.characters_name.append(row[2])

    def load_accounts(self):
        try:
            with open(self.storage, mode="r", newline="") as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) == 3:
                        self._load_row(row)
        except FileNotFoundError:
            print(f"File {self.storage} not found. Creating a new one.")
            with open(self.storage, mode="w", newline="") as file:
                pass

    def save_account(
        self, new_username: str, new_password: str, new_character_name: str
    ):
        file_exists = os.path.exists(self.storage)
        with open(self.storage, mode="a", newline="") as file:
            writer = csv.writer(file)
            if not file_exists:
                self._write_csv_header(writer)
            self._write_csv_row(writer)

    def inputs_for_register(self) -> str:
        new_username = self.get_unique_username()
        new_password = self.get_validation("Enter your password: ")
        new_character_name = self.get_unique_characters_name()
        return new_username, new_password, new_character_name

    def append_for_register(
        self, new_username: str, new_password: str, new_character_name: str
    ) -> None:
        self.username.append(new_username)
        self.password.append(new_password)
        self.characters_name.append(new_character_name)

    def character_save_register(self, new_character_name: str) -> None:
        new_character = Character(new_character_name)
        new_character.save_to_csv()

    def register(self) -> None:
        new_username, new_password, new_character_name = self.inputs_for_register()
        self.append_for_register(new_username, new_password, new_character_name)
        self.save_account(new_username, new_password, new_character_name)
        print("Account created successfully!")
        self.character_save_register(new_character_name)

    def is_valid_input(self, validation: str) -> bool:
        return re.match(PATTERN, validation)

    def get_unique_username(self) -> str:
        return self._get_unique_value(
            "Enter your username: ",
            self.username,
            "Username already exists! Please try again.",
        )

    def get_unique_characters_name(self) -> str:
        return self._get_unique_value(
            "Enter your character's name: ",
            self.characters_name,
            "Character name already exists! Please try again.",
        )

    def _get_unique_value(
        self, prompt: str, existing_values: list, error_message: str
    ) -> str:
        while True:
            value = self.get_validation(prompt)
            if value not in existing_values:
                return value
            print(error_message)

    def get_validation(self, prompt: str) -> str:
        while True:
            value = input(prompt)
            if self.is_valid_input(value):
                return value
            else:
                print(
                    "Invalid input. Please avoid spaces, commas, and special characters."
                )

    def _validate_login(self, username: str, password: str) -> bool:
        if username in self.username:
            index = self.username.index(username)
            return self.password[index] == password
        return False

    def login(self) -> None:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if self._validate_login(username, password):
            character_name = self.characters_name[self.username.index(username)]
            player_character = Character.load_character(character_name)
            if player_character:
                print("login successful")
                self.game_menu.open_game_menu(player_character)
        else:
            print("Invalid username or password.")

    def menu(self) -> None:
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
