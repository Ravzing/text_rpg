"""
This file contains the Combat class whick is responsible for handling the combat between the player and the enemy.
"""

class Combat:

    def __init__(self, character, menu) -> None:
        self.character = character
        self.menu = menu

    def combat(self, enemy):
        print(f"\n⚔️ Combat with {enemy.name} ⚔️")
        while self.character.health > 0 and enemy.health > 0:
            self._combat_stat_display(enemy)
            self._combat_choice_display()
            choice = input("Choose your action: ")
            self._combat_choice(choice, enemy)
            self._if_enemy_alive_attack(enemy)
        self._post_combat_actions(enemy)

    def _combat_stat_display(self, enemy) -> None:
        print(f"\nYour Health: {self.character.health}")
        print(f"Enemy Health: {enemy.health}")

    def _combat_choice_display(self) -> None:
        print("1. Attack")
        print("2. Run")

    def _combat_choice(self, choice: str, enemy) -> None:
        if choice == "1":
            self._perform_attack(enemy)
        elif choice == "2":
            self._run_away()
        else:
            print("Invalid action! Please choose a valid option.")

    def _run_away(self) -> None:
        print("You ran away!")
        self.menu.wilderness()

    def _perform_attack(self, enemy) -> None:
        result = self.attack_target(self.character, enemy)
        print(result)

    def _enemy_attack(self, enemy) -> None:
        enemy_result = self.attack_target(enemy, self.character)
        print(enemy_result)

    def _if_enemy_alive_attack(self, enemy) -> None:
        if enemy.health > 0:
            self._enemy_attack(enemy)

    def _post_combat_actions(self, enemy) -> None:
        if self.character.health <= 0:
            print("You have been defeated!")
            return self.menu.map_menu()
        elif enemy.health <= 0:
            print(f"You have defeated the {enemy.name}!")
            self.menu.wilderness()
            
    def attack_target(self, attacker, target) -> str:
        damage = max(0, attacker.attack - target.armor)
        target.health -= damage
        if target.health <= 0:
            target.health = 0
        return f"{attacker.name} dealt {damage} damage, remaining health: {target.health} for {target.name}"