from tkinter import *
from tkinter.messagebox import *
from itertools import permutations

def win_cond(terminate,player1,player2):
    poss_1=permutations([1,2,3])
    poss_2=permutations([4,5,6])
    poss_3=permutations([7,8,9])
    poss_4=permutations([1,4,7])
    poss_5=permutations([2,5,8])
    poss_6=permutations([3,6,9])
    poss_7=permutations([1,5,9])
    poss_8=permutations([3,5,7])
    
    for i in poss_3,poss_4,poss_2,poss_1,poss_5,poss_6,poss_7,poss_8:
        for j in list(i):
            play1=all(poss in player1 for poss in j)
            play2=all(poss in player2 for poss in j)

            if play1:
                showinfo("RESULT - ","Player 1 WINS. !!!")
                terminate=True
                return terminate
            elif play2:
                showinfo("RESULT - ","Player 2 WINS. !!!")
                terminate=True
                return terminate
            # temp_var=0
            # for value in keypress_count.values():
            #     if value==1:
            #         temp_var=1
            #     else:
            #         temp_var=0
            #         break
            # if temp_var==1:
            #     showinfo("RESULT - ","It's a DRAW. !!!")
            #     terminate=True
            #     return terminate
