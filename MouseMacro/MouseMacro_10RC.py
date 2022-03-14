# this a code to use your mouse do to certain things
# this code is to do 10 repeated right clicks in a quick succession
import mouse

for click in range(10):
    mouse.click('right')
# this doesn't work on M1 mac :(
# it will work on Windows though
