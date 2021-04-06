from tkinter import *
from TicTacToe import draw_grid

window=Tk()

def main_body():
    global window
    window.title("Tic Tac Toe")
    window.geometry("355x445")

    terminate=False
    counter=0
    p_val=""
    player1,player2=list(),list()
    keypress_count={1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}

# Highlighted Button, implies that players turn to play.
    button_play1=Button(window, text="Player1: 'X'", font=('arial',20,'bold') ,width=20,height=1)
    button_play1.grid(row=1, columnspan=4)

    button_play2=Button(window, text="Player2: 'O'", font=('arial',20,'bold') ,width=20,height=1,state=DISABLED)
    button_play2.grid(row=2, columnspan=4)

# a 3x3 grid to play on.
# passing button1 and button2 as parameters to help toggle at every chance.
    draw_grid.draw_grid(window,button_play1,button_play2)

# exit button to terminate program immediately
    quit_button=Button(window, bg='black', fg='red', text="EXIT", command=window.destroy, font=('arial',10,'bold') ,width=10,height=1)
    quit_button.grid(columnspan=4,sticky='w')

    reset_button=Button(window, bg='black', fg='red', text="RESET", font=('arial',10,'bold') ,width=10,height=1 ,command=main_body)
    reset_button.grid(columnspan=4,sticky='e')

    window.mainloop()

# starting of the program.
if __name__ == '__main__':
    main_body()
