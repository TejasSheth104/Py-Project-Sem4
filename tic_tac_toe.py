from tkinter import *
from TicTacToe import draw_grid,win_con,key_press,chance

window=Tk()
p_val=""
counter=0
terminate=False
player1,player2=list(),list()
keypress_count={1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}

def main_body():
    global window,counter
    window.title("Tic Tac Toe")
    window.geometry("300x400")

    lab_def=Label(window, text="\nPlayer1 = X\nPlayer2 = O\n", width=40,height=2)
    lab_def.grid(row=2, columnspan=4)
    
    draw_grid.draw_grid(window,p_val,counter,terminate,player1,player2,keypress_count)

    quit_button=Button(window, text="EXIT", command=window.destroy, width=20,height=1)
    quit_button.grid(row=10, columnspan=4)

    window.mainloop()

if __name__ == '__main__':
    main_body()