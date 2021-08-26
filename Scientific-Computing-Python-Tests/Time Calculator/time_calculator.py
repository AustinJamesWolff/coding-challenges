def add_time(start, duration, day = False):
    """
    DOCSTRING: This function takes a clock-time as its first argument,
    a number of hours and minutes in "military clock time" as a second argument,
    and an optional day of the week as the third argument.
    
    Then it adds our 2nd argument time to our 1st argument,
    and returns the updated clock time.
    
    >>>add_time("11:43 AM", "00:20")
    12:03 PM
 
    >>>add_time("10:10 PM", "3:30")
    1:40 AM (next day)
 
    >>>add_time("11:43 PM", "24:20", "tueSday")
    12:03 AM, Thursday (2 days later)
    """
    
    # Used for conversion near the end
    daysOfWeek = {
        "Sunday": 1,
        "Monday": 2,
        "Tuesday": 3,
        "Wednesday": 4,
        "Thursday": 5,
        "Friday": 6,
        "Saturday": 7
    }
    
    # Converts our clock time into total number of minutes the time represents
    def timeConvert(clockTime):
        print(clockTime)
        hourToMins = int(clockTime[0]) * 60
        totalMin = hourToMins + int(clockTime[1])
        try:
            if clockTime[2] == "PM":
                totalMin += 720
        except IndexError:
            print("During timeConvert function: No 'AM' or 'PM' found, not a problem for 2nd argument of add_time function.")
        return totalMin

    # Below turns our clock time into an index for the timeConvert function above
    tempStartList = start.split(" ")
    startList = tempStartList[0].split(":")
    startList.append(tempStartList[1])
    durList = duration.split(":")
    
    # Stores the clock-to-minute conversion above into two new variables
    totalStartMin = timeConvert(startList)
    totalDurMin = timeConvert(durList)
    
    # Calculates the new total minutes our new time represents
    totalNewMin = totalStartMin + totalDurMin
    print("totalNewMin: " + str(totalNewMin))

    # Below will give us the amount of new days we added (could be 0)
    newDays = totalNewMin // 1440
    print("newDays: " + str(newDays))
    
    newDayOfWeek = ""
    
    # If there was a day of the week passed as the optional argument,
    # the statement below will tell us what the day is now, after 
    # our new time is added to the original clock
    if day != False:
        day = day.lower().capitalize()
        keyNumber = daysOfWeek[day] + newDays
        if keyNumber > 7 and keyNumber <= 14:
            keyNumber -= 7
        elif keyNumber > 14 and keyNumber <= 21:
            keyNumber -= 14
        elif keyNumber > 21 and keyNumber <= 28:
            keyNumber -= 21
        keyDay = list(daysOfWeek.keys())[list(daysOfWeek.values()).index(keyNumber)]
        newDayOfWeek = ", " + str(keyDay)
    
    # Converts our new total minutes back into clock-time
    def convertBack(backTime):
        tempClockList =[]
        hoursRemainder = (backTime // 60) - (newDays * 24)
        tempClockList.append(hoursRemainder)
        minuteRemainder = backTime % 60
        tempClockList.append(minuteRemainder)
        if hoursRemainder < 12:
            tempClockList.append("AM")
        else:
            tempClockList.append("PM")
        print(tempClockList)
        if hoursRemainder == 0 and tempClockList[2] == "AM":
            tempClockList[0] = "12"
        if hoursRemainder > 12:
            tempClockList[0] = str(tempClockList[0] - 12)
        if hoursRemainder <= 12:
            tempClockList[0] = str(tempClockList[0])
        if minuteRemainder < 10:
            tempClockList[1] = "0" + str(tempClockList[1])
        if minuteRemainder >= 10:
            tempClockList[1] = str(tempClockList[1])
        tempClockFace = ":".join(tempClockList[0:2])
        tempClockFace = tempClockFace + " " + str(tempClockList[2])
        return tempClockFace
    
    # Stores our new and updated clock-time into a variable
    newClockTime = convertBack(totalNewMin)    
    
    # Adds how many days later, if applicable
    if newDays == 0:
        daysLater = ""
    elif newDays == 1:
        daysLater = " (next day)"
    else:
        daysLater = " ({} days later)".format(newDays)
    
    
    # Below should be the last statement
    # We will test print it first
    print(newClockTime + newDayOfWeek + daysLater)
    print(" ///// End of function //// ")
    return newClockTime + newDayOfWeek + daysLater