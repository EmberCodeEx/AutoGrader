
### YOUR CODE FOR openLocks() FUNCTION GOES HERE ###
def openLocks(number_of_lockers, number_of_students):
    if number_of_students < 0 or number_of_lockers < 0:
        return None
    number_of_open_lockers = 0
    lockersData = initialLogic(number_of_lockers, number_of_students)
    for i in range(0, len(lockersData)):
        locker = lockersData[i]
        if locker[0] == 1:
            number_of_open_lockers += 1
    return number_of_open_lockers

#### End OF MARKER





### YOUR CODE FOR mostTouchableLocker() FUNCTION GOES HERE ###
def mostTouchableLocker(number_of_lockers, number_of_students):
    if number_of_students < 0 or number_of_lockers < 0:
        return None
    most_touched_locker = -1
    most_touches = 0
    lockersData = initialLogic(number_of_lockers, number_of_students)
    for i in range(0, len(lockersData)):
        locker = lockersData[i]
        if locker[1] >= most_touches:
            most_touches = locker[1]
            most_touched_locker = i
    return most_touched_locker + 1
    
#### End OF MARKER

#### INITIAL LOGIC
def initialLogic(no_of_lockers, no_of_students):
    # lockersData = [[0, 1], [0, 1] .... ]
    lockersData = []
    for i in range(1, no_of_students + 1):
        if i == 1:
            for j in range(1, no_of_lockers + 1):
                # first element of locker is locker state == open/close
                # second element of locker is no of touches
                # 0 == locker close, 1 == locker open
                locker = [1, 1]
                lockersData.append(locker)
        else: 
            for k in range(2, no_of_lockers + 1):
                # get locker data at index k - 1
                locker = lockersData[k - 1]
                # check if index of locker id properly divisible by index of student
                if k % i == 0:
                    # check if locker is closed then open it else close it
                    if locker[0] == 0:
                        locker[0] = 1
                    else:
                        locker[0] = 0
                    # increase nuumber of touchers by one
                    locker[1] = locker[1] + 1
                    # update locker data
                    lockersData[k - 1] = locker
    return lockersData
#### END INITIAL LOGIC


