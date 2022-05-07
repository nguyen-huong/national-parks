# Huong Nguyen, huongmng@usc.edu
# ITP 115, Spring 2022
# Section: Mamba
# Final Project
# tasks.py
# Description: Read csv of parks, return a list of park, convert dates, and return largest park

# Parameter: fileName is the name of the CSV file to read and it has a default
# value of "national_parks.csv"
# Return value: a list of dictionary objects where the keys are the strings from
# the header row and the values are the information from the rest of the CSV file
# You will notice that the description string for a park may contain a comma.
# The description for a park can contain the string up to the first comma. If you
# want to include the entire description, then you will need to use slicing and
# the str.join() function.
def readParksFile(fileName = "national_parks.csv"):
    #initialize an empty list of park, open file, and return header
    parksList = []
    fileIn = open(fileName, "r")
    header = fileIn.readline().strip()
    # print(header)
    # get keys based on the header for dictionary
    keys = header.strip().split(",")
    # print(key)
    for line in fileIn:
        #go line by line to return values of each park and description by the index of 7
        parkDict = {}
        listpark = line.strip().split(",")
        # print(listpark)
        # print(",".join(listpark[:7]))
        description =  ",".join(listpark[7:])
        listpark[7] = description
        description = description.strip('"')
        #stop value at 8
        for pos in range(8):
            # dictionary[key] = value
            # return parkDict with the format of dictionary, pos, keys (header), listpark (list of values)
            parkDict[keys[pos]] = listpark[pos]
        parksList.append(parkDict)
    # print (listpark)
    # print(description)
    # print(keys)
    # print (parksList)
    return parksList

# readParksFile(fileName = "national_parks.csv")

#  Parameter: dataStr is a string containing the date (YYYY-MM-DD)
#  Return value: a string with the date in the following format: Month Day, Year
#  Create any variables you need such as a list of month names.
def convertDate(str):
    #create a list of months
    monthList = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December"]
    #split the string of date, separate it through slicing based on date, month, year
    split = str.strip().split("-")
    date = split[2]
    monthIndex = (int(split[1])-1)
    month = monthList[monthIndex]
    year = split[0]
    #concat the string
    str = month + " " + date + "," + " " + year
    return str

# convertDate("2003-03-17")

# Parameter: parksList is a list of the parks where each park is a dictionary
# Return value: a string that is the park code of the park with the largest area
# Determine the largest park by using the value of the "Acres" key in the
# dictionary for each park. If the value was set as a string, then convert to an integer.
# To get the park code, use the "Code" key in the dictionary for each park
# OH notes: look at assignment 4
# parksList = readParksFile(fileName = "national_parks.csv")
def getLargestPark(parksList):
    #intialize a maximum value and an empty string for code
    max = 0
    byCode = ""
    #loop through to compare value by acres, then if that value is greater than the maximum value, update and get the code for the largest park
    for parkDict in parksList:
        #retrieve by acres
        byAcres = parkDict["Acres"]
        byAcres = int(byAcres)
        if byAcres > max:
            max = byAcres
            byCode = parkDict["Code"]
    return byCode

# getLargestPark(parksList)

