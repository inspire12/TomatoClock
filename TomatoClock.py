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
        self.top = Tkinter.Tk()
        self.top.wm_title('Tomato Clock')
        self.top.geometry('{}x{}'.format(250, 120))
        self.top.resizable(width=False, height=False)
        #self.top.iconbitmap(r'photo/tomato.ico')

        # the frame to place the blocks
        self.frame = Tkinter.Frame(self.top)
        self.frame.pack()

        # work time block
        self.work_label = Tkinter.Label(self.frame,text='Tomato Time')
        self.work_label.grid(row=0,column=0)
        self.work_time = Tkinter.Entry(self.frame,width=5)
        self.work_time.insert(Tkinter.INSERT,'40')
        self.work_time.grid(row=0,column=1)
        self.mini_label = Tkinter.Label(self.frame,text='miniutes')
        self.mini_label.grid(row=0,column=2)

        # break time block
        self.break_label = Tkinter.Label(self.frame,text='Break Time')
        self.break_label.grid(row=1,column=0)
        self.break_time = Tkinter.Entry(self.frame,width=5)
        self.break_time.insert(Tkinter.INSERT,'5')
        self.break_time.grid(row=1,column=1)
        self.mini_label_ = Tkinter.Label(self.frame,text='miniutes')
        self.mini_label_.grid(row=1,column=2)


        # button
        self.b = Tkinter.Button(self.frame,text="start counting", command=self.start_count)
        self.b.grid(row=2, column=0, columnspan=3)
        # break time block
        self.hour = Tkinter.Label(self.frame, text='hour')
        self.hour.grid(row=3, column=0)
        self.hour = Tkinter.Entry(self.frame, width=5)
        self.hour.insert(Tkinter.INSERT, '5')
        self.hour.grid(row=3, column=1)
        self.mini_label_ = Tkinter.Label(self.frame, text='hour')
        self.mini_label_.grid(row=3, column=2)

        self.top.mainloop()


    def start_count(self):

        work,rest = self.work_time.get(),self.break_time.get()
        #print work,rest
        count = 0

        self.count_down_time(int(work), 0)
        limit_playing_time(int(rest))
        count += 1


    def count_down_time(self,miniutes,seconds):
        miniutes = abs(miniutes)
        seconds -= 1
        if seconds < 0:
            seconds = 59
            miniutes -= 1
        if seconds >= 10:
            print "\r%d:%2d" % (miniutes, seconds)
        else :
            print "\r%d:0%d" % (miniutes, seconds)
        try:
            timer = threading.Timer(1, self.count_down_time, args=[miniutes,seconds])
            timer.start()
            timer.join()
        except:
            timer.cancel()
        if miniutes <= 0:
            timer.cancel()



    def stop(self):
        self._stop.set()

if __name__ == '__main__':
    tc = TomatoClock()
