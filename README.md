# Snake, Water, Gun

A command-line version of the classic South Asian hand game, played against the computer. Built in plain Python as one of my practice projects after finishing the language basics.

```
=== Snake, Water, Gun ===
Your move [s]nake, [w]ater, [g]un or [q]uit: s
You chose Snake, computer chose Water.
You win!
Score -> Wins: 1 | Losses: 0 | Draws: 0
```

## Rules

| Move | Beats | Because |
|---|---|---|
| Snake | Water | the snake drinks the water |
| Water | Gun | the water drowns the gun |
| Gun | Snake | the gun shoots the snake |

## The interesting part: one subtraction instead of six `if` checks

My first version checked every win/lose combination with its own `elif`. Six branches, easy to get wrong.

Then I encoded the moves as numbers: **Snake = 1, Water = -1, Gun = 0**. With that encoding, `computer - you` is only ever `-1` or `2` when the computer wins. So the whole result fits in one line:

```python
return "lose" if (computer - you) in (-1, 2) else "win"
```

The unit tests check all nine possible match-ups, so the shortcut is proven, not just assumed.

## Features

- Input validation: a wrong key asks again instead of crashing
- Play as many rounds as you like, `q` to quit
- Running score of wins, losses and draws
- Game logic kept separate from input/output, so it can be tested

## Run it

Requires Python 3.10+. No external packages.

```bash
git clone https://github.com/hassanrazawebdev/snake-water-gun.git
cd snake-water-gun
python game.py
```

Run the tests:

```bash
python -m unittest -v
```

## What I practised

- Dictionaries for mapping input to values and values to names
- Pulling logic into a pure function (`decide_winner`) so it can be unit tested
- Input loops and validation
- Writing tests with `unittest`

## Ideas for next versions

- Best-of-5 match mode
- A simple computer strategy that learns from the player's past moves
