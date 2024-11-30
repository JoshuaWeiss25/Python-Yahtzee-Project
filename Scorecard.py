import pickle

def new_scorecard(player_num):
    filename="./Scorecards/Player"+str(player_num)+"_Score.pkl"
    with open(filename,"wb") as file:
        score_dict = {
            "1s":[False,0],             # list contains a boolean and an int
            "2s":[False,0],             # the boolean is wheather or not the "row" has been played yet
            "3s":[False,0],             # the int is the score in the row; 0 until the row has been played
            "4s":[False,0],
            "5s":[False,0],
            "6s":[False,0],
            "3of":[False,0],
            "4of":[False,0],
            "FH":[False,0],
            "SmS":[False,0],
            "LgS":[False,0],
            "Yah":[False,0],
            "Cha":[False,0]
        }
        pickle.dump(score_dict,file)

def get_SC(player_num):                        #returns all data from specified scorecard
    filename="./Scorecards/Player"+str(player_num)+"_Score.pkl"
    with open(filename,"rb") as file:
        return pickle.load(file)

def edit_SC(player_num,row,data):              #replaces with new data at specified row in specified scorecard          
    filename="./Scorecards/Player"+str(player_num)+"_Score.pkl"
    scorecard={}                            #make temp var
    scorecard=get_SC(player_num)        #opens the file and saves it to a temp var
    scorecard[row]=data                     #Edit scorecard
    with open(filename,"wb") as file:
        pickle.dump(scorecard,file)         #saves the temp var by overwriting file

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def row_1s(player_num,dice):
    ##calculate score
    score=dice.count(1)*1
    ##save the score
    if not get_SC(player_num)["1s"][0]:        #run only if the row hasn't been scored before
        edit_SC(player_num,"1s",[True,score])
        print(f"You played a {score} in your Aces.")
        return True
    else:
        return False

def row_2s(player_num,dice):
    ##calculate score
    score=dice.count(2)*2
    ##save the score
    if not get_SC(player_num)["2s"][0]:        #run only if the row hasn't been scored before
        edit_SC(player_num,"2s",[True,score])
        print(f"You played a {score} in your Twos.")
        return True
    else:
        return False

def row_3s(player_num,dice):
    ##calculate score
    score=dice.count(3)*3
    ##save the score
    if not get_SC(player_num)["3s"][0]:        #run only if the row hasn't been scored before
        edit_SC(player_num,"3s",[True,score])
        print(f"You played a {score} in your Threes.")
        return True
    else:
        return False

def row_4s(player_num,dice):
    ##calculate score
    score=dice.count(4)*4
    ##save the score
    if not get_SC(player_num)["4s"][0]:        #run only if the row hasn't been scored before
        edit_SC(player_num,"4s",[True,score])
        print(f"You played a {score} in your Fours.")
        return True
    else:
        return False

def row_5s(player_num,dice):
    ##calculate score
    score=dice.count(5)*5
    ##save the score
    if not get_SC(player_num)["5s"][0]:        #run only if the row hasn't been scored before
        edit_SC(player_num,"5s",[True,score])
        print(f"You played a {score} in your Fives.")
        return True
    else:
        return False

def row_6s(player_num,dice):
    ##calculate score
    score=dice.count(6)*6
    ##save the score
    if not get_SC(player_num)["6s"][0]:        #run only if the row hasn't been scored before
        edit_SC(player_num,"6s",[True,score])
        print(f"You played a {score} in your Sixes.")
        return True
    else:
        return False

def row_3of(player_num,dice):
    score=0
    for i in range(6):
        if dice.count(i+1)>=3:
            score=sum(dice)
            break
    if not get_SC(player_num)["3of"][0]:        #run only if the row hasn't been scored before
        edit_SC(player_num,"3of",[True,score])
        print(f"You played a {score} in your Three of a Kind.")
        return True
    else:
        return False
        
def row_4of(player_num,dice):
    score=0
    for i in range(6):
        if dice.count(i+1)>=4:
            score=sum(dice)
            break
    if not get_SC(player_num)["4of"][0]:        #run only if the row hasn't been scored before
        edit_SC(player_num,"4of",[True,score])
        print(f"You played a {score} in your Four of a Kind.")
        return True
    else:
        return False

def row_FH(player_num,dice):
    doub=0
    trip=0
    score=0
    for i in range(6):
        if dice.count(i+1)==3:
            trip=i+1
        if dice.count(i+1)==2:
            doub=i+1
    if doub!=0 and trip!=0:
        score=25
    if not get_SC(player_num)["FH"][0]:        #run only if the row hasn't been scored before
        edit_SC(player_num,"FH",[True,score])
        print(f"You played a {score} in your Full House.")
        return True
    else:
        return False

def row_SmS(player_num,dice):
    score=0
    dice.sort()
    dice=list(set(dice))            #gets rid of duplicates
    if dice==[1,2,3,4] or dice==[2,3,4,5] or dice==[3,4,5,6]:
        score=30
    if not get_SC(player_num)["SmS"][0]:        #run only if the row hasn't been scored before
        edit_SC(player_num,"SmS",[True,score])
        print(f"You played a {score} in your Small Straight.")
        return True
    else:
        return False

def row_LgS(player_num,dice):
    dice.sort()
    score=0
    if dice==[1,2,3,4,5] or dice==[2,3,4,5,6]:
        score=40
    if not get_SC(player_num)["LgS"][0]:        #run only if the row hasn't been scored before
        edit_SC(player_num,"LgS",[True,score])
        print(f"You played a {score} in your Large Straight.")
        return True
    else:
        return False

def row_Yah(player_num,dice):
    score=0
    for i in range(6):
        if dice.count(i+1)==5:
            score=50
            break
    if not get_SC(player_num)["Yah"][0]:        #run only if the row hasn't been scored before
        edit_SC(player_num,"Yah",[True,score])
        print(f"You played a {score} in your Yahtzee.")
        return True
    else:
        return False

def row_Cha(player_num,dice):
    score=sum(dice)
    if not get_SC(player_num)["Cha"][0]:        #run only if the row hasn't been scored before
        edit_SC(player_num,"Cha",[True,score])
        print(f"You played a {score} in your Chance.")
        return True
    else:
        return False






#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## EVERYTHING BELLOW IS FOR TESTING
'''
def sample_edit_pkl(player_num):                        #SAMPLE on how to edit a pkl file
    filename="./Scorecards/Player"+str(player_num)+"_Score.pkl"
    scorecard={}                                        #make temp var
    with open(filename,"rb") as file:
        scorecard=pickle.load(file)                     #opens the file and saves it to a temp var
    
    ##Edit scorecard
    scorecard["1s"][0]=True
    scorecard["1s"][1]=3
    ##
   
    with open(filename,"wb") as file:
        pickle.dump(scorecard,file)                     #saves the temp var by overwriting file

import sys
def main():
    new_scorecard(sys.argv[1])
    print(get_SC(sys.argv[1]))
    
    edit_SC(sys.argv[1],"2s",[True,3])
    print(get_SC(sys.argv[1]))

    row_1s(sys.argv[1],[1,4,1,1,1])
    print(get_SC(sys.argv[1]))


    row_1s(sys.argv[1],[1,4,1,1,1])

    row_3of(sys.argv[1],[4,2,4,4,4])
    print(get_SC(sys.argv[1])["3of"])

    row_FH(sys.argv[1],[2,2,4,4,4])
    print(get_SC(sys.argv[1])["FH"])

    for i in get_SC(sys.argv[1]):
        print(f"{i} = {get_SC(sys.argv[1])[i]}")

if __name__ == "__main__":
    main()
'''
