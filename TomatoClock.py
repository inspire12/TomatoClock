# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-05-07 21:29:11
# @Last modified by:   WuLC
# @Last Modified time: 2016-05-07 23:01:00
# @Email: liangchaowu5@gmail.com

import Tkinter
import sys
import time
import threading

from PlaySong import limit_playing_time

class TomatoClock:
    def __init__(self):
        self.minutes = 0
        self.seconds = 0
        self.rest = 0

        self.root = Tkinter.Tk()

        self.root.wm_title('Tomato Clock')
        self.root.geometry('{}x{}'.format(250, 120))
        self.root.resizable(width=False, height=False)
        #self.top.iconbitmap(r'photo/tomato.ico')

        # the frame to place the blocks
        self.frame = Tkinter.Frame(self.root)
        self.frame.pack()


        # work time block
        self.work_label = Tkinter.Label(self.frame,text='Tomato Time')
        self.work_label.grid(row=0,column=0)
        self.work_time = Tkinter.Entry(self.frame,width=5)
        self.work_time.insert(Tkinter.INSERT,'40')
        self.work_time.grid(row=0,column=1)
        self.mini_label = Tkinter.Label(self.frame,text='minutes')
        self.mini_label.grid(row=0,column=2)

        # break time block
        self.break_label = Tkinter.Label(self.frame,text='Break Time')
        self.break_label.grid(row=1,column=0)
        self.break_time = Tkinter.Entry(self.frame,width=5)
        self.break_time.insert(Tkinter.INSERT,'5')
        self.break_time.grid(row=1,column=1)
        self.mini_label_ = Tkinter.Label(self.frame,text='minutes')
        self.mini_label_.grid(row=1,column=2)


        # button
        self.b = Tkinter.Button(self.frame,text="start counting", command=self.start_count)
        self.b.grid(row=2, column=0, columnspan=3)

        # residual time block
        #self.hour = Tkinter.Label(self.frame, text='hour')
        #self.hour.grid(row=3, column=0)
        self.hour = Tkinter.Label(self.frame, width=5,text = str(self.minutes) +":" +str(self.seconds))
        self.hour.grid(row=3, column=1)
        self.mini_label_ = Tkinter.Label(self.frame, text='hour')
        self.mini_label_.grid(row=3, column=2)

        #
        # ing- always on the top
        self.root.lift
        self.root.call('wm', 'attributes', '.', '-topmost', True)
        self.root.after_idle(self.root.call, 'wm', 'attributes', '.', '-topmost', False)
        self.root.mainloop()


    def start_count(self):

        self.minutes,self.rest = int(self.work_time.get()),int(self.break_time.get())
        #print work,rest
        count = 0
        self.seconds = 0
        if(self.count_down_time()):
            print("Let's song")

        count += 1


    def count_down_time(self):
        self.minutes = abs(self.minutes)
        self.seconds -= 1
        if self.seconds < 0:
            self.seconds = 59
            self.minutes -= 1
            if self.minutes < 0:
                limit_playing_time(self.rest)
                return True

        if self.seconds >= 10:
            #print "\r%d:%2d" % (self.minutes, self.seconds)
            self.hour.config(text=str(self.minutes) +":" +str(self.seconds))
        else :
            #print "\r%d:0%d" % (self.minutes, self.seconds)
            self.hour.config(text=str(self.minutes) +":0" +str(self.seconds))
        self.root.after(1000, self.count_down_time)


if __name__ == '__main__':
    tc = TomatoClock()
