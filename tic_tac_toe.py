from tkinter import *
from TicTacToe import draw_grid

window=Tk()

def show_frame(frame):
    frame.tkraise()

def submit(input_name1,input_name2,frame_main,frame_player):
    name_val1=input_name1.get()
    name_val2=input_name2.get()

    frame_player.tkraise()
#==================Frame Player code
    play_user1=Button(frame_player, text=str(name_val1+"'X'"), font=('arial',10,'bold') ,width=18,height=1)
    play_user1.grid(row=3, columnspan=4,sticky='w')

    play_user2=Button(frame_player, text=str(name_val2+"'O'"), font=('arial',10,'bold') ,width=18,height=1,state=DISABLED)
    play_user2.grid(row=3, columnspan=4,sticky='e')

    draw_grid.draw_grid(frame_player,play_user1,play_user2)

    back_main=Button(frame_player, bg='black', fg='red', text="BACK", command=lambda:show_frame(frame_main), font=('arial',10,'bold') ,width=18,height=1)
    back_main.grid(row=8,columnspan=4,sticky='nsew')

def main_body():
    global window
    window.title("Tic Tac Toe")
    window.geometry("340x400")

    frame_main=Frame(window)
    frame_player=Frame(window)
    frame_detail=Frame(window)

    for frame in (frame_main,frame_player):
        frame.grid(row=0,column=0,sticky='nsew')

#==================Frame Main code
    # First Row
    name1=Label(frame_main,text= "Player1 Name")
    name1.grid(row=1,column=2,sticky='w')
    input_name1=Entry(frame_main)
    input_name1.grid(row=1,column=3)

    # Second Row
    name2=Label(frame_main,text= "Player2 Name")
    name2.grid(row=2,column=2,sticky='w')
    input_name2=Entry(frame_main)
    input_name2.grid(row=2,column=3)

    submit_detail=Button(frame_main, text="SUBMIT", font=('arial',10,'bold') ,width=18,height=1, command=lambda: submit(input_name1,input_name2,frame_main,frame_player))
    submit_detail.grid(row=3, columnspan=4,sticky='nsew')
    
    # terminate=False
    # counter=0
    # p_val=""
    # player1,player2=list(),list()
    # keypress_count={1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}

# #==================Frame Main code
# # Highlighted Button, implies that players turn to play.
#     button_play1=Button(frame_main, text="Player1: 'X'", font=('arial',10,'bold') ,width=18,height=1)
#     button_play1.grid(row=1, columnspan=4,sticky='w')

#     button_play2=Button(frame_main, text="Player2: 'O'", font=('arial',10,'bold') ,width=18,height=1,state=DISABLED)
#     button_play2.grid(row=1, columnspan=4,sticky='e')

# # a 3x3 grid to play on.
# # passing button1 and button2 as parameters to help toggle at every chance.
#     draw_grid.draw_grid(frame_main,button_play1,button_play2)

#     # reset_button=Button(window, bg='black', fg='red', text="RESET", command=main_body, font=('arial',10,'bold') ,width=18,height=1)
#     # reset_button.grid(row=8,columnspan=4,sticky='w')

# # exit button to terminate program immediately
#     quit_button=Button(frame_main, bg='black', fg='red', text="EXIT", command=window.destroy, font=('arial',10,'bold') ,width=18,height=1)
#     quit_button.grid(row=8,columnspan=4,sticky='e')

    show_frame(frame_main)

    window.mainloop()

# starting of the program.
if __name__ == '__main__':
    main_body()
