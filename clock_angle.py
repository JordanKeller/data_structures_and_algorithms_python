def angle_clock(hour, minutes):

	"""Given an hour and minute reading on a clock as input,
	output the angle between the hour and minute hands."""

	# measurements in degrees
	ang_min = (minutes/60) * 360 
	# minute-adjusted hour fraction
	true_hour = (hour % 12) + (minutes / 60)
	ang_hr = (true_hour / 12) * 360

	return min(abs(ang_hr - ang_min), 360 - abs(ang_hr - ang_min))

# Test cases

h = 12
m = 30

#print(angle_clock(h, m))

h = 3
m = 30

#print(angle_clock(h, m))
