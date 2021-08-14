def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

########## modifying list ############

allName = ['mehedi', 'karim', 'rahim']
completedName = list()

while allName:
    name = allName.pop()
    print(name)
    completedName.append(name)
print('completedList: ',completedName)

### build a function based on this concept

def pressureCooker(bookedList,completedList):
    while bookedList:
        name = bookedList.pop()
        if name % 2 == 0:
            completedList.append(name)
        else:
            pass

def printing(completedList):
    for name in completedList:
        print(name)

booked =   [x for x in range(1,10)]
completed = []
pressureCooker(booked,completed)
printing(completed)
