"""Combat systems for Meowtal Combat."""

import random
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

console = Console()

BOSS_ART= r"""
            (\. -- ./)
        O-0)))--|     \
          |____________|
           -|--|--|--|-
           _T~_T~_T~_T_
          |____________|
          |_o_|____|_o_|
       .-~/  :  |   %  \
.-..-~   /  :   |  %:   \
`-'     /   :   | %  :   \
       /   :    |#   :    \
      /    :    |     :    \
     /    :     |     :     \
 . -/     :     |      :     \- .
|\  ~-.  :      |      :   .-~  /|
\ ~-.   ~ - .  _|_  . - ~   .-~ /
  ~-.  ~ -  . _ _ _ .  - ~  .-~
       ~ -  . _ _ _ .  - ~"""

def hp_bar(current, maximum, width=20):
    """creates a bar to show player's changing HP"""
    current = max(0, min(current, maximum))
    filled = int((current / maximum) * width) if maximum else 0
    empty = width - filled
    return f"[green]{'█' * filled}[/][grey50]{'░' * empty}[/] {current}/{maximum}"


def generate_enemy(player, mode="explore"):
    """Create enemy stats scaled by player level."""
    level = player["level"]

    dust_bunny = {
        "name": "Dust Bunny",
        "hp": 10 + (level * 2),
        "attack": 4 + level,
        "defense": 1 + (level // 2),
        "xp_reward": 8 + (level * 2),
        "treat_reward": 5 + level,
        "boss": False,
    }

    rogue_roomba = {
        "name": "Rogue Roomba",
        "hp": 15 + (level * 3),
        "attack": 6 + level,
        "defense": 2 + (level // 2),
        "xp_reward": 12 + (level * 3),
        "treat_reward": 8 + (level * 2),
        "boss": False,
    }

    supreme_roomba = {
        "name": "Supreme Roomba",
        "hp": 36 + (level * 4),
        "attack": 10 + level,
        "defense": 4 + (level // 2),
        "xp_reward": 40,
        "treat_reward": 30,
        "boss": True,
    }

    if mode == "hunt_boss" and level >= 3:
        if random.randint(1, 100) <= 40:
            return supreme_roomba

    return random.choice([dust_bunny, rogue_roomba])


def calculate_damage(attacker_attack, defender_defense):
    """Damage formula with slight random variation."""
    variation = random.randint(-1, 2)
    raw_damage = attacker_attack + variation - defender_defense
    return max(1, raw_damage)


def level_up(player):
    """Apply level ups while XP threshold is met."""
    while player["xp"] >= player["xp_to_next"]:
        player["xp"] -= player["xp_to_next"]
        player["level"] += 1
        player["max_hp"] += 5
        player["attack"] += 1
        player["defense"] += 1
        player["hp"] = player["max_hp"]
        player["xp_to_next"] += 10
        console.print(f"\n[bold magenta]LEVEL UP![/] You are now level [bold]{player['level']}[/].")
        console.print("[green]Max HP +5, Attack +1, Defense +1, HP fully restored.[/]")



def combat(player, mode="explore"):
    """Turn-based combat loop. Returns win/loss/escape/boss_win."""
    enemy = generate_enemy(player, mode=mode)
    enemy_max_hp = enemy["hp"] #fixed denominator for the fight 
    console.print(Panel.fit(f"[bold red]A {enemy['name']} appears![/]", border_style="red"))

    if enemy["boss"]:
        console.print("[bold red]The Supreme Roomba descends...[/]")
        console.print(BOSS_ART, style="bold red")


    while player["hp"] > 0 and enemy["hp"] > 0:
        console.rule("[bold blue]Combat Turn[/]")
        console.print(f"Your HP   : {hp_bar(player['hp'], player['max_hp'])}")
        console.print(f"{enemy['name']} HP: {hp_bar(enemy['hp'], enemy_max_hp)}")
        console.print()
        console.print(
            Panel.fit(
                "1. Scratch\n2. Use Catnip (+8 to +13 HP)\n3. Run (50% chance)",
                title="Choose Action",
                border_style="cyan",
            )
        )

        action = Prompt.ask("Choose action", choices=["1", "2", "3"], default="1")
        console.print()

        if action == "1":
            damage = calculate_damage(player["attack"], enemy["defense"])
            enemy["hp"] -= damage
            console.print(f"[green]You scratch for {damage} damage.[/]")
            console.print()

        elif action == "2":
            if player["catnip"] > 0:
                player["catnip"] -= 1
                old_hp = player["hp"]
                heal_amount = 8 + min(5, player["level"] - 1)
                player["hp"] = min(player["max_hp"], player["hp"] + heal_amount)
                healed = player["hp"] - old_hp
                console.print(f"[green]You used catnip and healed {healed} HP.[/]")
                console.print()
            else:
                console.print("[yellow]No catnip left.[/]")
                console.print()
                continue

        elif action == "3":
            if random.random() < 0.5:
                console.print("[yellow]You escaped![/]")
                return "escape"
            console.print("[yellow]Run failed! You lose your turn.[/]")
            console.print()

        else:
            console.print("[red]Invalid choice.[/]")
            console.print()
            continue

        if enemy["hp"] <= 0:
            console.print(f"[bold green]You defeated {enemy['name']}![/]")
            player["xp"] += enemy["xp_reward"]
            player["treats"] += enemy["treat_reward"]
            console.print(f"[cyan]+{enemy['xp_reward']} XP[/], [yellow]+{enemy['treat_reward']} treats[/]")
            console.print()

            if enemy["boss"]:
                player["boss_defeated"] = True
                return "boss_win"

            level_up(player)
            return "win"

        console.print("[dim]Enemy turn...[/]")
        enemy_damage = calculate_damage(enemy["attack"], player["defense"])
        player["hp"] -= enemy_damage
        console.print(f"[red]The {enemy['name']} hits you for {enemy_damage} damage.[/]")
        console.print()

    console.print("[bold red]\nYou were defeated...[/]")
    return "loss"
