
import cheese as hc

balls = hc.balls
strikes = hc.strikes
count = 'The count is {0} balls and {1} strikes.'.format(balls, strikes)
print(count,'\n')

pitch=hc.pitch_selection()
p_loc=hc.loc_selection()
swing=hc.swing_selection()
s_loc=hc.loc_selection()

print('The pitcher sets\n')
x_pit=hc.control_roll(pitch)
x_bat=hc.control_roll(swing)
print(x_pit,x_bat)
if x_pit is False  and x_bat is False:
	strikes += 1
	print('Foul ball!')
elif x_pit is False and x_bat is True:
	balls += 1
	print('Ball')
elif x_pit is True and x_bat is False:
	strikes += 1
	print('Swung on and missed.')
else:
	if p_loc == s_loc:
		print('He was looking for that pitch!')
		b_pow=hc.power_roll(swing,True)
		p_pow=hc.power_roll(pitch)
		#add method to resolve
	else:
		pass
		






	

print('{} balls and {} strikes'.format(balls,strikes))