from tkinter import *
import time

WORK_TIME = 1500
SHORT_BREAK_TIME = 300
LONG_BREAK_TIME = 900
seconds = WORK_TIME

def format_time(seconds):
     l = []
     mins = str(seconds // 60).zfill(2)
     secs = str(seconds % 60).zfill(2)
     return '{} : {}'.format(mins,secs)

#TODO:
def pause():
     global seconds
     print(format_time(seconds))

def play_timer(label):
     global seconds
     seconds -= 1
     #label.config(text = format_time(seconds))
     print(format_time(seconds))
     time.sleep(1)
     play_timer(label)



def home_page(master):
     frame = Frame(master)
     title_label = Label(frame, text = 'Pomodoro', font = ('Arial','30'), bg = '#000000', fg = '#00ff00')
     global seconds
     time_label = Label(frame,  text = format_time(seconds),font = ('Arial','30'), bg = '#000000', fg = '#00ff00')
     pause_buttton = Button(frame, text = 'Pause')
     resume_buttton = Button(frame, text = 'Resume', command = lambda: play_timer(time_label))
     title_label.grid()
     time_label.grid(row = 1)
     resume_buttton.grid(row = 2, column = 1, columnspan = 2, rowspan = 2)
     pause_buttton.grid(row = 2, column = 3, columnspan = 2, rowspan = 2)
     frame.pack()

root = Tk()
root.configure(background = '#000000')
root.geometry('500x500')
home_page(root)

root.mainloop()

# 2 min rukh haa