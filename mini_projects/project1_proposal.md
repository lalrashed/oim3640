# Mini Project Proposal  
## "Meowtal Combat" 
Layla Al-rashed
---

## 1. Project Overview

**Meowtal Combat** is a terminal-based  game where the player controls a stray cat surviving in a city ruled by rogue robotic vacuums.

The player will explore alleys, encounter enemies, collect treats (currency), purchase upgrades, and level up. The ultimate goal is to defeat the final boss: The Supreme Roomba. 

The game will operate in the terminal and rely on user input through a structured menu system.

---

## 2. Core Gameplay Loop

The player will interact with three main screens:

1. **Main Menu**
2. **Explore (Random Events)**
3. **Shop**

The game continues until:
- The player defeats the Supreme Roomba (win condition), or
- The player's HP reaches 0 (loss condition).

---

## 3. Player System

The player (cat) will have the following stats:

- HP (Health Points)
- Attack (Claw Power)
- Defense (Fur Defense)
- Level
- XP (Experience Points)
- Treats (Currency)
- Catnip (Healing item count)

Player data will be stored in a dictionary structure.

---

## 4. Exploration System

When the player chooses to explore, a random event occurs:

- Enemy encounter
- Find treats
- Quiet alley (no event)

Random outcomes will be generated using Python’s `random` module.

---

## 5. Combat System (Turn-Based)

If an enemy appears, the game enters combat mode.

During combat, the player can choose:

1. Scratch (Attack)
2. Use Catnip (Heal)
3. Run (50% success chance)

Combat continues in turns until:
- The enemy’s HP reaches 0 (victory), or
- The player’s HP reaches 0 (game over).

Damage will be calculated using attack, defense, and a small random variation.

---

## 6. Enemy System

Enemies will scale based on player level.

Enemy types include:

- Dust Bunny (weak)
- Rogue Roomba (moderate)
- Supreme Roomba (final boss)

Each enemy will have:
- HP
- Attack
- Defense
- XP reward
- Treat reward

Enemy data will also be stored in dictionary structures.

---

## 7. Shop System

The player can spend Treats at the shop to purchase:

1. Catnip (healing item)
2. Sharpen Claws (+1 permanent attack upgrade)

The shop will use a simple numbered input system.

---

## 8. Leveling System

The player earns XP after winning battles.

When XP reaches the required threshold:
- Level increases
- Max HP increases
- Attack increases
- HP restores to full

XP required to level up will increase with each level.

---

## 9. Win Condition

The player wins by reaching Level 3 and defeating the Supreme Roomba.

The game ends if the player's HP reaches 0.

---

## 10. Technical Implementation

This project will use:

- Python
- Functions to modularize the game logic
- Dictionaries for storing player and enemy data
- Lists for inventory management
- The `random` module for encounter generation
- A continuous game loop for user interaction

---

## 11. Planned Function Structure

- `main()`
- `create_player()`
- `main_menu(player)`
- `explore(player)`
- `generate_enemy(player)`
- `combat(player, enemy)`
- `shop(player)`
- `level_up(player)`

---

I want to pursue this project because I think it will challenge me while also being fun. I adore cats, so a cat-focused game is an exciting prospect to build out!