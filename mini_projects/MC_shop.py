"""Shop systems for Meowtal Combat."""

from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt

console = Console()


def _show_shop_menu(player):
    """Menu for the shop formatted with rich table """
    table = Table(title="Alley Shop", header_style="bold cyan")
    table.add_column("Option", style="bold white")
    table.add_column("Item")
    table.add_column("Cost", justify="right")
    table.add_column("Status", justify="center")

    treats = player["treats"]
    table.add_row("1", "Buy Catnip (+1)", "6", "[green]Affordable[/]" if treats >= 6 else "[red]Too Expensive[/]")
    table.add_row("2", "Warm Vent Rest (+10 HP)", "5", "[green]Affordable[/]" if treats >= 5 else "[red]Too Expensive[/]")
    table.add_row("3", "Claw Upgrade (+1 Attack)", "20", "[green]Affordable[/]" if treats >= 20 else "[red]Too Expensive[/]")
    table.add_row("4", "Leave shop", "-", "-")

    console.print(f"\n[bold]Treats:[/] {player['treats']}  [bold]Catnip:[/] {player['catnip']}  [bold]HP:[/] {player['hp']}/{player['max_hp']}  [bold]Attack:[/] {player['attack']}")
    console.print(table)

    # """Print shop options and current resources."""
    # print("\n=== Alley Shop ===")
    # print(f"Treats: {player['treats']}")
    # print(f"Catnip: {player['catnip']}")
    # print(f"HP: {player['hp']}/{player['max_hp']}")
    # print(f"Attack: {player['attack']}")
    # print("1. Buy Catnip (+1) - 6 treats")
    # print("2. Warm Vent Rest (+10 HP) - 5 treats")
    # print("3. Claw Upgrade (+1 Attack) - 20 treats")
    # print("4. Leave shop")


def shop(player):
    """Interactive shop loop for spending treats."""
    in_shop = True
    while in_shop:
        _show_shop_menu(player)
        choice = Prompt.ask("Choose an option", choices=["1", "2", "3", "4"], default="4")
        # choice = input("Choose an option: ").strip()

        if choice == "1":
            if player["treats"] < 6:
                print("Not enough treats.")
                continue
            player["treats"] -= 6
            player["catnip"] += 1
            print("You bought 1 catnip.")

        elif choice == "2":
            if player["hp"] >= player["max_hp"]:
                print("You are already at full HP.")
                continue
            if player["treats"] < 5:
                print("Not enough treats.")
                continue
            player["treats"] -= 5
            old_hp = player["hp"]
            player["hp"] = min(player["max_hp"], player["hp"] + 10)
            healed = player["hp"] - old_hp
            print(f"You recovered {healed} HP.")

        elif choice == "3":
            if player["treats"] < 20:
                print("Not enough treats.")
                continue
            player["treats"] -= 20
            player["attack"] += 1
            print("Claws sharpened. Attack increased by 1.")

        elif choice == "4":
            print("You leave the shop.")
            in_shop = False

        else:
            print("Invalid choice.")
