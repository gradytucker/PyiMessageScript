import os, time


num = raw_input('type in person you would like to text: ')

body = raw_input('what would you like to say?: ')

cmd = """osascript<<EOF
tell application "Messages"

    set targetBuddy to "%r"
    set targetService to id of 1st service whose service type = iMessage


        set textMessage to "%s"

        set theBuddy to buddy targetBuddy of service id targetService
        send textMessage to theBuddy


end tell

EOF""" % (num, body)

print 'texting recipient in 5'
time.sleep(1)
print 'texting recipient in 4'
time.sleep(1)
print 'texting recipient in 3'
time.sleep(1)
print 'texting recipient in 2'
time.sleep(1)
print 'texting recipient in 1'
time.sleep(1)

def send_Message():

     os.system(cmd)

send_Message()

print 'message sent!'
