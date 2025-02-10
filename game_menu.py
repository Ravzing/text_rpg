from account_storage import AccountRegistry
from enemies_list import Enemy
from characters_info import Character
from game_combat import Combat
import sys


class Menu:
    def __init__(self, account_registry: AccountRegistry) -> None:
        self.account_registry = account_registry
        self.current_character = None

    def menu(self) -> None:
        while True:
            print("1. Register")
            print("2. Login")
            print("3. Exit")
            choice = input("Enter your choice: ")
            self._menu_choice(choice)

    def _menu_choice(self, choice: str) -> None:
        if choice == "1":
            self.account_registry.register()
        elif choice == "2":
            self.account_registry.login()
        elif choice == "3":
            print("Thanks for playing till next time!")
            sys.exit()
        else:
            print("Invalid choice!")

    def open_game_menu(self, character) -> None:
        self.current_character = character
        while True:
            print("\nGame Menu:")
            print("1. Character")
            print("2. Map")
            print("3. Log out")
            choice = input("Choice: ")
            self._open_game_menu_choice(choice)

    def _open_game_menu_choice(self, choice: str) -> None:
        if choice == "1":
            self.character()
        elif choice == "2":
            self.map_menu()
        elif choice == "3":
            print("Logging out...\n")
            self.menu()
            return
        elif choice == "4":
            self.add_stats()
        else:
            print("Invalid choice! Please enter a valid option.")

    def add_stats(self) -> None:
        self.current_character.attack += 20
        self.current_character.armor += 10
        return self.current_character.update_character()

    def character(self) -> None:
        if self.current_character:
            print("\n🎭 Character Info 🎭")
            print(f"Name: {self.current_character.name}")
            print(f"Health: {self.current_character.health}")
            print(f"Armor: {self.current_character.armor}")
            print(f"Attack: {self.current_character.attack}")
            print(f"Woodcutting Level: {self.current_character.woodcutting}")
            print(f"Fishing Level: {self.current_character.fishing}")
            print(f"Mining Level: {self.current_character.mining}")
            print(f"Smithing Level: {self.current_character.smithing}")
        else:
            print("No character data available.")

    def map_menu(self) -> None:
        while True:
            print("\nMap Menu:")
            print("1. Forest")
            print("2. Sea")
            print("3. Cave")
            print("4. Wilderness")
            print("5. Back")
            sub_choice = input("Choice: ")
            self._map_menu_choice(sub_choice)

    def _map_menu_choice(self, sub_choice: str) -> None:
        if sub_choice == "1":
            self.forest()
        elif sub_choice == "2":
            self.sea()
        elif sub_choice == "3":
            self.cave()
        elif sub_choice == "4":
            self.wilderness()
        elif sub_choice == "5":
            self.open_game_menu(self.current_character)
        else:
            print("Invalid choice! Please enter a valid option.")

    def forest(self) -> None:
        print("🌲 Entering the forest...")
        # TODO

    def sea(self) -> None:
        print("🌊 Entering the sea...")

    def cave(self) -> None:
        print("🦇 Entering the cave...")

    def wilderness(self) -> None:
        print("🐺 Entering the wilderness...")
        print("Enemies in area:")
        enemies = Enemy.load_enemies_from_csv()
        for i, enemy in enumerate(enemies):
            print(
                f"{i + 1}: {enemy.name}: Health: {enemy.health}, Armor: {enemy.armor}, Attack: {enemy.attack}"
            )
        while True:
            try:
                choice = int(input("Choose an enemy to fight: ")) - 1
                if 0 <= choice < len(enemies):
                    combat = Combat(self.current_character, self)
                    combat.combat(enemies[choice])
                    break
                else:
                    print("To exit wilderness press enter")
            except ValueError:
                self.map_menu()
