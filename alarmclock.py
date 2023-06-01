#Importing all the necessary libraries to form the alarm clock:
from tkinter import *
import datetime
import time
import threading
from playsound import playsound
import pygame
# from tkinter import messagebox
# import winsound

current_time=None
now=None
threadlocal = threading.local()
stopsound=None

def stopalarm():
    global stopsound
    # playsound.stop()
    # winsound.PlaySound(None, winsound.SND_PURGE)
    pygame.mixer.music.stop()
    pygame.exit()
    # stopsound.destroy()

def timeup_notification(time):
    # messagebox.showinfo("Notification", "Your time has come.\nIt is "+str(time))
    notification = Toplevel()
    notification.title("Notification")
    notification.geometry("300x100")

    label = Label(notification, text="\nYour time has come.\nIt is "+str(time)+"\n")
    label.pack(pady=20)

    # Destroy the notification after 2.25 seconds
    notification.after(2250, notification.destroy)

def timeset_notification(time):
    # messagebox.showinfo("Notification", "Your time has come.\nIt is "+str(time))
    notification = Toplevel()
    notification.title("Notification")
    notification.geometry("300x100")

    label = Label(notification, text="Your timer is set to "+str(time))
    label.pack(pady=20)

    # Destroy the notification after 1.25 seconds
    notification.after(1250, notification.destroy)

def alarm(set_alarm_timer):
    global clock
    global stopsound
    
    threadlocal.selectedtheme = clicked.get()
    date = current_time.strftime("%d/%m/%Y")
    print("\nNew timer has been set.")
    print("The Set Date is:",date)
    print("The Set Time is:",set_alarm_timer,"\n")
    while True:
        time.sleep(1)
        if now == set_alarm_timer:
            pygame.init()
            print("Your time has come.\nIt is",set_alarm_timer)
            if threadlocal.selectedtheme == "default":
                pygame.mixer.music.load('default.mp3')
                # winsound.PlaySound('default.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
                # SND_FILENAME flag indicates the string is a filename
                # SND_ASYNC flag indicates to play the sound asynchronously
                # playsound('default.mp3')
            elif threadlocal.selectedtheme == "pleasant":
                # playsound('pleasant.mp3')
                pygame.mixer.music.load('pleasant.mp3')
            elif threadlocal.selectedtheme == "rock":
                # playsound('rock.mp3')
                pygame.mixer.music.load('rock.mp3')
            else:
                pygame.quit()
                break
            pygame.mixer.music.play()
            notification_thread=threading.Thread(target=timeup_notification, args=(set_alarm_timer,),daemon=True)
            notification_thread.start()
            break

def displaycurrenttime():
    print("The current time is")
    global current_time
    global now
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        print(now)

def settheme(selection):
    clicked.set(selection)

def callalarm():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    notification_thread=threading.Thread(target=timeset_notification, args=(set_alarm_timer,),daemon=True)
    notification_thread.start()
    alarm_thread = threading.Thread(target=alarm, args=(set_alarm_timer,), daemon=True)
    # Setting daemon as True makes the thread quit when all the main processes have finished execution
    # Extra , after 1st arg is to ensure only 1 arguement is passed
    alarm_thread.start()

clock = Tk()

print("{ Alarm Clock is now active }")
currenttime_thread=threading.Thread(target=displaycurrenttime, daemon=True)
currenttime_thread.start()
# Path to your alarm image
bg = PhotoImage(file=r"C:\\Users\\Ramith\\Projects\\Python Alarm Clock Project\\alarm.png")
bglab = Label(clock, image=bg,bg ="#5cc2d6")
bglab.place(x=0, y=0, relwidth=1, relheight=1)

clock.title("Alarm Clock")
clock.geometry("400x200")
time_format=Label(clock, text= "Enter time in 24 hour format!", fg="red",bg="black",font="Arial").place(x=640,y=340)
addTime = Label(clock,text = "Hour                   Min                  Sec",font=60).place(x = 630,y = 270)
setYourAlarm = Label(clock,text = "When do you want to set the timer to",fg="purple",font=("Italic",10,"bold")).place(x=350, y=300)

# The Variables we require to set the alarm(initialization):
hour = StringVar()
min = StringVar()
sec = StringVar()

#Time required to set the alarm clock:
options = ["default","pleasant","rock"]
clicked =StringVar()
clicked.set("Select theme")
drop = OptionMenu(clock,clicked,*options,command=settheme)
drop.pack(pady=20)

hourTime= Entry(clock,textvariable = hour,bg = "lavender",width = 15).place(x=600,y=300)
minTime= Entry(clock,textvariable = min,bg = "orange",width = 15).place(x=700,y=300)
secTime = Entry(clock,textvariable = sec,bg = "yellow",width = 15).place(x=800,y=300)

#To take the time input by user:
submit = Button(clock,text = "Set Alarm",fg="purple",width = 20,command = callalarm).place(x =700,y=370)
stopsound = Button(clock,text = "Stop Alarm",fg="red",width = 20,command = stopalarm).place(x =700,y=420)
clock.state('zoomed')   #to maximize window
clock.mainloop()
#Execution of the window.