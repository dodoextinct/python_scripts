import time

print('press Enter to begin. Again press enter to start the stopwatch and Ctrl + C to cancel.')

input()
print('started')
starttime = time.time()
lasttime = starttime

lapnum = 1

try:
	while True:
		input()
		lapTime = round(time.time() - lasttime, 2)
		totalTime = round(time.time() - starttime, 2)
		print('Lap #{0}: {1} {2}'.format(lapnum, totalTime, lapTime), end = '')
		lapnum +=1
		lasttime = time.time()
except KeyboardInterrupt:
	print('\nDone.')

