from tkinter import *
from tkinter.messagebox import *
from TicTacToe import chance,win_con,draw_grid

counter=0
keypress_count={1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
player1,player2=list(),list()

def limit_keypress(window,p_val,counter,terminate,player1,player2,keypress_count,box_key):
    if keypress_count[box_key]==0:
        keypress_count[box_key]=1
        return True
    else:
        return False

def key_press(window,p_val,terminate,box_num,val,place_value):
    global counter,keypress_count,player1,player2
    if limit_keypress(window,p_val,counter,terminate,player1,player2,keypress_count,box_num):
        p_val=chance.chance(window,p_val,terminate,player1,player2,keypress_count,box_num)+val
        place_value.set(p_val)
        if win_con.win_cond(window,p_val,counter,terminate,player1,player2,keypress_count):
            msg=askquestion(title="TRY AGAIN", message="WANT TO PLAY AGAIN?")
            if msg=='yes':
                terminate=False
                counter=0
                p_val=""
                player1,player2=list(),list()
                keypress_count={1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
                draw_grid.draw_grid(window,p_val,counter,terminate,player1,player2,keypress_count)
            if msg=='no':
                showinfo("EXIT","THANK YOU. !!!")
                window.destroy()
