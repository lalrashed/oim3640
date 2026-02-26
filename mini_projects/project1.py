#Meowtal Combat RPG
"""Project 1 - Meowtal Combat 
"""


def create_player(name):
    """Create and return the player stats dictionary. Set to default values."""
    return {
        "name": name,
        "hp": 25,
        "max_hp": 25,
        "attack": 6,
        "defense": 2,
        "level": 1,
        "xp": 0,
        "treats": 10,
        "catnip": 2,
    }


def show_stats(player):
    """Display current player stats."""
    print("\n=== 🐈 Cat Stats 🐈===")
    print(f"Name: {player['name']}")
    print(f"HP: {player['hp']}/{player['max_hp']}")
    print(f"Attack: {player['attack']}")
    print(f"Defense: {player['defense']}")
    print(f"Level: {player['level']}")
    print(f"XP: {player['xp']}")
    print(f"Treats: {player['treats']}")
    print(f"Catnip: {player['catnip']}")


def main_menu():
    """Display the main menu options."""
    print("\n=== MEOWTAL COMBAT ===")
    print("1. Explore 🔭")
    print("2. Shop 🛍️")
    print("3. View Stats 🌟 ")
    print("4. Quit 🛑")


def handle_menu_choice(player, choice):
    """Handle one menu choice. Return 3False to stop the game loop."""
    if choice == "1":
        print("\nExplore is coming ")
    elif choice == "2":
        print("\nShop is coming")
    elif choice == "3":
        show_stats(player)
    elif choice == "4":
        print("Goodbye, alley cat.")
        return False
    else:
        print("Invalid choice. Enter 1, 2, 3, or 4.")

    return True


def demo_tutorial(player):
    """Walks the player through menu navigation before gameplay starts."""

    print("\n=== Meowtal Combat Demo ===")
    print(f"Welcome, {player}.")
    print("This game uses number choices in the menu.")
    print("Type 1 to Explore.")
    print("Type 2 to open the Shop.")
    print("Type 3 to view your current stats.")
    print("Type 4 to quit the game.")
    input("Press Enter to open the main menu ->")

def main():
    """Run the main game loop."""

    print("Welcome to Meowtal Combat! Brave kitty, you have a journey ahead of you!")
    name=input("Before you start your journey, what's your name?").strip()
    print("Nice to meet you {name}!")
    demo_tutorial(name) 
    player = create_player(name)
    game_running = True
    while game_running:
        main_menu()
        choice = input("Choose an option: ").strip()
        game_running = handle_menu_choice(player, choice)


if __name__ == "__main__":
    main()