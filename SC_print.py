import Scorecard as SC
from tabulate import tabulate
#import sys

class SCtable:
    def __init__(self,num_players):
        self.num_players=num_players
        self.grandTotal=[]
        for i in range(num_players):
            self.grandTotal.append(0)
        #Sets up the titles of the rows
        self.board = [
            ['Aces (1s)'],           #0
            ['Twos (2s)'],           #1
            ['Threes (3s)'],         #2
            ['Fours (4s)'],          #3
            ['Fives (5s)'],          #4
            ['Sixes (6s)'],          #5
            ['Top Subtotal'],        #6
            ['Bonus'],               #7
            ['Top Total'],           #8
            [''],                    #9
            ['3 of a Kind (3ofK)'],  #10
            ['4 of a Kind (4ofK)'],  #11
            ['Full House (FH)'],     #12
            ['SM Straight (SmS)'],   #13
            ['LG Straight (LgS)'],   #14
            ['YAHTZEE (Yah)'],       #15
            ['Chance (Cha)'],        #16
            ['Bottom Total'],        #17
            ['Grand Total']          #18
        ]   
        #the header
        self.head = ['Player']

        for i in range(len(self.board)):
            for j in range(num_players):
                #This sets up that before the player has a score it is an X except for the totals and bonuses which are 0
                if not (self.board[i][0]=='' or self.board[i][0]=='Top Subtotal' or self.board[i][0]=='Bonus' or self.board[i][0]=='Top Total' or self.board[i][0]=='Bottom Total' or self.board[i][0]=='Grand Total'):
                    self.board[i].append('')
                else:
                    #empty space between top totals and bottom totals (between Top Total and 3 of a Kind)
                    self.board[i].append('') 
                    self.head.append(str(j+1))
        
    #This function updates the scorecard itself, replacing the X's with the score that the player rolled
    def update_table(self):
        for i in range(self.num_players):
            card=SC.get_SC(i+1)
            #Making it so the totals are initially 0
            topSubTotal=0
            Bonus=0
            topTotal=0
            bottomTotal=0
            if card["1s"][0]:
                self.board[0][i+1] = card["1s"][1]
                topSubTotal+=card["1s"][1]                  #allows for this score to be added to the sub total
            if card["2s"][0]:
                self.board[1][i+1] = card["2s"][1]
                topSubTotal+=card["2s"][1]
            if card["3s"][0]:
                self.board[2][i+1] = card["3s"][1]
                topSubTotal+=card["3s"][1]
            if card["4s"][0]:
                self.board[3][i+1] = card["4s"][1]
                topSubTotal+=card["4s"][1]
            if card["5s"][0]:
                self.board[4][i+1] = card["5s"][1]
                topSubTotal+=card["5s"][1]
            if card["6s"][0]:
                self.board[5][i+1] = card["6s"][1]
                topSubTotal+=card["6s"][1]
            if card["3of"][0]:
                self.board[10][i+1] = card["3of"][1]
                bottomTotal+=card["3of"][1]
            if card["4of"][0]:
                self.board[11][i+1] = card["4of"][1]
                bottomTotal+=card["4of"][1]
            if card["FH"][0]:
                self.board[12][i+1] = card["FH"][1]
                bottomTotal+=card["FH"][1]
            if card["SmS"][0]:
                self.board[13][i+1] = card["SmS"][1]
                bottomTotal+=card["SmS"][1]
            if card["LgS"][0]:
                self.board[14][i+1] = card["LgS"][1]
                bottomTotal+=card["LgS"][1]
            if card["Yah"][0]:
                self.board[15][i+1] = card["Yah"][1]
                bottomTotal+=card["Yah"][1]
            if card["Cha"][0]:
                self.board[16][i+1] = card["Cha"][1]
                bottomTotal+=card["Cha"][1]

            #In Yahtzee there is a bonus, this if detects if the player got a high enough score for the bonus
            if topSubTotal>=63:
                Bonus=35
            topTotal=topSubTotal+Bonus
            #This makes it so the totals/bonus does not have X's
            self.board[6][i+1]=topSubTotal
            self.board[7][i+1]=Bonus
            self.board[8][i+1]=topTotal
            self.board[17][i+1] = bottomTotal
            self.grandTotal[i]=bottomTotal+topTotal
            self.board[18][i+1] = self.grandTotal[i]
            
    def get_grand(self):
        return self.grandTotal
            
    def printTable(self):
        self.update_table()
        
        print(tabulate(self.board, headers=self.head, tablefmt='grid'))
        



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## EVERYTHING BELLOW IS FOR TESTING
'''
def main():
    
    num_players=int(sys.argv[1])
    for i in range(num_players):
        SC.row_1s(i+1,[1,4,1,1,1])
    T=SCtable(num_players)
    T.printTable()
    print(T.grandTotal)

if __name__ == "__main__":
    main()
'''








