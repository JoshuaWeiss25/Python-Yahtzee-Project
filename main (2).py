import Dice
import Scorecard as SC
import SC_print as Table
import sys

#implements the UserGuide.txt/the rules into the game: you have a choice of displaying them or not
def display_rules(filename):
    rules = input("Would you like to display the rules of Yahtzee? (Y/N): ")
    if rules.lower().strip() in ["yes", "y", "sure", "ye", "ofc", "yup"]:
        with open(filename,'r') as file:
            for line in file:
                print(line)
        play_yahtzee()
    elif rules.lower().strip() in ["no","n","nope"]:
        play_yahtzee()
    else:
        print("Invalid response, please try again.")
        display_rules(filename)

def play_yahtzee():
    D=Dice.Dice()                   #initialize the dice class as D
    valid_in0=False                 #here to line 23 will keep asking "How many players: " until valid input
    while not valid_in0:    
        try:
            num_players = int(input("How many players: "))
            if num_players<0:
                raise ValueError
            if num_players==0:
                sys.exit()
            if num_players>15:
                verify=input("Are you sure? High numbers of players can have unintended consequences. See UserGuide.txt for more info. (Y/N):")
                if verify.lower().strip() in ["no","n","nope"]:
                    print("Exiting game.")
                    sys.exit()
            if num_players>=50:
                verify=input("Are you REALLY SURE? (Y/N):")
                if verify.lower().strip() in ["no","n","nope"]:
                    print("Exiting game.")
                    sys.exit()
            if num_players>=100:
                verify=input("Triple checking - ARE YOU REALLY SURE? You are trying to play with 100(or more) players. At this point we give no garuntee that the program will run properly, but we won't stop you from trying. (Y/N):")
                if verify.lower().strip() in ["no","n","nope"]:
                    print("Exiting game.")
                    sys.exit()
            if num_players>=200:
                verify=input("Really? 200 or more players? Okay, you are crazy. ARE YOU REALLY REALLY REALLY SURE?(Y/N):")
                if verify.lower().strip() in ["no","n","nope"]:
                    print("Exiting game.")
                    sys.exit()
            valid_in0=True
            
        except:
            print("Invalid input. Please try again")
    for i in range(num_players):        #create new blank scorecards for each player (or overwrite old ones)
        try:
            SC.new_scorecard(i+1)
        except OSError:
            print("Too many players, or other error when creating scorecards, such as not enough disk space. Ending program.")      #no other choice, could not find a way to keep runing the program, so have to exit
            sys.exit()
    
    table=Table.SCtable(num_players) #makes the scorecard table

    for i in range(13):                 #13 rounds
        for player_r in range(num_players):     #cycles through the players for each round
            player=player_r+1
            
            print(f'Player {player}, it is your turn!')
            is_rolling = True
            turn = 0
            
            print("Scorecard:")
            table.printTable()

            while (is_rolling == True) and (turn <= 2):
                turn += 1
                print("\nRolling dice...")
                if turn == 1:
                    D.reset() # need to take in the rolled number
                    
                print(f'You rolled {D.current}!') # CHANGE: this to label each die with an index number
                
                
                
                if turn<3:
                    valid_in1=False                     #here to line 101 will keep asking "Roll again? (Y/N): " until valid input
                    while not valid_in1:
                        player_input = input("Roll again? (Y/N): ")
                        if player_input.lower().strip() in ["yes", "y", "sure", "ye", "ofc", "yup"]:
                            valid_in1=True
                            is_rolling == True
                            valid_in2=False             #here to line 74 will keep asking "How many players: " until valid input
                            max=0
                            while not valid_in2:
                                try:
                                    max_in=input("How many dice do you want to want to keep: ")
                                    if max_in.lower()=="exit":
                                        print("Exiting game.")
                                        sys.exit()
                                    max = int(max_in.strip())
                                    if max>5 or max<0:
                                        raise ValueError
                                    valid_in2=True
                                except ValueError:
                                    print("Invalid input. Please try again.")
                            
                            usr_list = []
                            for j in range(max):
                                valid_in3=False        #here to line 91 will keep asking "How many players: " until valid input
                                while not valid_in3:
                                    try:
                                        dice_num_in=input("Which die number do you wish to keep: ")
                                        if dice_num_in.lower()=="exit":
                                            print("Exiting game.")
                                            sys.exit()
                                        dice_num = int(dice_num_in.strip())
                                        if dice_num>6 or dice_num<0:
                                            raise ValueError
                                        usr_list.append(dice_num)
                                        valid_in3=True
                                    except ValueError:
                                        print("Invalid input. Please try again.")

                            D.reroll(usr_list)
                        elif player_input.lower().strip() in ["no","n","nope"]:
                            is_rolling = False
                            valid_in1=True
                        elif player_input.lower()=="exit":                  # A built-in way to end the game
                            print("Exiting game.")
                            sys.exit()
                        else:
                            print("Invalid input. Please try again.")
                    

            valid_in4=False
            while not valid_in4: #run match case until valid input
                not_alr_played=False
                usr_input=input("What row would you like to play this in? ").lower()
                match usr_input:
                    case "1s":
                        not_alr_played=SC.row_1s(player,D.current)
                    case "2s":
                        not_alr_played=SC.row_2s(player,D.current)
                    case "3s":
                        not_alr_played=SC.row_3s(player,D.current)
                    case "4s":
                        not_alr_played=SC.row_4s(player,D.current)
                    case "5s":
                        not_alr_played=SC.row_5s(player,D.current)
                    case "6s":
                        not_alr_played=SC.row_6s(player,D.current)
                    case "3ofk":
                        not_alr_played=SC.row_3of(player,D.current)
                    case "4ofk":
                        not_alr_played=SC.row_4of(player,D.current)
                    case "fh":
                        not_alr_played=SC.row_FH(player,D.current)
                    case "sms":
                        not_alr_played=SC.row_SmS(player,D.current)
                    case "lgs":
                        not_alr_played=SC.row_LgS(player,D.current)
                    case "yah":
                        not_alr_played=SC.row_Yah(player,D.current)
                    case "cha":
                        not_alr_played=SC.row_Cha(player,D.current)
                    case "exit":
                        print("Exiting game.")
                        sys.exit()
                    case _:
                        print("Invalid input. Please try again with one of the following inputs:\n1s; 2s; 3s; 4s; 5s; 6s; 3ofK; 4ofK; FH; SmS; LgS; Yah; Cha")
                        continue
                
                
                if not_alr_played:      #breaks out of the loop if you select a valid choice
                    valid_in4=True
                else:                   #if you tried to play something that was already played, yell at user for being stupid and give them another chance to not be stupid
                    print("You've already played that row. Please try another row.")

    table.printTable()
                                #ADD: Anounce the winner
    if table.grandTotal.count(max(table.grandTotal))==1:        #if there isn't a tie...
        winner=table.grandTotal.index(max(table.grandTotal))+1
        print(f"The winner is player {winner}! Congragulations player {winner}!")
    else:
        final_scores=table.grandTotal
        winners = []       
        for num in range(len(final_scores)):
            if final_scores[num] == max(table.grandTotal):
                winners.append(num+1)
        print("There is a tie between the following players:") 
        for i in winners:
            print(f"Player {i}")

def main():

    filename = 'UserGuide.txt'
    display_rules(filename)
    
    
if __name__ == "__main__":
    main()
