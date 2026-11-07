"""Snake, Water, Gun: a command-line game against the computer.

Rules
-----
- Snake drinks Water  -> Snake wins
- Water drowns Gun    -> Water wins
- Gun shoots Snake    -> Gun wins

Each choice is encoded as a number (Snake = 1, Water = -1, Gun = 0).
With that encoding, the winner can be found from a single subtraction
instead of checking all six win/lose combinations one by one.
"""

import random

SNAKE, WATER, GUN = 1, -1, 0

CHOICES = {"s": SNAKE, "w": WATER, "g": GUN}
NAMES = {SNAKE: "Snake", WATER: "Water", GUN: "Gun"}


def decide_winner(you: int, computer: int) -> str:
    """Return 'draw', 'win' or 'lose' from the player's point of view.

    (computer - you) is -1 or 2 only when the computer wins:
        Snake(1) vs Gun(0)    -> 0 - 1  = -1  (Gun beats Snake)
        Water(-1) vs Snake(1) -> 1 - -1 =  2  (Snake beats Water)
        Gun(0) vs Water(-1)   -> -1 - 0 = -1  (Water beats Gun)
    Every other non-zero difference means the player wins.
    """
    if you == computer:
        return "draw"
    return "lose" if (computer - you) in (-1, 2) else "win"


def get_player_choice() -> int | None:
    """Ask until the player types s, w, g, or q to quit."""
    while True:
        raw = input("Your move [s]nake, [w]ater, [g]un or [q]uit: ").strip().lower()
        if raw == "q":
            return None
        if raw in CHOICES:
            return CHOICES[raw]
        print("Invalid input. Please type s, w, g or q.")


def main() -> None:
    score = {"win": 0, "lose": 0, "draw": 0}
    print("=== Snake, Water, Gun ===")

    while True:
        you = get_player_choice()
        if you is None:
            break

        computer = random.choice(list(NAMES))
        result = decide_winner(you, computer)
        score[result] += 1

        print(f"You chose {NAMES[you]}, computer chose {NAMES[computer]}.")
        print({"win": "You win!", "lose": "You lose!", "draw": "It's a draw."}[result])
        print(f"Score -> Wins: {score['win']} | Losses: {score['lose']} | Draws: {score['draw']}\n")

    print(f"Final score -> Wins: {score['win']} | Losses: {score['lose']} | Draws: {score['draw']}")
    print("Thanks for playing!")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nGame closed. Bye!")
