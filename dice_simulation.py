import random
import time
import sys

# Dice faces as ASCII art
dice_faces = {
    1: "🎲\n[     ]\n[  *  ]\n[     ]",
    2: "🎲\n[ *   ]\n[     ]\n[   * ]",
    3: "🎲\n[ *   ]\n[  *  ]\n[   * ]",
    4: "🎲\n[ * * ]\n[     ]\n[ * * ]",
    5: "🎲\n[ * * ]\n[  *  ]\n[ * * ]",
    6: "🎲\n[ * * ]\n[ * * ]\n[ * * ]"
}


def roll_dice_effect():
    """Simulates the dice rolling effect with animation."""
    print("Rolling the dice...")
    for i in range(6):  # Rolling animation
        print(f"🎲 Rolling... {random.randint(1, 6)}", end="\r", flush=True)
        time.sleep(0.2)
    print("\n")


def display_dice_face(number):
    """Displays the ASCII art of the dice face."""
    print(dice_faces[number])


def main():
    print("Welcome to the Dice Simulator! 🎲")
    print("Type 'exit' anytime to quit.")
    print("-" * 30)

    while True:
        user_input = input("Roll the dice? (yes/no/exit): ").strip().lower()
        if user_input == "yes":
            roll_dice_effect()
            rolled_number = random.randint(1, 6)
            display_dice_face(rolled_number)
            print(f"You rolled: {rolled_number}")
            print("-" * 30)
        elif user_input == "no":
            print("Okay! If you change your mind, type 'yes' to roll.")
        elif user_input == "exit":
            print("Thanks for playing! Goodbye!")
            sys.exit(0)  # Clean exit
        else:
            print("Invalid input. Please type 'yes', 'no', or 'exit'.")


# Run the program
if __name__ == "__main__":
    main()



