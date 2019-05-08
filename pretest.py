import pitchCode
import pygame
from tkinter import *

####################################
# customize these functions
####################################


def init(data):
	data.noteList = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
	data.currInterval = 2
	data.score = 0
	data.splash = True
	data.pre = None
	data.testNotes = []
	data.testIntervals = [2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7]
	data.currStage = 10
	data.timer = 0
	data.playing = False
	data.testOver = False
	data.timer = 0
	data.allNotes = []
	initializeNotes(data)


def initializeNotes(data):
	pygame.init()
	pygame.mixer.pre_init(44100, 16, 2, 4096)
	for note in ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]:
		data.allNotes.append(pygame.mixer.Sound("monsterNotes/" + note + ".wav"))

def initTest(data):
	if(data.pre):
		data.testNotes = [0, 3, 5, 2, 6, 7, 3, 8, 9, 5, 11, 0]
	elif not(data.pre):
		data.testNotes = [2, 5, 7, 3, 0, 6, 1, 8, 10, 9, 4, 1]

def mousePressed(event, data):
    # use event.x and event.y
    pass

def keyPressed(event, data):
	if not(data.testOver):
		if event.keysym == "1":
			data.pre = True
			data.splash = not data.splash
			data.playing = True
			initTest(data)
		elif event.keysym == "2":
			data.pre = False
			data.splash = not data.splash
			data.playing = True
			initTest(data)
		if event.keysym == "n":
			data.playing = True
			data.currStage += 1
			if(data.currStage > 11):
				data.testOver = True
		pitchCode.playNote(data.allNotes, data.testNotes[data.currStage])

def timerFired(data):
	if(data.playing):
		if(data.currStage <= 11):
			data.timer += 1
			sungNote = pitchCode.record()
			if(pitchCode.checkInterval(data.testIntervals[data.currStage],data.testNotes[data.currStage], sungNote)):
				data.score += 1
			if(data.timer % 10 == 0):
				pitchCode.playNote(data.allNotes, data.testNotes[data.currStage])
			if(data.timer % 50 == 0):
				data.playing = False
				data.timer = 0


def redrawAll(canvas, data):
	if not(data.testOver):
		if(data.splash):
			canvas.create_text(data.width//2, data.height//3, text ="IS THIS A PRE-TEST OR POST-TEST?")
			canvas.create_text(data.width//2, data.height*2//3, text = "Press 1 for Pre Test\nPress 2 for Post Test")
		elif(data.playing):
			canvas.create_text(data.width//2, data.height//3, text = "Sing a %d Interval\nStarting from %s" % (data. testIntervals[data.currStage], data.noteList[data.testNotes[data.currStage]]))
		elif not (data.playing):
			canvas.create_text(data.width//2, data.height//2, text = "PRESS N TO MOVE TO THE NEXT QUESTION")
	else:
		canvas.create_text(data.width//2, data.height//4, text = "YOUR SCORE IS:")
		canvas.create_text(data.width//2, data.height//2, text = data.score)

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

run(400, 200)