from enemies_list import Enemy

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
            elif choice == "4":
                self.add_stats()
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
            print("4. Wilderness")
            print("5. Back")
            sub_choice = input("Choice: ")
            
            if sub_choice == "1":
                self.forest()
            elif sub_choice == "2":
                self.sea()
            elif sub_choice == "3":
                self.cave()
            elif sub_choice == "4":
                self.wilderness()
            elif sub_choice == "5":
                return 
            else:
                print("Invalid choice! Please enter a valid option.")

    def forest(self):
        print("🌲 Entering the forest...")

    def sea(self):
        print("🌊 Entering the sea...")

    def cave(self):
        print("🦇 Entering the cave...")
        
    def wilderness(self):
        print("🐺 Entering the wilderness...")
        print("Enemies in area:")
        enemies = Enemy.load_enemies_from_csv()
        for i, enemy in enumerate(enemies):
            print(f"{i + 1}: {enemy.name}: Health: {enemy.health}, Armor: {enemy.armor}, Attack: {enemy.attack}")
        choice = int(input("Choose an enemy to fight: ")) - 1
        if 0 <= choice < len(enemies):
            self.combat(enemies[choice])
        else:
            print("Invalid choice! Returning to map menu.")
            
    def add_stats(self):
        self.current_character.armor += 10
        return self.current_character.update_character()
    
    def combat(self, enemy):
        print(f"\n⚔️ Combat with {enemy.name} ⚔️")
        while self.current_character.health > 0 and enemy.health > 0:
            print(f"\nYour Health: {self.current_character.health}")
            print(f"Enemy Health: {enemy.health}")
            print("1. Attack")
            print("2. Run")
            action = input("Choose your action: ")
            if action == "1":
                result = self.current_character.attack_enemy(enemy)
                print(result)
            elif action == "2":
                print("You ran away!")
                return self.wilderness()
            else:
                print("Invalid action! Please choose a valid option.")
            if enemy.health > 0:
                enemy_result = enemy.attack_enemy(self.current_character)
                print(enemy_result)
        if self.current_character.health <= 0:
            print("You have been defeated!")
            return self.map_menu()
        elif enemy.health <= 0:
            print(f"You have defeated the {enemy.name}!")
            return self.wilderness()