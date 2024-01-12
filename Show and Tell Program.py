"""HEADER
Name: Ayan Hazarika
Date: 6/18/2020
Program: Show and Tell Program
Description: Constellation Connector!
"""

#Importing required modules
import turtle
from tkinter import*

#Printing intro message
print("Hey there!")
print("This is a Constellation Connector program! Firstly, you will be asked which constellation you would like the program to draw out of 5 selected constellations. The program will then draw this constellation, so all you have to do is sit back and relax! Enjoy!")

#Asking user for their name
myGui = Tk()
nameLabel = Label(myGui, text = "Please Enter Your Name Here: ")
nameLabel.pack()

#Entry box for user to enter their name
n1 = StringVar()
nameBox = Entry(myGui, textvariable = n1)
nameBox.pack()

#Function to run when button is clicked
def buttonAndConstellationsFunction():
    messageLabel = Label(myGui, text = ("Hello! Let's Get Started!"))
    messageLabel.pack()
    constellationMessage = Label(myGui, text = "Here are the constellations to choose from!")
    constellationMessage.pack()
    printConstellationList = Label(myGui, text = "a) Star  b) Car  c) Hourglass  d) Diamond  e) Super Star")
    printConstellationList.pack()
    
    n2 = StringVar()
    constellationBox = Entry(myGui, textvariable = n2)
    constellationBox.pack()
    
#Creating button and telling it what to do
button = Button(myGui, text = "Click Here", command = buttonAndConstellationsFunction)
button.pack()
