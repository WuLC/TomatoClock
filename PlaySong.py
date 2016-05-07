# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-04-27 15:14:15
# @Last modified by:   WuLC
# @Last Modified time: 2016-05-07 22:51:34
# @Email: liangchaowu5@gmail.com
# @Function: play music with pygame,and control its' playing time 

import pygame
import os
import multiprocessing

def play_mp3(mp3_file_path):
	"""play mp3 file till the end
	
	Args:
	    mp3_file_path (str): file path of mp3 file 
	
	Returns:
	    None
	"""
    # check file path
	if not os.path.isfile(mp3_file_path):
		print 'mp3 file path %s not correct'%mp3_file_path
		return 
	# play song
	pygame.mixer.init()
	pygame.mixer.music.load(mp3_file_path)
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy(): 
		#pygame.time.Clock().tick(10)
		pass


def limit_func_time(func,args,time):
	"""limit the running time of a function
	
	Args:
	    func (function): function to run
	    args (tuple): args of func ,in the form of tuple
	    time (int): limit of running time 
	
	Returns:
	    boolean: whether the running time of the function  exceeds the limit,True means not exceed
	"""
	p = multiprocessing.Process(target = func,args=args)
	p.start()
	p.join(time)
	if p.is_alive():
		p.terminate()
		return False
	return True
	
def limit_playing_time(miniutes):
	limit_func_time(play_mp3,('sound/bgm.mp3',),miniutes*60)

if __name__ == '__main__':
	mp3_file_path = 'sound/bgm.mp3'
	time = 300 # seconds
	result = limit_func_time(play_mp3, (mp3_file_path, ), time)
	if result:
		print 'finish playing the whole song'
	else:
		print 'Time out'
