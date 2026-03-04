"""Combat systems for Meowtal Combat."""

import random


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
        print(f"\nLEVEL UP! You are now level {player['level']}.")
        print("Max HP +5, Attack +1, Defense +1, HP fully restored.")


def combat(player, mode="explore"):
    """Turn-based combat loop. Returns win/loss/escape/boss_win."""
    enemy = generate_enemy(player, mode=mode)
    print(f"\nA {enemy['name']} appears!")

    while player["hp"] > 0 and enemy["hp"] > 0:
        print("\n--- Combat ---")
        print(f"Your HP: {player['hp']}/{player['max_hp']}")
        print(f"{enemy['name']} HP: {enemy['hp']}")
        print("1. Scratch")
        print("2. Use Catnip (+8 HP)")
        print("3. Run (50% chance)")

        action = input("Choose action: ").strip()

        if action == "1":
            damage = calculate_damage(player["attack"], enemy["defense"])
            enemy["hp"] -= damage
            print(f"You scratch for {damage} damage.")

        elif action == "2":
            if player["catnip"] > 0:
                player["catnip"] -= 1
                old_hp = player["hp"]
                player["hp"] = min(player["max_hp"], player["hp"] + 8)
                healed = player["hp"] - old_hp
                print(f"You used catnip and healed {healed} HP.")
            else:
                print("No catnip left.")
                continue

        elif action == "3":
            if random.random() < 0.5:
                print("You escaped!")
                return "escape"
            print("Run failed! You lose your turn.")

        else:
            print("Invalid choice.")
            continue

        if enemy["hp"] <= 0:
            print(f"\nYou defeated {enemy['name']}!")
            player["xp"] += enemy["xp_reward"]
            player["treats"] += enemy["treat_reward"]
            print(f"+{enemy['xp_reward']} XP, +{enemy['treat_reward']} treats")

            if enemy["boss"]:
                player["boss_defeated"] = True
                return "boss_win"

            level_up(player)
            return "win"

        enemy_damage = calculate_damage(enemy["attack"], player["defense"])
        player["hp"] -= enemy_damage
        print(f"The {enemy['name']} hits you for {enemy_damage} damage.")

    print("\nYou were defeated... ")
    return "loss"
