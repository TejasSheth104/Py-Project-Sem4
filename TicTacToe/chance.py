from tkinter import *

def chance(window,p_val,counter,terminate,player1,player2,keypress_count,box_num):
    for box_num_value in range(1,10):
        if box_num==box_num_value:
            if counter%2!=0:
                counter+=1
                player1.append(box_num)
                return 'O',counter
            if counter%2==0:
                counter+=1
                player2.append(box_num)
                return 'X',counter
