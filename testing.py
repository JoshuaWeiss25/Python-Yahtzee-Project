#This file is not needed for game operation. File not used, for testing purposes only.

#the purpose of this file was to manually create scorecards and test chunks of code based on them.
#other files have more testing code at the bottom of the file


import Scorecard as SC
import SC_print as Table
import Dice




def main():
    
    d=Dice.Dice()
    for i in range(3):
        SC.new_scorecard(i+1)
    

    i=3
    SC.edit_SC(i,"1s",[True,3])
    SC.edit_SC(i,"2s",[True,6])
    SC.edit_SC(i,"3s",[True,9])
    SC.edit_SC(i,"4s",[True,12])
    SC.edit_SC(i,"5s",[True,15])
    SC.edit_SC(i,"6s",[True,18])
    SC.edit_SC(i,"3of",[True,23])
    SC.edit_SC(i,"4of",[True,24])
    SC.edit_SC(i,"FH",[True,25])
    SC.edit_SC(i,"SmS",[True,30])
    SC.edit_SC(i,"LgS",[True,40])
    SC.edit_SC(i,"Yah",[True,50])
    SC.edit_SC(i,"Cha",[True,15])

    i=2
    SC.edit_SC(i,"1s",[True,5])
    SC.edit_SC(i,"2s",[True,10])
    SC.edit_SC(i,"3s",[True,15])
    SC.edit_SC(i,"4s",[True,20])
    SC.edit_SC(i,"5s",[True,25])
    SC.edit_SC(i,"6s",[True,30])
    SC.edit_SC(i,"3of",[True,30])
    SC.edit_SC(i,"4of",[True,30])
    SC.edit_SC(i,"FH",[True,25])
    SC.edit_SC(i,"SmS",[True,30])
    SC.edit_SC(i,"LgS",[True,40])
    SC.edit_SC(i,"Yah",[True,50])
    SC.edit_SC(i,"Cha",[True,30])

    i=1
    SC.edit_SC(i,"1s",[True,5])
    SC.edit_SC(i,"2s",[True,10])
    SC.edit_SC(i,"3s",[True,15])
    SC.edit_SC(i,"4s",[True,20])
    SC.edit_SC(i,"5s",[True,25])
    SC.edit_SC(i,"6s",[True,30])
    SC.edit_SC(i,"3of",[True,30])
    SC.edit_SC(i,"4of",[True,30])
    SC.edit_SC(i,"FH",[True,25])
    SC.edit_SC(i,"SmS",[True,30])
    SC.edit_SC(i,"LgS",[True,40])
    SC.edit_SC(i,"Yah",[True,50])
    SC.edit_SC(i,"Cha",[True,30])



    table=Table.SCtable(3)


    table.printTable()

    print((table.grandTotal))
    if table.grandTotal.count(max(table.grandTotal))==1:        #if there isn't a tie...
        winner=table.grandTotal.index(max(table.grandTotal))+1
        print(f"The winner is player {winner}! Congragulations player {winner}!")
    else:
        final_scores=table.grandTotal
        print("There is a tie between the following players:") 

        winners = []       
        for num in range(len(final_scores)):
            if final_scores[num] == max(table.grandTotal):
                winners.append(num+1)

        for i in winners:
            print(f"Player {i}")


    






if __name__=="__main__":
    main()
