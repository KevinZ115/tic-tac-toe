import random
import sys


def guess_number(name='PlayerOne'):
    player_wins = 1
    game_count = 1

    def play_guess_number():
        nonlocal name
        nonlocal player_wins


        player_choice = input(
            f"\n{name} Guess a number: 1, 2, 3 \n\n"
        )

        if player_choice not in ["1", "2", "3"]:
            print(f"Invalid choice, {name}, Please enter 1, 2, or 3.")
            return play_guess_number()

        computer_choice = random.choice("123")

        print(f"\n{name}, you chose {player_choice}.")
        print(f"I was thinking about the number {computer_choice}.")

        player = int(player_choice)
        computer = int(computer_choice)

        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins

            if player == computer:
                player_wins += 1
                return f"{name} You Win"
            else:
                return f"Sorry {name} better luck next time"
            
        game_result = decide_winner(player, computer)

        print(game_result)

        nonlocal game_count
        game_count += 1


        print(f"\nGame Count: {game_count}")
        print(f"\nPlayer Wins: {player_wins}")
        print(f"\nWinning Percentage: {player_wins / game_count:.2%}")

        print(f"\nPlay again {name}")

        while True:
            playagain = input("\nY for Yes or \nQ to Quit\n")
            if playagain.lower() not in ["y", "q"]:
                continue
            else:
                break

        if playagain.lower() == "y":
            return play_guess_number()
        else:
            print("\nNICEE")
            print("Thank you for playing!\n")
            if __name__ == "__main__":
                sys.exit(f"Bye {name}!")
            else:
                return
            
    return play_guess_number



if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience."
    )
    
    parser.add_argument(
        '-n', '--name', metavar='name',
        required=True, help='The name of the player.'
    )

    args = parser.parse_args()

    guess_my_number = guess_number(args.name)
    guess_my_number()