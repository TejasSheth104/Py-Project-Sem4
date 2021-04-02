from tkinter import *
from tkinter.messagebox import *
from TicTacToe import key_press

def draw_grid(window,p_val,counter,terminate,player1,player2,keypress_count):
    place_value1, place_value2, place_value3=StringVar(), StringVar(), StringVar()
    place_value4, place_value5, place_value6=StringVar(), StringVar(), StringVar()
    place_value7, place_value8, place_value9=StringVar(), StringVar(), StringVar()

    grid_but1=Button(window, textvariable=place_value1, width=10,height=4, command=lambda: key_press.key_press(window,p_val,terminate,1,"",place_value1))
    grid_but1.grid(row=5,column=1)
    grid_but2=Button(window, textvariable=place_value2, width=10,height=4, command=lambda: key_press.key_press(window,p_val,terminate,2,"",place_value2))
    grid_but2.grid(row=5,column=2)
    grid_but3=Button(window, textvariable=place_value3, width=10,height=4, command=lambda: key_press.key_press(window,p_val,terminate,3,"",place_value3))
    grid_but3.grid(row=5,column=3)
    grid_but4=Button(window, textvariable=place_value4, width=10,height=4, command=lambda: key_press.key_press(window,p_val,terminate,4,"",place_value4))
    grid_but4.grid(row=6,column=1)
    grid_but5=Button(window, textvariable=place_value5, width=10,height=4, command=lambda: key_press.key_press(window,p_val,terminate,5,"",place_value5))
    grid_but5.grid(row=6,column=2)
    grid_but6=Button(window, textvariable=place_value6, width=10,height=4, command=lambda: key_press.key_press(window,p_val,terminate,6,"",place_value6))
    grid_but6.grid(row=6,column=3)
    grid_but7=Button(window, textvariable=place_value7, width=10,height=4, command=lambda: key_press.key_press(window,p_val,terminate,7,"",place_value7))
    grid_but7.grid(row=7,column=1)
    grid_but8=Button(window, textvariable=place_value8, width=10,height=4, command=lambda: key_press.key_press(window,p_val,terminate,8,"",place_value8))
    grid_but8.grid(row=7,column=2)
    grid_but9=Button(window, textvariable=place_value9, width=10,height=4, command=lambda: key_press.key_press(window,p_val,terminate,9,"",place_value9))
    grid_but9.grid(row=7,column=3)
