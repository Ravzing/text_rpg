import csv
import os

class Inventory: pass
class Equipment: pass

characters_list = "characters.csv"

class Character:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.armor = 10
        self.attack = 5
        self.woodcutting = 1
        self.fishing = 1
        self.mining = 1
        self.smithing = 1
        self.storage = characters_list
    
    def save_to_csv(self):
        file_exists = os.path.exists(characters_list)
        with open(characters_list, mode='a', newline='') as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(["name", "health", "armor", "attack", "woodcutting", "fishing", "mining", "smithing"])
            writer.writerow([self.name, self.health, self.armor, self.attack,
                            self.woodcutting, self.fishing, self.mining, self.smithing])
        print(f"Character '{self.name}' saved successfully!")
            
    @classmethod
    def load_character(cls, name):
        characters = cls.load_all_characters()
        for char in characters:
            if char["name"] == name:
                character = cls(name)
                character.health = int(char["health"])
                character.armor = int(char["armor"])
                character.attack = int(char["attack"])
                character.woodcutting = int(char["woodcutting"])
                character.fishing = int(char["fishing"])
                character.mining = int(char["mining"])
                character.smithing = int(char["smithing"])
                return character
        print(f"Character '{name}' not found in {characters_list}.")
        return None
    
    @classmethod
    def load_all_characters(cls):
        characters = []
        if os.path.exists(characters_list):
            with open(characters_list, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    characters.append(row)
        return characters
    
    def update_character(self):
        characters = self.load_all_characters()
        updated = False

        with open(characters_list, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["name", "health", "armor", "attack", "woodcutting", "fishing", "mining", "smithing"])
            for char in characters:
                if char["name"] == self.name:
                    writer.writerow([self.name, self.health, self.armor, self.attack,
                                     self.woodcutting, self.fishing, self.mining, self.smithing])
                    updated = True
                else:
                    writer.writerow([char["name"], char["health"], char["armor"], char["attack"],
                                     char["woodcutting"], char["fishing"], char["mining"], char["smithing"]])

        if updated:
            print(f"Character '{self.name}' updated successfully!")
        else:
            print(f"Character '{self.name}' not found. No update performed.")
                   
    def attack_enemy(self, enemy):
        damage =max(0, self.attack - enemy.armor)
        enemy.health -= damage
        if enemy.health <= 0:
            enemy.health = 0
        return f"{self.name} dealt {damage} damage, remaining health: {enemy.health}"
        
        