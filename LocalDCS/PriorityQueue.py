'''
    Class to implement functionality for prirority queue system of alarms
    This encompases priority 1,2 & 3 alarms only
'''


class PriQueue():

    def __init__(self):
        '''initilise the queue using dequeue'''
        self.queue = list()

    def __str__(self):
        '''returns the contents of the queue'''
        if self.isEmpty():
            temp = "Priority Queue is empty \n"
        else:
            temp = ""
            for i in range(len(self.queue)):
                temp += str(self.queue[i]) + '\n'    #-(i+1) - this flips the queue
        return temp

    def Enqueue(self, x):
        '''method to add items to the message queue based on priority'''

        #check to see if item is alreaady in the list
        for i, item in enumerate(self.queue):
            if (item.Tag == x.Tag) and (item.Pri == x.Pri):
                self.queue[i] = x
                return   
            else:
                continue   

        i = 0   
        if(x.Pri == 3):
            #if the alarm is a priority 3 alarm
            if ((self.Priority_count(2) == 0) and (self.Priority_count(1) == 0)):
                #if there are no p1 or p2 items...
                self.queue.append(x) 
            else:
                for i in range(len(self.queue)):
                    if (self.queue[i].Pri == 2):          #where are the any priority 2 items
                        break
                    elif (self.queue[i].Pri == 1):        #where are the priority 1 items
                        break
                self.queue.insert((i),x)

        elif(x.Pri == 2):
            #if the alarm is a priority 2 alarm
            if ((self.Priority_count(1) == 0)):
                self.queue.append(x)
            else:
                for i in range(len(self.queue)):
                    if (self.queue[i].Pri == 1):
                        break
                self.queue.insert((i),x)

        elif(x.Pri ==1):
            #the item is priority 1 it can just go to the end
            self.queue.append(x)
        else:
            print("Error - priority not regognised (Module PriQueue.Enqueue)")           

    def Dequeue(self, Tag):
        '''remove an item from the queue'''
        #this is removing the specific item that has either come out of alarm or the operator has resolved the issue
        for i in range(len(self.queue)):
            if (self.queue[i].Tag == Tag):
                return self.queue.pop(i)
        return None    

    def isEmpty(self):
        '''returns if the priority queue is empty'''
        if(len(self.queue) == 0):
            return True
        else:
            return False

    def Size(self):
        '''returns the size of the queue'''
        return len(self.queue)

    def Priority_count(self, x):
        '''returns the amount of priorty 1,2 or 3 items in the queue'''
        count = 0

        if(x==1):   
            #count the number of priority 1 items in the queue
            for i in range(len(self.queue)):
                if(self.queue[i].Pri == 1):
                    count +=1
            return count 

        elif(x==2):
            #count the number of priority 2 items in the queue
            for i in range(len(self.queue)):
                if(self.queue[i].Pri == 2):
                    count +=1
            return count

        elif(x==3):
            #count the number of priority 3 items in the queue
            for i in range(len(self.queue)):
                if(self.queue[i].Pri == 3):
                    count +=1
            return count


    def AreaPriority_Count(self, P, Area):
        '''returns the priority count for a specific area'''

        count = 0

        if(Area == "A"):
            if(P == 1):
                for i in range(len(self.queue)):
                    if(self.queue[i].Tag[:2] == "ED" and self.queue[i].Pri == 1):
                        count +=1
                return count
            elif(P == 2):
                for i in range(len(self.queue)):
                    if(self.queue[i].Tag[:2] == "ED" and self.queue[i].Pri == 2):
                        count +=1
                return count
            elif(P == 3):
                for i in range(len(self.queue)):
                    if(self.queue[i].Tag[:2] == "ED" and self.queue[i].Pri == 3):
                        count +=1
                return count
        elif(Area == "B"):
            if(P == 1):
                for i in range(len(self.queue)):
                    if(self.queue[i].Tag[:2] == "LD" and self.queue[i].Pri == 1):
                        count +=1
                return count
            elif(P == 2):
                for i in range(len(self.queue)):
                    if(self.queue[i].Tag[:2] == "LD" and self.queue[i].Pri == 2):
                        count +=1
                return count
            elif(P == 3):
                for i in range(len(self.queue)):
                    if(self.queue[i].Tag[:2] == "LD" and self.queue[i].Pri == 3):
                        count +=1
                return count
    
