import numpy as np


pitches = {1:[90, 75], 2:[85, 80], 3:[80, 85], 4:[75, 90]}
swings = {1:[90, 75], 2:[85, 80], 3:[80, 85], 4:[75, 90]}

def pitch_selection():
	print('Choose a pitch:')
	print('1) Fastball')
	print('2) Change Up')
	print('3) Slider')
	print('4) Split Finger Fastball')
	pitch = int(input('Make a choice:'))
	return pitch
	
def swing_selection():
	print('Choose a swing:')
	print('1) Choke Up')
	print('2) Regular swing')
	print('3) Good cut')
	print('4) Big rip')
	swing = int(input('Make a choice:'))
	return swing
	


