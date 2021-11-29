#####
# queue definition
##

queue = []

# add value at the end of the queue
def push(value):
    queue.append(value)
    
# remove the topmost element of the queue
# and return its value    
def pop():
    if not empty():
        return queue.pop(0)
    else:
        return None
    
# return true if the queue is empty
def empty():
    return len(queue) == 0

# display queue
def display():
    for i in queue:
        print(i, end=" ")
    print()