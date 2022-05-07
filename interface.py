# Huong Nguyen, huongmng@usc.edu
# ITP 115, Spring 2022
# Section: Mamba
# Final Project
# interface.py
# Description: create a menu, display menu, get user's choice, then either print all parks, parks in a state, find largest park, or search for a park
import tasks

# Parameters: None
# Return value: a dictionary where the keys are letters for the user to input and
# the values are descriptions of the menu options.
# The keys are the following letters: "A", "B", "C", "D", and "Q".
# The corresponding values are the following strings: "All national parks",
# "Parks in a particular state", "The largest park", "Search for a park", and
# "Quit".
def getMenuDict():
    #create two lists for keys and values corresponding
    menuKeys = ["A", "B", "C", "D", "Q"]
    menuValues = ["All national parks","Parks in a particular state","The largest park","Search for a park","Quit"]
    #make an empty dictionary
    dict = {}
    #loop through the stop value of 5 to create a dictionary by matching the keys with the values by position
    for pos in range(5):
        dict[menuKeys[pos]] = menuValues[pos]
    # print (dict)
    return dict

# getMenuDict()

# Parameter: menuDict is a dictionary for the menu
# Return value: None
# Print the menu to the user using the menuDict parameter.
def displayMenu(menuDict):
    #return options to users by loop through each key, and print out the value associated with it
    menuDict = getMenuDict()
    #for each key, print the associated value
    for key in menuDict:
        print(key, "->", menuDict[key])

# Parameter: menuDict is a dictionary for the menu
# Return value: a string that is a valid choice entered by the user
# Use the appropriate loop to continue to ask the user for input until they enter
# valid input. Allow the user to enter in upper or lower case. The keys in the
# menuDict parameter have the valid letters.
def getUserChoice(menuDict):
    #intialize choice as a string
    menuKeys = ["A", "B", "C", "D", "Q"]
    choice = ""
    #if string choice is not in the menu keys list, loop to ask for choice
    while choice not in menuKeys:
        choice = input("Choice: ").upper()
    return choice

# Parameter: parksList is a list of the parks where each park is a dictionary
# Return value: None
# Loop through the list and print some information for each park in the
# following format
# To print the date, use the tasks.convertDate() function.
# You may want to create a function to print one park where the parameter is a
# dictionary object for a park.
def printAllParks(parksList):
    #loop through until all parks
    for parkDict in parksList:
        #call functions to index dictionary of parks
        byAcres = parkDict["Acres"]
        byCode = parkDict["Code"]
        byName = parkDict["Name"]
        byState = parkDict["State"]
        byDate = parkDict["Date"]
        #concat string name with associated code in ()
        print(byName + " (" + byCode + ")")
        #print info of each park and description
        print("Location:", byState)
        print("Area:", byAcres, "acres")
        print("Date Established:", tasks.convertDate(parkDict["Date"]))

# Parameters: None
# Return value: a string with a two-letter abbreviation of a state
# Get input from the user for a state. Allow the user to enter upper or lower
# case.
def getStateAbbr():
    #if length state is not two then continue asking to reenter state
    state = input("Enter a state: ")
    #loop if length does not meet to ask for a state input
    while len(state) != 2:
        print("Need a two letter abbreviation")
        state = input("Enter a state: ")
    #return state abbreviation in uppercase
    return state.upper()

# Parameter: parksList is a list containing parks which are each represented
# with a dictionary object
# Return value: None
# Call the getStateAbbr() function to get a state.
# Loop through the parks using the parksList parameter. Check to see if the
# state entered by the user is in park using the "State" key. If so, then print
# some information for each park in the following format:
def printParksInState(parksList):
    #call function from tasks
    state = getStateAbbr()
    #initialize count
    count = 0
    #loop through until all parks
    for parkDict in parksList:
        # call functions to index dictionary of parks
        byAcres = parkDict["Acres"]
        byCode = parkDict["Code"]
        byName = parkDict["Name"]
        byState = parkDict["State"]
        byDate = parkDict["Date"]
        #check to see if the state is present in dictionary
        if state in byState:
            # print info of each park and description
            print(byName + " (" + byCode +")")
            print("Location:", byState)
            print("Area:", byAcres, "acres")
            print("Date Established:", tasks.convertDate(parkDict["Date"]))
            #increase count if state found
            count += 1
    #no state found, count is 0 and return invalid message
    if count == 0:
        print("There are no national parks in", state, "or it is not a valid state.")


# Parameter: parksList is a list containing parks which are each represented
# with a dictionary object
# Return value: None
def printLargestPark(parksList):
    #call tasks to get the code of the largest park.
    codePark = tasks.getLargestPark(parksList)
    #loop through until all parks
    for parkDict in parksList:
        #call functions to index dictionary of parks
        byAcres = parkDict["Acres"]
        byCode = parkDict["Code"]
        byName = parkDict["Name"]
        byState = parkDict["State"]
        byDate = parkDict["Date"]
        #strip special character when print description
        byDescription = parkDict["Description"].strip('"')
        #if the code is the same as the code in the dictionary
        if codePark == byCode:
            #print info
            print(byName + " (" + byCode + ")")
            print("Location:", byState)
            print("Area:", byAcres, "acres")
            print("Date Established:", tasks.convertDate(parkDict["Date"]))
            print("Description:", byDescription)

# Parameter: parksList is a list containing parks which are each represented
# with a dictionary object
# Return value: None
# Loop thru the list of parks and check to see if the search text is in the park’s
# Code, Name, or Description.
# A park should be printed even if the search text is a different case than in the
# park’s information.
# Print information about the park including the description
def printParksForSearch(parksList):
    search = input("Enter text for searching: ")
    search = search.lower()
    #initialize count
    count = 0
    #loop through until all parks
    for parkDict in parksList:
        #call functions to index dictionary of parks
        byAcres = parkDict["Acres"]
        byCode = parkDict["Code"]
        byName = parkDict["Name"]
        byState = parkDict["State"]
        byDate = parkDict["Date"]
        #strip special character when print description
        byDescription = parkDict["Description"].strip('"')
        #make all byCode lower to compare with search
        if search in byName.lower() or search in byCode.lower() or search in byDescription.lower():
            #print info and increase count if found in search
            print(byName + " (" + byCode + ")")
            print("Location:", byState)
            print("Area:", byAcres, "acres")
            print("Date Established:", tasks.convertDate(parkDict["Date"]))
            print("Description:", byDescription)
            count +=1
    #if no word found, count is 0, print error message
    if count == 0:
        print("There are no national parks for the search text of" + " '" + search + "'")