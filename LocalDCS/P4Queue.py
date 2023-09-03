'''
    class to implement the functionality for the priority 4 queue, the operator does not see 
    these alarms and they cause an automatic shutdown of some or all of production
'''

from collections import deque

class P4Queue():

    def __init__(self):
        '''initilise the queue'''
        self.queue = deque()

    def __str__(self):
        '''returns the contents of the queue'''
        if self.isEmpty():
            temp = "There are no P4 alarms \n"
        else:
            temp = "The P4 alarms are: \n"
            for i in range(len(self.queue)):
                temp +=str(self.queue[i]) + '\n'
        return temp
    
    def Enqueue(self, x):
        '''method to add an item to the queue'''
        self.queue.append(x)
        
    def Dequeue(self):
        '''remove an item from the queue'''

    def isEmpty(self):
        '''returns if the priority queue is empty'''
        if(len(self.queue) == 0):
            return True
        else:
            return False
    
    def Size(self):
        '''return the size of the queue'''
        if(self.isEmpty):
            return("the P4 queue is empty")
        else:
            return len(self.queue)
        