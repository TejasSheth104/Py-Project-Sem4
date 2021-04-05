from tkinter import *
from TicTacToe import draw_grid

def main_body():
    window=Tk()
    window.title("Tic Tac Toe")
    window.geometry("300x400")

# Highlighted Button, implies that players turn to play.
    button_play1=Button(window, text="Player1 = 'X'", width=20,height=1)
    button_play1.grid(row=1, columnspan=4)

    button_play2=Button(window, text="Player2 = 'O'", width=20,height=1,state=DISABLED)
    button_play2.grid(row=2, columnspan=4)

# a 3x3 grid to play on.
# passing button1 and button2 as parameters to help toggle at every chance.
    draw_grid.draw_grid(window,button_play1,button_play2)

# exit button to terminate program immediately
    quit_button=Button(window, text="EXIT", command=window.destroy, width=20,height=1)
    quit_button.grid(row=10, columnspan=4)

    window.mainloop()

# starting of the program.
if __name__ == '__main__':
    main_body()
