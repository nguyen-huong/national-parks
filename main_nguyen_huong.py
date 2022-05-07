# Huong Nguyen, huongmng@usc.edu
# ITP 115, Spring 2022
# Section: Mamba
# Final Project
# main.py
# Description: Call tasks and interface and return output according to user's choice

import tasks
import interface

def main():
    print("National Parks")
    #call tasks to return a list of park
    parksList = tasks.readParksFile("national_parks.csv")
    #call interface to get a menu for user
    menu = interface.getMenuDict()
    # choice = interface.getUserChoice(menu)
    # intialize choice as a string
    choice = ""
    #while not quitting, display options and call each function accordingly to the choices they pick
    while choice != "Q":
        interface.displayMenu(menu)
        choice = interface.getUserChoice(menu)
        if choice == "A":
            interface.printAllParks(parksList)
        elif choice == "B":
            interface.printParksInState(parksList)
        elif choice == "C":
            interface.printLargestPark(parksList)
        elif choice == "D":
            interface.printParksForSearch(parksList)

main()