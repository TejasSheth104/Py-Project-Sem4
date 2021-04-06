from tkinter import *
from TicTacToe import key_press

def draw_grid(window,button_play1,button_play2):
# 9 variables to set Button Value later (X/O)
    place_value1, place_value2, place_value3=StringVar(), StringVar(), StringVar()
    place_value4, place_value5, place_value6=StringVar(), StringVar(), StringVar()
    place_value7, place_value8, place_value9=StringVar(), StringVar(), StringVar()

    grid_but1=Button(window, textvariable=place_value1, bg="papaya whip", font=('arial',10,'bold'), relief="sunken", bd=10, width=10,height=4, command=lambda: key_press.key_press(window,1,place_value1,button_play1,button_play2))
    grid_but1.grid(row=5,column=1)
    
    grid_but2=Button(window, textvariable=place_value2, bg="papaya whip", font=('arial',10,'bold'), relief="sunken", bd=10, width=10,height=4, command=lambda: key_press.key_press(window,2,place_value2,button_play1,button_play2))
    grid_but2.grid(row=5,column=2)
    
    grid_but3=Button(window, textvariable=place_value3, bg="papaya whip", font=('arial',10,'bold'), relief="sunken", bd=10, width=10,height=4, command=lambda: key_press.key_press(window,3,place_value3,button_play1,button_play2))
    grid_but3.grid(row=5,column=3)
    
    grid_but4=Button(window, textvariable=place_value4, bg="papaya whip", font=('arial',10,'bold'), relief="sunken", bd=10, width=10,height=4, command=lambda: key_press.key_press(window,4,place_value4,button_play1,button_play2))
    grid_but4.grid(row=6,column=1)
    
    grid_but5=Button(window, textvariable=place_value5, bg="papaya whip", font=('arial',10,'bold'), relief="sunken", bd=10, width=10,height=4, command=lambda: key_press.key_press(window,5,place_value5,button_play1,button_play2))
    grid_but5.grid(row=6,column=2)
    
    grid_but6=Button(window, textvariable=place_value6, bg="papaya whip", font=('arial',10,'bold'), relief="sunken", bd=10, width=10,height=4, command=lambda: key_press.key_press(window,6,place_value6,button_play1,button_play2))
    grid_but6.grid(row=6,column=3)
    
    grid_but7=Button(window, textvariable=place_value7, bg="papaya whip", font=('arial',10,'bold'), relief="sunken", bd=10, width=10,height=4, command=lambda: key_press.key_press(window,7,place_value7,button_play1,button_play2))
    grid_but7.grid(row=7,column=1)
    
    grid_but8=Button(window, textvariable=place_value8, bg="papaya whip", font=('arial',10,'bold'), relief="sunken", bd=10, width=10,height=4, command=lambda: key_press.key_press(window,8,place_value8,button_play1,button_play2))
    grid_but8.grid(row=7,column=2)
    
    grid_but9=Button(window, textvariable=place_value9, bg="papaya whip", font=('arial',10,'bold'), relief="sunken", bd=10, width=10,height=4, command=lambda: key_press.key_press(window,9,place_value9,button_play1,button_play2))
    grid_but9.grid(row=7,column=3)
