import tkinter
import tkinter.font

window = tkinter.Tk()
window.title = ('Tic-Tac-Toe')

currentplayer = 'X'

board = [[0,0,0],
         [0,0,0],
         [0,0,0]]


color_gray = '#808080'
color_red = '#FF0000'
color_blue= '#0000FF'

frame = tkinter.Frame(window)  #container for the window for organization
frame.pack()  #adds frame to the window

label = tkinter.Label(frame, text=currentplayer+"'s turn", font = ('Comic Sans MS', 20))
label.grid(row = 0 , column = 0, columnspan = 3) #places it on the top of the frame


def move_maker(row, column):
    global currentplayer

    button = board[row][column] #clicked button from board
    if button['text'] =='': #checks if button has been used
        button['text'] = currentplayer 
        button['foreground'] = color_red if currentplayer == 'X' else color_blue #text for color
        currentplayer = 'O' if currentplayer == 'X' else 'X' 
        label.config(text=currentplayer+"'s turn")
    

#creates 3x3 grid
for row in range(3): 
    for column in range(3):
        buttonn = tkinter.Button(frame, text='', font=('Comic Sans MS', 50, 'bold'), width = 2, height = 1,
                                 background= color_gray, command = lambda row=row, column=column: move_maker(row,column))
        buttonn.grid(row=row + 1, column = column) #skips row because label
        board[row][column] = tkinter.Button(frame, text ='', font=('Comic Sans MS',50,'bold')) #stores button
        board[row][column] = buttonn 


#keeps window open
window.mainloop()
