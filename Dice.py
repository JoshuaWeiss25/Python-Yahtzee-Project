from numpy import random

class Dice:

    def __init__(self):
        self.current=[1,1,1,1,1]
        self.roll_num=0
        for i in range(5):
            self.roll(i+1)
    
    def roll(self,index):            #takes the index of the list of current dice, starting from 1 instead of 0 for user experience
        num=random.randint(6)+1 #Generates number from 1-6
        self.current[index-1]=num    #Saves generated number to the list of current dice at given index
        
    def reroll(self, keep):           #takes a list of indecies of dice that player wants to keep, from 1-5 for user experience
        '''
        pickup=self.current
        for i in keep:
            try:
                pickup.remove(i)
            except:
                continue
        '''
        pickup=[]
        for k in self.current:
            pickup.append(k)
        for i in keep:
            try:
                pickup.remove(i)
            except:
                continue
        for j in pickup:
            self.roll(self.current.index(j)+1)
        self.roll_num+=1

    def reset(self):
        roll_num=0
        self.reroll([])
        



## EVERYTHING BELLOW IS FOR TESTING
'''
def main():
    test=Dice()

    
    
    

    print(test.current)




if __name__ == "__main__":
    main()
'''
