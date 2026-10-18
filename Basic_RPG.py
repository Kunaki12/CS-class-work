#By Cameron Greene
#Basic RPG game
#10/17/2026 

import random

# Parent class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def is_alive(self):
        return self.health > 0

    def attack(self, target):
        damage = random.randint(1, self.attack_power)
        target.health = max(0, target.health - damage)

        print(f"{self.name} attacks {target.name}!")
        print(f"{target.name} takes {damage} damage!")

    def show_status(self):
        print(f"\nName: {self.name}")
        print(f"Health: {self.health}")
        print(f"Attack Power: {self.attack_power}")


# Child class
class Player(Character):
    def __init__(self, name):
        super().__init__(name, 100, 20)

        self.level = 1
        self.gold = 0
        self.inventory = ["Health Potion"]

    def heal(self):
        if "Health Potion" in self.inventory:
            self.health = min(100, self.health + 30)
            self.inventory.remove("Health Potion")
            print(f"{self.name} used a Health Potion!")
            print(f"Health is now {self.health}.")
        else:
            print("You don't have any potions!")

    def level_up(self):
        self.level += 1
        self.attack_power += 5
        print(f"\nLEVEL UP! You are now level {self.level}!")

    def show_status(self):
        super().show_status()
        print(f"Level: {self.level}")
        print(f"Gold: {self.gold}")
        print(f"Inventory: {self.inventory}")


# Another child class
class Monster(Character):
    def __init__(self, name, health, attack_power):
        super().__init__(name, health, attack_power)


# Function to create a random monster
def create_monster():
    monsters = [
        {"name": "Goblin", "health": 40, "attack": 10},
        {"name": "Skeleton", "health": 50, "attack": 12},
        {"name": "Orc", "health": 70, "attack": 15}
    ]

    monster_data = random.choice(monsters)

    return Monster(
        monster_data["name"],
        monster_data["health"],
        monster_data["attack"]
    )


# Function for battling monsters
def battle(player):
    monster = create_monster()

    print(f"\nA wild {monster.name} appears!")

    while player.is_alive() and monster.is_alive():

        print(f"\nYour HP: {player.health}")
        print(f"{monster.name} HP: {monster.health}")

        print("\n1. Attack")
        print("2. Heal")
        print("3. Run")

        choice = input("Choose an action: ").strip()

        if choice == "1":
            player.attack(monster)

        elif choice == "2":
            player.heal()

        elif choice == "3":
            print("You escaped!")
            return

        else:
            print("Invalid choice!")
            continue

        # Monster attacks if still alive
        if monster.is_alive():
            monster.attack(player)

    if player.is_alive():
        print(f"\nYou defeated the {monster.name}!")

        gold_reward = random.randint(10, 30)
        player.gold += gold_reward

        print(f"You earned {gold_reward} gold!")
        player.level_up()

    else:
        print("\nYou have been defeated!")


# Main game function
def main():
    print("WELCOME TO MEDIEVAL RPG!")

    name = input("Enter your character's name: ").strip()

    if not name:
        name = "Knight"

    player = Player(name)

    shop = {
        "Health Potion": 15
    }

    while player.is_alive():

        print("\n===== MAIN MENU =====")
        print("1. Fight Monster")
        print("2. View Character")
        print("3. Buy Health Potion")
        print("4. Quit")

        try:
            choice = int(input("Choose an option: "))

        except ValueError:
            print("Please enter a number!")
            continue

        if choice == 1:
            battle(player)

        elif choice == 2:
            player.show_status()

        elif choice == 3:
            potion_price = shop["Health Potion"]

            if player.gold >= potion_price:
                player.gold -= potion_price
                player.inventory.append("Health Potion")
                print("You bought a Health Potion!")
            else:
                print("Not enough gold!")

        elif choice == 4:
            print("Thanks for playing!")
            break

        else:
            print("Invalid option!")

    if not player.is_alive():
        print("GAME OVER!")


# Start the game
if __name__ == "__main__":
    main()
