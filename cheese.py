import numpy as np

balls=0
strikes=0
num = {1:[90, 75], 2:[85, 80], 3:[80, 85], 4:[75, 90]}
p_out = {1:'Strike swinging',2:'Strike looking',3:'Foul ball'}
b_out = {1:'Home run!',2:'Hit in the air...',3:'Hit on the ground...',4:'Off the plate for a ball.'}

def pitch_selection():
	x = [1,2,3,4]
	print('Choose a pitch:')
	print('1) Fastball')
	print('2) Change Up')
	print('3) Slider')
	print('4) Split Finger Fastball')
	pitch = int(input('Make a choice:'))
	if pitch not in x:
		print('He steps off the rubber.')
		return pitch_selection()
	else:
		return pitch
	
def swing_selection():
	x =[1,2,3,4]
	print('Choose a swing:')
	print('1) Choke Up')
	print('2) Regular swing')
	print('3) Good cut')
	print('4) Big rip')
	swing = int(input('Make a choice:'))
	if swing not in x:
		print('He calls for time')
		return swing_selection()
	else:
		return swing
		
def loc_selection():
	x=[1,2,3,4]
	print('Choose a location:')
	print('1) High-Away')
	print('2) High-Tight')
	print('3) Low-Away')
	print('4) Low-Inside')
	loc = int(input('Make a choice: '))
	if loc not in x:
		return loc_selection()
	return loc
	

'''Returns False if roll fails'''
def control_roll(m):
	x=num[m][0]
	y=np.random.randint(0,100)
	#print('x ',x,' y ',y)
	if y > x:
		return False
	return True

'''Returns False if roll fails'''
def power_roll(m,bonus=None):
	x=num[m][1]
	if bonus==True:
		x +=5
	y=np.random.randint(0,100)
	if y > x:
		return False
	return True

def pow_res(p,b):
	dif=abs(b-p)
	


	
	


