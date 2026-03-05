"""Exploration systems for Meowtal Combat."""

import random
from MC_combat import combat
from rich.console import Console
from rich.panel import Panel
console = Console()


def explore(player):
    """Handle random events when the player explores."""
    console.print(Panel.fit("[bold cyan]You sneak into a neon-lit alley...[/]", border_style="cyan"))
    # randomizer for determining events
    event = random.randint(1, 100)

    # greatest prob for action/combat to keep game interesting and not make it too easy. Reward are less common.
    if event <= 40:
        console.print("[bold red]An enemy appears and chases you![/]\n")
        console.print("[yellow]Tip: save catnip for combat healing.[/]")
        return combat(player, mode="explore")  # now actually enters combat

    elif event <= 70:
        found_treats = random.randint(2, 8)  # randomizes num treats you get each time
        player["treats"] += found_treats  # update stats
        console.print(f"[bold green]You found a fish-snack stash! +{found_treats} treats.[/]")
        print("Treats are currency for the shop, not direct healing.\n")  # inform player
        return "treats"

    elif event <= 90:
        heal_amount = random.randint(2, 4)
        old_hp = player["hp"]
        # shouldn't be possible to go over full health (i.e. 25/25) so this adds healing, but caps it at max HP
        player["hp"] = min(player["max_hp"], player["hp"] + heal_amount)
        gained = player["hp"] - old_hp
        if gained > 0:
            console.print(f"[bold green]You rest by a warm vent and recover +{gained} HP.[/]")
            print("Catnip is still your main heal during combat.")
        else:
            console.print("[bold magenta]Lucky day! You found hidden catnip. +1 catnip.[/]\n")
        return "rest"

    else:
        player["catnip"] += 1
        print("Lucky day! You found hidden catnip. +1 catnip 🪴.")
        print("Catnip heals HP when used in combat.\n")
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


