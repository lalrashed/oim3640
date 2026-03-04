#Meowtal Combat RPG
"""Project 1 - Meowtal Combat 
"""
from MC_explore import explore, hunt_boss 
from MC_shop import shop

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
        "xp_to_next":20, # for level up function in combat 
        "treats": 10,
        "catnip": 2,
        "boss_defeated": False  #for win condition
    }

def main_menu(player):
    """Display the main menu options."""
    print("\n=== MEOWTAL COMBAT ===")
    print("1. Explore 🔭")
    print("2. Shop 🛍️")
    print("3. View Stats 🌟 ")
    print("4. Quit 🛑")
    if player["level"]>=3:
        print("5. Hunt Boss - FINAL CHALLENGE UNLOCKED")

def handle_menu_choice(player, choice):
    """Handle one menu choice. Return False to stop the game loop."""
    if choice == "1":
        result = explore(player)
        if result == "loss":
            print("\nGAME OVER: Your kitty was defeated in the alley.")
            return False
    elif choice == "2":
        shop(player)
    elif choice == "3":
        show_stats(player)
    elif choice == "4":
        print("Goodbye, alley cat.")
        return False
    elif choice == "5":
        result = hunt_boss(player)
        if result == "loss":
            return False
        if result == "boss_win":
            print("\nYou defeated the Supreme Roomba. You win!")
            return False
    else:
        print("Invalid choice. Enter number ")

    return True


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



def demo_tutorial(name):
    """Explain how the game works, how to win, and how to lose."""

    print("\n=== Meowtal Combat Demo ===")
    print(f"Welcome, {name}.")
    print("You are a stray cat surviving a city of rogue robot vacuums.")

    print("\nGoal:")
    print("Reach Level 3, then defeat the Supreme Roomba.")

    print("\nGame Over:")
    print("If your HP drops to 0, your run ends.")

    print("\nHow gameplay works:")
    print("1) Explore: random alley events (enemies, treats, or quiet alley).")
    print("2) Combat: choose actions each turn to survive and win XP/treats.")
    print("3) Shop: spend treats on catnip and attack upgrades.")
    print("4) Level up: stronger stats, then push toward the boss fight.")

    print("\nMenu controls:")
    print("Type 1 to Explore.")
    print("Type 2 for Shop.")
    print("Type 3 to view stats.")
    print("Type 4 to quit.\n")

    input("Press Enter to open the main menu ->")


def main():
    """Run the main game loop."""

    #this is the only way to get the tip of the tail aligned 
    welcome_art= r"""                       /)
              /\___/\ ((
              \`@_@'/  ))
              {_:Y:.}_//
   ----------{_}^-'{_}----------"""


    
    print("Welcome to Meowtal Combat! Brave kitty, you have a journey ahead of you!")
    print(welcome_art)
    name=input("Before you start your journey, what's your name?").strip()
    print(f"Nice to meet you {name}!")
    demo_tutorial(name) 
    player = create_player(name)
    game_running = True
    while game_running:
        main_menu(player)
        choice = input("Choose an option: ").strip()
        game_running = handle_menu_choice(player, choice)


if __name__ == "__main__":
    main()

