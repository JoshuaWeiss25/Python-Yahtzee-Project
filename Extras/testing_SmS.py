#This file is not needed for game operation. File not used, for testing purposes only.

#the purpose of this file was to test detecting a small straight (which was the bane of our existance).
#other files have more testing code at the bottom of the file
import Scorecard as SC
import SC_print as Table
import Dice


def main():
    player = 1
    SC.new_scorecard(1)
    D=Dice.Dice()
    D.current=[4, 3, 1, 2, 6]

    if SC.row_SmS(player,D.current):
        print("Works!")
    else:
        print("blech")
    
    SC.new_scorecard(1)
    D.current=[1, 5, 3, 2, 4]
    if SC.row_SmS(player,D.current):
        print("Works!")
    else:
        print("No Work :(")

if __name__=="__main__":
    main()
