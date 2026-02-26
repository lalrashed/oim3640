#Meowtal Combat RPG
"""Project 1 - Meowtal Combat 
"""

import random
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

def main_menu():
    """Display the main menu options."""
    print("\n=== MEOWTAL COMBAT ===")
    print("1. Explore 🔭")
    print("2. Shop 🛍️")
    print("3. View Stats 🌟 ")
    print("4. Quit 🛑")

def handle_menu_choice(player, choice):
    """Handle one menu choice. Return False to stop the game loop."""
    if choice == "1":
        explore(player)
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


def explore(player):
    """Handle random events when the player explores."""
    print("\nYou sneak into a neon-lit alley...")
    #randomizer for determining events
    event = random.randint(1, 100)
    #greatest prob for action/combat to keep game interesting and not make it too easy. Reward are less common. 
    if event <= 40:
        print("A rogue Roomba appears and chases you!")
        print("Combat function is coming later.")
        print("Tip: save catnip for combat healing.")
    elif event <= 70:
        found_treats = random.randint(2, 8) #randomizes num treats you get each time
        player["treats"] += found_treats #update stats
        print(f"You found a fish-snack stash! +{found_treats} treats.")
        print("Treats are currency for the shop, not direct healing.") #inform player
    elif event <= 90:
        heal_amount = random.randint(2, 4)
        old_hp = player["hp"]
        #shouldn't be possible to go over full health (i.e. 25/25) so this adds healing, but caps it at max HP 
        player["hp"] = min(player["max_hp"], player["hp"] + heal_amount) 
        gained = player["hp"] - old_hp
        if gained > 0:
            print(f"You rest by a warm vent and recover +{gained} HP.")
            print("Catnip is still your main heal during combat.")
        else:
            print("You nap by a warm vent, but you're already at full HP. Healthy kitty!")
    else:
        player["catnip"] += 1
        print("Lucky day! You found hidden catnip. +1 catnip 🪴.")
        print("Catnip heals HP when used in combat.")


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

