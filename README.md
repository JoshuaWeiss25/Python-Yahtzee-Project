Hi! My name is Josh. I took CSC 200 at URI, and this was a group project. The assignment was to make a game; my group chose to make Yahtzee.

Some more info about the game:
  - The game is entirely run and played in the terminal
  - run the game by running `main()` in `main.py`. How to do that depends where you are running it from (like what IDE you use).
  - The game can *technically* ***theoretically*** support up to the integer limit of players. The limitations are:
    - storage space
    - run time
    - screen size (for displaying the scores)
  - If it's in the `/Extras/` folder, that means it isn't needed to run the game
    - `Reflection(git).md` is a written relfection on the project based on the assignment, with the names of my two partners censored. I reflect on the process of making the game and the challenges I faced. Might be worth a read, there is a funny story or two in there.
    - `testing.py` is a file where I manualy constructed scorecards to test certain blocks of code. keeping it for a history. not needed to run the game at all.
  - rules and syntax to play the game can be found in `UserGuide.txt` (which can be printed to terminal at the begining of game)




There are a couple things that I didn't get the chance to do here and I might revisit in the future if I have the time.
- Save states
  - becasue of the way I saved the scores, the game lends itself to being able to continue a previous game
  - I just need to save the state of the game (Round number, player number) and learn/figure out how to start the loops in the middle
- Yahtzee Bonus: what happens when you get yahtzee multiple times
- Revamp the user interface for rolling the dice. It's weird and not very intuitive
- fix the weird way the rules print to the terminal
