# 1. Write a Python program to print the following string in a specific format (see the output).
# Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"


# #method 1
# print("""Twinkle, twinkle, little star, 
#                 How I wonder what you are!
#                         Up above the world so high,
#                         Like a diamond in the sky.
# Twinkle, twinkle, little star,
#                 How I wonder what you are""")



# #method 2
# print("Twinkle, twinkle, little star, \n \t How I wonder what you are!\n \t\t\t Up above the world so high, \n\t\t\t Like a diamond in the sky. \nTwinkle, twinkle, little star, \n\t\t\tHow I wonder what you are")




# 2. Write a Python program to find out what version of Python you are using.

# import sys
# print(f"Python Version No. = {sys.version}")




# 3. Write a Python program to display the current date and time.
# Sample Output :
# Current date and time :
# 2014-07-05 14:34:14

# import datetime
# x = datetime.datetime.now()
# print(f"Today date is = {x.strftime("%d-%m-%Y")} \n and Time is = {x.strftime("%H:%M:%S")} ")




# 4. Write a Python program that calculates the area of a circle based on the radius entered by the user.
# Sample Output :
# r = 1.1
# Area = 3.8013271108436504

# from math import pi

# r = float(input("Enput the radius of circle \t"))

# area = pi*r**2

# print("The area of this circle is + str(area)")





# 5. Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.
# fullName = str(input("Enter your Full name"))
# nameArr = fullName.split()
# print(nameArr[1]+" "+nameArr[0])


# 6. Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
# value = str(input("Enter numbers and use comma operator for multipal value \t"))
# myNums = value.split(",")

# myList = list(myNums)
# myTuple = tuple(myNums)
# print(f"{type(myList)}  {type(myTuple)}")
# print("List : ", myList)
# print("Tuple : ",myTuple)


# 7. Write a Python program that accepts a filename from the user and prints the extension of the file.
# Sample filename : abc.java
# Output : java

# myStr = str(input("Enter file name with extation \t"))
# value = myStr.split(".")
# print("Extention of this file name + " + str(value[1]))



# 8. Write a Python program to display the first and last colors from the following list.
# color_list = ["Red","Green","White" ,"Black"]

# color_list = ["Red","Green","White" ,"Black"]
# print("first color is = " + color_list[0] + "\nlast color of list = " + color_list[len(color_list) - 1])



# 9. Write a Python program to display the examination schedule. (extract the date from exam_st_date).
# exam_st_date = (11, 12, 2014)
# Sample Output : The examination will start from : 11 / 12 / 2014

# exam_st_date = (11, 12, 2014)
# print(f"The examination will start from : {exam_st_date[0]}/ {exam_st_date[1]}/ {exam_st_date[2]}")



# 10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
# Sample value of n is 5
# Expected Result : 615

# n = int( input("Enter a numeric value = "))
# print(f"{(n)+(n*11)+(n*111)}")