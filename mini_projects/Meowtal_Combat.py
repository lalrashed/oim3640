#Meowtal Combat RPG
"""Project 1 - Meowtal Combat 
"""
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt

from MC_explore import explore, hunt_boss
from MC_shop import shop

console = Console()

WIN_ART =r"""    *                  *
             __                *
          ,db'    *     *
         ,d8/       *        *    *
         888
         `db\       *     *
           `o`_                    **
      *               *   *    _      *
            *                 / )
         *    (\__/) *       ( (  *
       ,-.,-.,)    (.,-.,-.,-.) ).,-.,-.
      | @|  ={      }= | @|  / / | @|o |
     _j__j__j_)     `-------/ /__j__j__j_
     ________(               /___________
      |  | @| \              || o|O | @|
      |o |  |,'\       ,   ,'"|  |  |  |  
     vV\|/vV|`-'\  ,---\   | \Vv\hjwVv\//v
                _) )    `. \ /
               (__/       ) )
                         (_/"""

LOSE_ART =  r"""
      |\      _,,,---,,_
      /,`.-'`'    -.  ;-;;,_
     |,4-  ) )-,_. ,\ (  `'-'
    '---''(_/--'  `-'\_)  """




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
    menu_text = (
        "[bold cyan]1.[/] Explore 🔭\n"
        "[bold cyan]2.[/] Shop 🛍️\n"
        "[bold cyan]3.[/] View Stats 🌟\n"
        "[bold cyan]4.[/] Quit 🛑"
    )
    if player["level"] >= 3:
        menu_text += "\n[bold cyan]5.[/] Hunt Boss - [bold red]FINAL CHALLENGE UNLOCKED[/]"

    console.print(
        Panel.fit(
            menu_text,
            title="[bold magenta]MEOWTAL COMBAT[/]",
            border_style="bright_blue",
        )
    )



def handle_menu_choice(player, choice):
    """Handle one menu choice. Return False to stop the game loop."""
    if choice == "1":
        result = explore(player)
        if result == "loss":
            console.print("\n[bold red]GAME OVER:[/] Your kitty was defeated in the alley.")
            console.print(LOSE_ART, style="red")
            return False
        pause()
    elif choice == "2":
        shop(player)
    elif choice == "3":
        show_stats(player)
        pause()
    elif choice == "4":
        console.print("[bold yellow]Goodbye, alley cat.[/]")
        return False
    elif choice == "5":
        result = hunt_boss(player)
        if result == "loss":
            console.print(LOSE_ART, style="red")
            return False
        if result == "boss_win":
            console.print("\n[bold green]You defeated the Supreme Roomba. You win kitty![/]")
            console.print(WIN_ART, style="green")
            return False
    else:
        console.print("[red]Invalid choice. Enter a number.[/]")

    return True


def show_stats(player):

    """Display current player stats."""
    table = Table(title="🐈 Cat Stats 🐈", show_header=True, header_style="bold green")
    table.add_column("Stat", style="cyan")
    table.add_column("Value", style="white")

    table.add_row("Name", str(player["name"]))
    table.add_row("HP", f'{player["hp"]}/{player["max_hp"]}')
    table.add_row("Attack", str(player["attack"]))
    table.add_row("Defense", str(player["defense"]))
    table.add_row("Level", str(player["level"]))
    table.add_row("XP", str(player["xp"]))
    table.add_row("Treats", str(player["treats"]))
    table.add_row("Catnip", str(player["catnip"]))

    console.print(table)


def demo_tutorial(name):
    """Explain how the game works, how to win, and how to lose."""
    demo_text = (
        f"Welcome, [bold]{name}[/].\n"
        "You are a stray cat surviving a city of rogue robot vacuums.\n\n"
        "[bold]Goal:[/]\n"
        "Reach [bold]Level 3[/], then defeat the [bold]Supreme Roomba[/].\n\n"
        "[bold]Game Over:[/]\n"
        "If your HP drops to [bold]0[/], your run ends.\n\n"
        "[bold]Tip[/]:\nTreats are used as currency for the Shop. You can use treats to buy catnip that will heal you in combat or buy rests that will recover your HP.\n\n "
        "[bold]How gameplay works:[/]\n"
        "1) Explore: random alley events (enemies, treats, or quiet alley).\n"
        "2) Combat: choose actions each turn to survive and win [bold]XP[/]/treats.\n"
        "3) Shop: spend treats on [bold]catnip[/] and attack upgrades.\n"
        "4) Level up: stronger stats, then push toward the boss fight.\n\n"
        "[bold]Menu controls:[/]\n"
        "Type [bold]1[/] to Explore.\n"
        "Type [bold]2[/] for Shop.\n"
        "Type [bold]3[/] to view stats.\n"
        "Type [bold]4[/] to quit."
    )

    console.print(
        Panel(
            demo_text,
            title="Meowtal Combat Demo",
            border_style="bright_blue",
            expand=False,
            padding=(1, 2),
        )
    )
    input("Press Enter to open the main menu -> ")

def pause():
    """spaces out the game"""
    input("Press Enter to continue...\n\n")


def main():
    """Run the main game loop."""

    #this is the only way to get the tip of the tail aligned 
    welcome_art= r"""                       /)
              /\___/\ ((
              \`@_@'/  ))
              {_:Y:.}_//
   ----------{_}^-'{_}----------"""

    console.print("\n[bold yellow]Welcome to Meowtal Combat! Brave kitty, you have a journey ahead of you![/]")
    console.print(welcome_art, style="bold white")
 
    name=input("\nBefore you start your journey, what's your name?").strip()
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

