"""
This is the main file for the RPG game.
Run this file to play the game.
this file will import the other classes and functions that you need to run the game.
this game is a text-based RPG game.
need to create a character, explore different areas, and fight enemies.
character will have their own stats and abilities.
also username and password to save the game.
"""

from game_menu import Menu
from account_storage import AccountRegistry
from game_combat import Combat


if __name__ == "__main__":
    account_registry = AccountRegistry()
    menu = Menu(account_registry)
    account_registry.game_menu = menu
    combat = Combat(menu.character, menu)
    menu.menu()
