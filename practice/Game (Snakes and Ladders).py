import random
import time

class Player:
    def __init__(self, name=None):
        self.name = name
        self.position = 0
        self.dice = 0

    def Roll_Dice(self, snakes, ladders):
        if self.position >= 0 and self.position <= 100:
            self.dice = random.randint(1, 6)  # first roll
            print(f"\n{self.name} rolls the dice... 🎲 You got a {self.dice}! ")

            if self.position + self.dice <= 100:
                self.position += self.dice
                print(f"Your current position is: {self.position}.\n")

                Answer, move_back = snakes.CheckTrap(self.position)  # check if the player is on a snake trap
                if Answer:
                    self.position -= move_back
                    if self.position < 0:
                        self.position = 0

                    print(f"Oops! A snake bites you at position {self.position}! 🐍 You move back by {move_back} steps.")
                else:
                    print("You’re safe! 😎 No snakes in your path!")

                Ans, move_forward = ladders.CheckLadders(self.position)  # check if the player is on a ladder
                if Ans:
                    self.position += move_forward
                    print(f"Yay! You found a ladder! 🪜 You move up by {move_forward} steps. Your position is now: {self.position}.")
                else:
                    print(f"You’re on a safe square at position {self.position}. No ladders here.")
            else:
                print("You need to roll exactly to reach 100! Try again.")
        else:
            return

    def get_position(self):
        return self.position


class Snakes:
    def __init__(self):
        self.snakes = random.sample(range(2, 99), 10)

    def CheckTrap(self, position):
        for i in self.snakes:
            if i == position:
                print(f"\nYou stepped on a snake at position {position}!")
                move_back = random.randint(1, position)
                return True, move_back
        return False, 0


class Ladders:
    def __init__(self):
        self.ladders = random.sample(range(2, 99), 10)

    def CheckLadders(self, position):
        for i in self.ladders:
            if i == position:
                print(f"\nYou stepped on a ladder at position {position}!")
                move_forward = random.randint(1, 100 - position)  # Always move up
                return True, move_forward
        return False, 0


class Game_status:
    def __init__(self):
        self.position_player1 = 0
        self.position_comp = 0

    def update_status(self, player1, comp):
        self.position_player1 = player1.position
        self.position_comp = comp.position

        if self.position_player1 == 100:
            print(f"\nCongratulations! {player1.name} wins! 🎉")
            return True
        elif self.position_comp == 100:
            print(f"\nOh no! {comp.name} wins! 😱")
            return True
        else:
            return False


def Choose_player(Players):
    choice = random.choice(Players)
    print(f"\n{choice.name} is randomly selected to go first! Let’s start the game!\n")
    return choice


def main():
    print("Welcome to the Ultimate Snake and Ladder Game! 🎲🐍🪜")

    Player_name = input("Enter your player name: ")
    Player1 = Player(Player_name)
    Computer = Player("Computer")

    Players = [Player1, Computer]
    snakes = Snakes()
    ladders = Ladders()

    Current_Player = Choose_player(Players)
    print(f"\nGame starting... 🚀 {Current_Player.name}'s turn begins!\n")

    Game = Game_status()

    if Current_Player == Player1:
        Player1.Roll_Dice(snakes, ladders)
    else:
        Computer.Roll_Dice(snakes, ladders)

    # 🧠 Check winner after first move
    if Game.update_status(Player1, Computer):
        print("Game finished")
        return

    while True:
        input("Press Enter to continue to the next turn...\n")
        Status = Game.update_status(Player1, Computer)
        if Status:
            print("Game finished")
            break
        else:
            if Current_Player == Player1:
                Current_Player = Computer
            else:
                Current_Player = Player1

            print(f"\nIt’s now {Current_Player.name}'s turn!\n")
            Current_Player.Roll_Dice(snakes, ladders)
            time.sleep(1)

main()
# Redesign this and write a program where I am playing against the computer