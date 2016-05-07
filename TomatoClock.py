# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-05-07 21:29:11
# @Last modified by:   WuLC
# @Last Modified time: 2016-05-07 23:01:00
# @Email: liangchaowu5@gmail.com

import Tkinter
import sys
import time

from PlaySong import limit_playing_time

class TomatoClock:
	def __init__(self):
		self.top = Tkinter.Tk()
		self.top.wm_title('Tomato Clock')   
		self.top.geometry('{}x{}'.format(250, 80))  
		self.top.resizable(width=False, height=False)
		self.top.iconbitmap(r'photo/tomato.ico')

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

		self.top.mainloop()


	def start_count(self):
		work,rest = self.work_time.get(),self.break_time.get()
		#print work,rest		
		count = 0
		while True:
			self.count_down_time(int(work))
			limit_playing_time(int(rest))
			count += 1
		

	def count_down_time(self,miniutes):
		miniutes = abs(miniutes)
		seconds = 0
		while miniutes >= 0 and seconds>=0:
			if miniutes == 0 and seconds==0:
				return 
			if seconds == 0 and miniutes > 0:
			    miniutes -= 1
			    seconds = 60
			seconds -= 1
			print "\r%s:%s" %(miniutes,seconds)
			time.sleep(1)


if __name__ == '__main__':
	tc = TomatoClock()
