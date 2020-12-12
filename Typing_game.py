############################   Variables  ##########################################################
score = 0
timer = 60
count = 0
sliderWord = ''
miss = 0
########################################################################################################
words = ['grapes',"mango","Parrot","Apple","yellow","Bus","Train","door","Rat","Python"]

# def labelSlider():
#     global count,sliderWord
#     text = 'Welcome to typing speed game'
#     if (count>=len(text)):
#         count = 0
#         sliderWord = ''
#     sliderWord = text[count]
#     count = count + 1
#     fontLabel.configure(text=sliderWord)
#     fontLabel.after(500,labelSlider)
    

def countDown():
    global timer,score,miss
    if timer<=10:
        timeCountLabel.configure(fg="red")
    if (timer>0):
        timer -= 1
        timeCountLabel.configure(text=timer)
        timeCountLabel.after(900,countDown)
    else:
        gamePlayDetailLabel.configure(text="Hit = {} | Miss = {} | Attempted = {} \n Total Score = {}"
                                    .format(score,miss,score+miss,score))
        rr = messagebox.askyesnocancel("Notification","Well Played!! Do you want to retry?")
        if(rr==True):
            score = 0
            timer = 60
            miss = 0
            timeCountLabel.configure(text=timer)
            wordLabel.configure(text=words[0])
            scoreCountLabel.configure(text=score)
        




def startGame(event):
    gamePlayDetailLabel.configure(text="")
    if timer == 60:
        countDown()
    global score,miss
    if (wordEntry.get() == wordLabel['text']):
        score += 1
        scoreCountLabel.configure(text=score)
    else:
        miss += 1
        print("miss: ",miss)
    random.shuffle(words)

    wordEntry.delete(0,END)
    wordLabel.configure(text = words[0])

from tkinter import *
from tkinter import messagebox
import random
############################### Root method ###################################################
root = Tk()
root.geometry("800x600+400+150")
root.configure(bg="cyan")
root.title("Typing Speed Increaser Game")
root.iconbitmap("gamepad.ico")


###############################  Label method  ##################################################
fontLabel = Label(root,text="Welcome to typing speed game",font=("Times New Roman",30,"italic bold"),
            bg="cyan",fg='red',width=30)
fontLabel.place(x=50,y=10)
#labelSlider()

random.shuffle(words)
wordLabel = Label(root,text=words[0],font=('arial',40,'bold'),bg='cyan',fg='red')
wordLabel.place(x=300,y=225)

scoreLabel = Label(root,text='Your Score: ',font =('arial',25,'bold'),bg='cyan',fg='Navy Blue')
scoreLabel.place(x=10,y=60)

scoreCountLabel = Label(root,text=score,font =('arial',25,'bold'),bg='cyan',fg='Navy Blue')
scoreCountLabel.place(x=50,y=100)

timeLabel = Label(root,text='Time Left: ',font =('arial',25,'bold'),bg='cyan',fg='Navy Blue')
timeLabel.place(x=600,y=60)

timeCountLabel = Label(root,text=timer,font =('arial',25,'bold'),bg='cyan',fg='Navy Blue')
timeCountLabel.place(x=650,y=100)

gamePlayDetailLabel = Label(root,text='Type word above and hit enter to start',
                            font=('arial',25,'bold'),bg='cyan',fg='grey')
gamePlayDetailLabel.place(x=125,y=370)

#########################################  Entry method  ################################################# 
wordEntry=Entry(root,font=('arial',25,'bold'),bd='8',justify='center')
wordEntry.place(x=190,y=315)
wordEntry.focus_set() #set the focus of the entered alphabet in center
##########################################################################################################

root.bind('<Return>',startGame)

root.mainloop() #holds the output Screen
