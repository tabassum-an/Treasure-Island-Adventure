import time
import os
import random


def clear_screen():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def print_slow(text, delay=0.03):
    """Print text with a typing effect."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


def game_over(reason):
    """Handle game over scenarios with a consistent format."""
    print_slow(f"\n{reason}", 0.05)
    print_slow("GAME OVER", 0.1)

    if input("\nPlay again? (y/n): ").lower() == 'y':
        clear_screen()
        start_game()
    else:
        print_slow("Thanks for playing Treasure Island!")


def start_game():
    clear_screen()
    print_slow("Welcome to Treasure Island.", 0.05)
    print_slow("Your mission is to find the treasure.", 0.05)
    print_slow("""
    *******************************************************************************
    *                                                                             *
    *                    TREASURE ISLAND ADVENTURE                                *
    *                                                                             *
    *******************************************************************************
    """, 0.005)
    time.sleep(1)
    first_choice()


def first_choice():
    print_slow('\nYou\'re at a crossroad.', 0.03)
    choice1 = input('Where do you want to go? Type "left" or "right": ').lower()

    if choice1 == "left":
        print_slow("\nYou decide to take the left path...")
        lake_choice()
    elif choice1 == "right":
        game_over("You fell into a hidden hole!")
    else:
        print_slow("Invalid choice. Please choose 'left' or 'right'.")
        first_choice()


def lake_choice():
    print_slow('\nYou\'ve come to a lake. There is an island in the middle of the lake.', 0.03)
    choice2 = input('Type "wait" to wait for a boat. Type "swim" to swim across: ').lower()

    if choice2 == "wait":
        print_slow("\nYou wait patiently and eventually a small boat arrives...")
        door_choice()
    elif choice2 == "swim":
        game_over("You got attacked by an angry trout while swimming!")
    else:
        print_slow("Invalid choice. Please choose 'wait' or 'swim'.")
        lake_choice()


def door_choice():
    print_slow("\nYou arrive at the island unharmed. There is a house with 3 doors.", 0.03)
    print_slow("One red, one yellow, and one blue.", 0.03)
    choice3 = input("Which color do you choose? (red/yellow/blue): ").lower()

    if choice3 == "red":
        game_over("It's a room full of fire!")
    elif choice3 == "yellow":
        treasure_found()
    elif choice3 == "blue":
        game_over("You enter a room of hungry beasts!")
    else:
        print_slow("Invalid choice. Please choose 'red', 'yellow', or 'blue'.")
        door_choice()


def treasure_found():
    print_slow("\nThe door creaks open slowly...", 0.05)
    time.sleep(1)
    print_slow("You found the treasure chest!", 0.05)
    print_slow("""
    *******************************************************************************
    *                                                                             *
    *                            YOU WIN!                                         *
    *                                                                             *
    *                          _.--.                                              *
    *                      _.-'_:-'||                                             *
    *                  _.-'_.-::::'||                                             *
    *             _.-:'_.-::::::'  ||                                             *
    *           .'`-.-:::::::'     ||                                             *
    *          /.'`;|:::::::'      ||_                                            *
    *         ||   ||::::::'     _.;._'-._                                        *
    *         ||   ||:::::'  _.-!oo @.!-._'-.                                     *
    *         \`.  ||:::::.-!()oo @!()@.-'_.|                                     *
    *          '.'-;|:.-'.&$@.& ()$%-'o.'\|||                                     *
    *            `>'-.!@%()@'@_%-'_.-o _.|'||                                     *
    *             ||-._'-.@.-'_.-' _.-o  |'||                                     *
    *             ||=[ '-._.-.-'      0  |'||                                     *
    *             || '-.]=|| |'|      o  |'||                                     *
    *             ||      || |'|        _| ';                                     *
    *             ||      || |'|    _.-'_.-'                                      *
    *             |'-._   || |'|_.-'_.-'                                          *
    *              '-._'-.|| |' `_.-'                                             *
    *                  '-.||_/.-'                                                 *
    *                                                                             *
    *******************************************************************************
    """, 0.05)

    if input("\nPlay again? (y/n): ").lower() == 'y':
        clear_screen()
        start_game()
    else:
        print_slow("Thanks for playing Treasure Island!")


if __name__ == "__main__":
    try:
        start_game()
    except KeyboardInterrupt:
        print("\n\nGame interrupted. Thanks for playing!")