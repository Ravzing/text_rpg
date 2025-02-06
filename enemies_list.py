import csv

enemy_storage = "enemies.csv"

class Enemy:
    def __init__(self, name, health, armor, attack):
        self.name = name
        self.health = health
        self.armor = armor
        self.attack = attack
        self.storage = enemy_storage
        
    def take_damage(self, damage):
        self.health -=max(0, damage)
        if self.health <= 0:
            self.health = 0
            return "{self.name} has been slain"
        return f"{self.name} took {damage} damage, remaining health: {self.health}"
    
    def load_enemies_from_csv(self):
        enemies = []
        with open(enemy_storage, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                enemies.append(Enemy(row["name"], row["health"], row["armor"], row["attack"]))
        return enemies