# Updated Animation Starter Code

from tkinter import *

####################################
# customize these functions
####################################

def readFile(path):
    with open(path, "rt") as f:
        return f.read()

def writeFile(path, contents):
    with open(path, "wt") as f:
        f.write(contents)

def init(data):
    data.rows = 12
    data.cols = 64
    data.boxW = 20
    data.boxH = 20
    data.board = createMap(data)
    data.entry = 1
    generateFloor(data.board)
    #data.board = readFile("levels/level1")
    # load data.xyz as appropriate
    pass

def readFromString(board):
    board = board[1:-1]
    tempBoard = []
    for char in board:
        if(char == "["):
            tempList = []
        if(char == "0" or char == "1"):
            tempList.append(int(char))
        elif(ord(char) >= 97 and ord(char) <= 122):
            tempList.append(char)
        if(char == "]"):
            tempBoard.append(tempList)
    return tempBoard



def createMap(data):
    tempMap = [[0] * data.cols for i in range(data.rows)]
    return tempMap

def generateFloor(newMap):
    for i in range(1, 3):
        newMap[-1 * i] = [1] * len(newMap[0])

def mousePressed(event, data):
    col = event.x//data.boxW
    row = event.y//data.boxH
    #print(row, col)
    if(type(data.entry) == int):
        data.board[row][col] =  int(not data.board[row][col]) 
    else:
        data.board[row][col] = data.entry
    # use event.x and event.y
    pass

def keyPressed(event, data):
    if (event.keysym == "space"):
        print(data.board)
        writeFile("levels/level6", str(data.board))
    if(event.keysym == "s"):
        data.entry = "s"
    if(event.keysym == "o"):
        data.entry = "o"
    if(event.keysym == "m"):
        data.entry = "m"
    if(event.keysym == "t"):
        data.entry = "t"
    if(event.keysym == "b"):
        data.entry = "b"
    if(event.keysym == "x"):
        data.entry = "x"
    if(event.keysym == "1"):
        data.entry = 1
    # use event.char and event.keysym
    pass

def timerFired(data):
    pass

def redrawAll(canvas, data):
    for i in range(len(data.board)):
        for j in range(len(data.board[i])):
            if(data.board[i][j] == 1):
                color = "green"
            elif(data.board[i][j] == "s"):
                color = "red"
            elif(data.board[i][j] == "o"):
                color = "blue"
            elif(data.board[i][j] == "m"):
                color = "yellow"
            elif(data.board[i][j] == "t"):
                color = "orange"
            elif(data.board[i][j] == "b"):
                color = "purple"
            elif(data.board[i][j] == "x"):
                color = "black"
            else:
                color = None
            canvas.create_rectangle(j*data.boxW, i*data.boxH, (j+1)*data.boxW, (i+1)*data.boxH, fill = color)
    # draw in canvas
    pass

####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(1280, 240)