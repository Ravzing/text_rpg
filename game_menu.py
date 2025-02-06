class Menu:
    def __init__(self, account_registry):
       self.account_registry = account_registry 
       self.current_character = None
       
    def open_game_menu(self, character):
        self.current_character = character
        while True:
            print("\nGame Menu:")
            print("1. Character")
            print("2. Map")
            print("3. Log out")
            choice = input("Choice: ")
            
            if choice == "1":
                self.character()
            elif choice == "2":
                self.map_menu()
            elif choice == "3":
                print("Logging out...\n")
                self.account_registry.menu()
                return 
            else: 
                print("Invalid choice! Please enter a valid option.")

    def character(self):
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

    def map_menu(self):
        while True:
            print("\nMap Menu:")
            print("1. Forest")
            print("2. Sea")
            print("3. Cave")
            print("4. Back")
            sub_choice = input("Choice: ")
            
            if sub_choice == "1":
                self.forest()
            elif sub_choice == "2":
                self.sea()
            elif sub_choice == "3":
                self.cave()
            elif sub_choice == "4":
                return 
            else:
                print("Invalid choice! Please enter a valid option.")

    def forest(self):
        
        
        print("🌲 Entering the forest...")

    def sea(self):
        print("🌊 Entering the sea...")

    def cave(self):
        print("🦇 Entering the cave...")

        