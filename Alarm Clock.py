from tkinter import* #import for GUI interface
import datetime as dt #using dt as a nickname, this allows us to manipulate dates and times
import time #this allows us to manipulate dates and times
import winsound as ws #allow us to generate sounds for the alarm clock

def alarm(setAlarmTimer):  
    while True:  
        time.sleep(1)  
        actualTime = dt.datetime.now() #collects the current time now using the datetime(dt) from datetime module 
        currentTime = actualTime.strftime("%H : %M : %S")  #stores the time into separate variables with the specific format  
        the_message = "Current Time: " + str(currentTime)  
        print(the_message)  
        if currentTime == setAlarmTimer:  
            ws.PlaySound("sound.wav", ws.SND_ASYNC)  
            print("Time to Wake Up!")
            break  
#if the current time is equivalent to the set alarm timer and play the sound for the same using the winsound module, or else the timer continues

def getAlarmTime():  
    alarmSetTime = f"{hour.get()} : {minute.get()} : {second.get()}"  
    alarm(alarmSetTime) 
    


#creating clock GUI

guiWindow = Tk()  #instantiate an instance of a window
guiWindow.title("The Alarm Clock")  
guiWindow.geometry("464x200")  #width and height of the window
guiWindow.config(bg = "#FFDEAD")  #background color
guiWindow.resizable(width = False, height = False)  #can the height or weight of the gui window be altered



timeFormat = Label( #used to specify the container box where we can place the text or images
    #label written in the form Label(name of window/container, detail1 detail2, etc)
    guiWindow,
    text = "Remember to set time in 24-hour!",
    fg = "white", #foreground, specifies the color of text
    bg = "#D2B48C",
    font = ("Arial", 15)
    ). place(
        x = 70,
        y = 160
        )

add_time = Label(
    guiWindow,
    text = " Hour    Minute    Second",
    font = 60,
    fg = "white",
    bg = "#D2B48C"
    ).place(
        x = 220,
        y = 10
        )

setAlarm = Label(  
    guiWindow,  
    text = "Set Time for Alarm: ",  
    fg = "white",  
    bg = "#D2B48C",    
    font = ("Helevetica", 13, "bold")  
    ).place(  
        x = 5,  
        y = 50  
        )

hour = StringVar()  
minute = StringVar()  
second = StringVar()

hourTime = Entry(  
    guiWindow,  
    textvariable = hour,  
    bg = "#FEFBD8",  
    width = 4,  
    font = (20)  
    ).place(  
        x = 220,  
        y = 53  
        )

minuteTime = Entry(  
    guiWindow,  
    textvariable = minute,  
    bg = "#FEFBD8",  
    width = 4,  
    font = (20)  
    ).place(  
        x = 297,  
        y = 53  
        )

secondTime = Entry(  
    guiWindow,  
    textvariable = second,  
    bg = "#FEFBD8",  
    width = 4,  
    font = (20)  
    ).place(  
        x = 390,  
        y = 53  
        )  

submit = Button(  
    guiWindow,  
    text = "Set The Alarm",  
    fg = "white",  
    bg = "#A0522D",  
    width = 15,  
    command = getAlarmTime,  #calls the function getAlarmTime 
    font = (20)  
    ).place(  
        x = 140,  
        y = 100  
        )  
   
guiWindow.mainloop()  #place window on screen
