import pickle
import sys
from EventObj import Event
from PriorityQueue import PriQueue    

###this whole script probaly donsent need to exist

data = sys.stdin.buffer.read()
E = pickle.loads(data)
#print(E)
#print("This is the recieved piped data {}\n\n".format (E))


'''at this stage we have the object imported and now need to run a series of logic statement 
    to determine where the alarm is located, what the priority is and...

-- FInd the Tag in the A&T database
-- compare sensor value against trip values
-- if value exceeds paramaters, output message.


Alarm logic
-- Depending on the tag number of the alarm determine where the alarm needs to appear on the operators screen 
-- The LL/HH/L/H pre determines the priority of the alarm and this is sent to the operator. 
-- Depending on the priority level of the alarm the operator will be given a certian amount of time to react, before the susbsytem is 
    shutdown automatically. A master list of all current alarms will also be collacted with the highest priority alarms at the top of the list.

'''

'''
if(Event Priority = 4):
    trigger automatic module shutdown
elseif(Event priroty between 1 and 3):
    send message to operator and alarm point on GUI
else:
    log event and present background notification to operator


'''
#Archive function moved to event class
#print(Event.WarningMsg(E))
Event.Archive(E)
