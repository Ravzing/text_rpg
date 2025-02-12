import csv
import os

enemy_storage = "enemies.csv"


class Enemy:
    def __init__(self, name, health, armor, attack):
        self.name = name
        self.health = int(health)
        self.armor = int(armor)
        self.attack = int(attack)
        self.storage = enemy_storage

    @classmethod
    def load_enemies_from_csv(cls):
        enemies = []
        if os.path.exists(enemy_storage):
            with open(enemy_storage, mode="r", newline="") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if row["name"] and row["health"] and row["armor"] and row["attack"]:
                        enemies.append(
                            cls(row["name"], row["health"], row["armor"], row["attack"])
                        )
        return enemies
