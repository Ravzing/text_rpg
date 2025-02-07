import csv
import os

CHARACTERS_LIST = "characters.csv"


class Inventory:
    pass


class Equipment:
    pass


class Character:
    def __init__(self, name: str):
        self.name: str = name
        self.health: int = 100
        self.armor: int = 10
        self.attack: int = 5
        self.woodcutting: int = 1
        self.fishing: int = 1
        self.mining: int = 1
        self.smithing: int = 1
        self.storage: str = CHARACTERS_LIST

    def save_to_csv(self) -> None:
        file_exists = os.path.exists(CHARACTERS_LIST)
        with open(CHARACTERS_LIST, mode="a", newline="") as file:
            writer = csv.writer(file)
            if not file_exists:
                self._write_csv_header(writer)
            self._write_csv_row(writer)
        print(f"Character '{self.name}' saved successfully!")

    def _write_csv_header(self, writer) -> None:
        writer.writerow(
            [
                "name",
                "health",
                "armor",
                "attack",
                "woodcutting",
                "fishing",
                "mining",
                "smithing",
            ]
        )

    def _write_csv_row(self, writer) -> None:
        writer.writerow(
            [
                self.name,
                self.health,
                self.armor,
                self.attack,
                self.woodcutting,
                self.fishing,
                self.mining,
                self.smithing,
            ]
        )

    def _write_existing_character(self, writer, char: dict) -> None:
        writer.writerow(
            [
                char["name"],
                char["health"],
                char["armor"],
                char["attack"],
                char["woodcutting"],
                char["fishing"],
                char["mining"],
                char["smithing"],
            ]
        )

    @classmethod
    def load_character(cls, name):
        characters = cls.load_all_characters()
        for char in characters:
            if char["name"] == name:
                return cls._create_character_dict(char)
        print(f"Character '{name}' not found in {CHARACTERS_LIST}.")
        return None

    @classmethod
    def _create_character_dict(cls, char: dict):
        character = cls(char["name"])
        character.health = int(char["health"])
        character.armor = int(char["armor"])
        character.attack = int(char["attack"])
        character.woodcutting = int(char["woodcutting"])
        character.fishing = int(char["fishing"])
        character.mining = int(char["mining"])
        character.smithing = int(char["smithing"])
        return character

    @classmethod
    def load_all_characters(cls):
        characters = []
        if os.path.exists(CHARACTERS_LIST):
            with open(CHARACTERS_LIST, mode="r", newline="") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    characters.append(row)
        return characters

    def update_character(self) -> None:
        characters = self.load_all_characters()
        updated = False

        with open(CHARACTERS_LIST, mode="w", newline="") as file:
            writer = csv.writer(file)
            self._write_csv_header(writer)
            for char in characters:
                if char["name"] == self.name:
                    self._write_csv_row(writer)
                    updated = True
                else:
                    self._write_existing_character(writer, char)
        self._print_update_status(updated)

    def _print_update_status(self, updated: bool) -> None:
        if updated:
            print(f"Character '{self.name}' updated successfully!")
        else:
            print(f"Character '{self.name}' not found. No update performed.")

    def attack_enemy(self, enemy) -> str:
        damage = max(0, self.attack - enemy.armor)
        enemy.health -= damage
        if enemy.health <= 0:
            enemy.health = 0
        return f"{self.name} dealt {damage} damage, remaining health: {enemy.health} for {enemy.name}"
