from tkinter import *
from TicTacToe import draw_grid,win_con,key_press,chance

window=Tk()

def main_body():
    global window
    window.title("Tic Tac Toe")
    window.geometry("300x400")

    button_play1=Button(window, text="Player1 = 'X'", width=20,height=1)
    button_play1.grid(row=1, columnspan=4)
    button_play2=Button(window, text="Player2 = 'O'", width=20,height=1,state=DISABLED)
    button_play2.grid(row=2, columnspan=4)

    draw_grid.draw_grid(window,button_play1,button_play2)

    quit_button=Button(window, text="EXIT", command=window.destroy, width=20,height=1)
    quit_button.grid(row=10, columnspan=4)

    window.mainloop()

if __name__ == '__main__':
    main_body()