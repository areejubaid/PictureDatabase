# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 11:30:00 2024

@author: areej
"""

"""
The program stores the dimensions of the picture (width and height), the colour of the frame (e.g.
black), and a description of the picture (e.g. flowers).
The text file Pictures.txt stores the data for the pictures in the order: description, width,
height, colour.
For example, for the first picture in the text file:
 Flowers is the description
 45 is the width
 50 is the height
 black is the frame colour.
The main program needs to ask the user to input their requirements for a picture. The user
will enter the colour of the frame, the maximum width, and the maximum height of the picture.
The program will then search the array of pictures, and output the picture description, the
width, and the height of any picture that meets the user's requirements.
The program should allow the user to input the colour in any case (e.g. Silver, silver, or
SILVER), and still output the correct results.
"""

def filing():
    count =0
    f = open ("Pictures.txt","r")
    desc = f.readline().strip()
    while desc !="":
        width = int(f.readline().strip())
        height = int(f.readline().strip())
        frame_colour = f.readline().strip()
        Pictures.append([desc,width,height,frame_colour])
        desc = f.readline().strip()
        count +=1
    f.close()
    return count

def colour_validation(colour):
    if colour =="black" or colour =="grey" or colour == "white":
        return True
    else:
        return False

def enterfiledata(desc,width,height):
    f = open("NewPictureData.txt","w")
    f.write(desc)
    f.write(width)
    f.write(height)
    f.close()

def find_data(colour, max_height, max_width, num):
    found = False
    for i in range(num):
        if Pictures[i][1]<= max_width and Pictures[i][2]<= max_height and Pictures[i][3]== colour.lower():
            print(f"The picture that matches our requirement has the description: {Pictures[i][0]}, it has the width: {Pictures[i][1]}, the height: {Pictures[i][2]} and the colour: {Pictures[i][3]}")
            found = True
            enterfiledata(Pictures[i][0],Pictures[i][1],Pictures[i][2])
    return found
    
#main
Pictures = [] 
num_of_pics = filing()
colour = input("Enter colour").lower()
while not colour_validation(colour):
    colour = input("Enter colour").lower()
    
max_width = int(input("Enter maximum width"))
max_height = int(input("Enter maximum height"))
check = find_data(colour, max_height, max_width, num_of_pics)

if check == False:
    print("There was no match found")
else:
    print("Congratulations! File has been created with the above data!")
