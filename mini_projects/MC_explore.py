"""Exploration systems for Meowtal Combat."""

import random
from MC_combat import combat

def explore(player):
    """Handle random events when the player explores."""
    print("\nYou sneak into a neon-lit alley...")
    # randomizer for determining events
    event = random.randint(1, 100)

    # greatest prob for action/combat to keep game interesting and not make it too easy. Reward are less common.
    if event <= 40:
        print("A rogue Roomba appears and chases you!")
        print("Tip: save catnip for combat healing.")
        return combat(player, mode="explore")  # now actually enters combat

    elif event <= 70:
        found_treats = random.randint(2, 8)  # randomizes num treats you get each time
        player["treats"] += found_treats  # update stats
        print(f"You found a fish-snack stash! +{found_treats} treats.")
        print("Treats are currency for the shop, not direct healing.")  # inform player
        return "treats"

    elif event <= 90:
        heal_amount = random.randint(2, 4)
        old_hp = player["hp"]
        # shouldn't be possible to go over full health (i.e. 25/25) so this adds healing, but caps it at max HP
        player["hp"] = min(player["max_hp"], player["hp"] + heal_amount)
        gained = player["hp"] - old_hp
        if gained > 0:
            print(f"You rest by a warm vent and recover +{gained} HP.")
            print("Catnip is still your main heal during combat.")
        else:
            print("You nap by a warm vent, but you're already at full HP. Healthy kitty!")
        return "rest"

    else:
        player["catnip"] += 1
        print("Lucky day! You found hidden catnip. +1 catnip 🪴.")
        print("Catnip heals HP when used in combat.")
        return "catnip"



def hunt_boss(player):
    """High-risk mode: more enemy encounters, chance for final boss."""
    if player["level"] < 3:
        print("\nYou are not strong enough to hunt the Supreme Roomba yet.")
        print("Reach level 3 first.")
        return "locked"

    print("\nYou enter Downtown Core. Danger is everywhere...")
    roll = random.randint(1, 100)

    # Very high chance of combat in hunt mode
    if roll <= 85:
        return combat(player, mode="hunt_boss")

    print("You scout the area but find no target this round.")
    return "no_target"


