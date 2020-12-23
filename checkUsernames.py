import requests 
import time

# Reddit Username API Info:
# https://www.reddit.com/dev/api/
#    /api/username_available
#    https://www.reddit.com/api/username_available.json?user=blah

DEBUG = False
checkusername = "https://www.reddit.com/api/username_available.json?user="

file = open('redditusernames.txt', 'r')
lines = file.readlines()
count = 0
for line in lines:
	req = checkusername + line.strip() # need to make sure to strip extraneous info from lines or it won't work
	r = requests.get(req, headers = {'User-agent': 'botbro 0.1'})
	if DEBUG:
		print("Line{}: {}".format(count, line.strip()))
		print("Request is: " + checkusername + line)
		print("R Content is: " + str(r.content))
		print("R Text is: " + r.text)
		print("R is: " + str(r))
		print(" ")
	if r.text == 'true':
		print("This username is available: " + line.strip())
		print(" ")
	else:
		pass
		#print("CAN'T USE THIS USERNAME: " + line.strip())
	# Increment counter and sleep for one second to prevent Reddit throttling
	count += 1
	time.sleep(1)
