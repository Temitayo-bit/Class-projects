# -*- coding: utf-8 -*-
"""interest calculator - Assignment.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Hbxg7ORx974LD4qNBJ-GvChAcph_-UOj
"""

def greeting():
#creating a method to welcome the user
  name = input("Input Username? ")
# A function that asks the user to input username
  print(f"Welcome {name}. Thank you for using this calculator")
#Displaying the welcome message
  return name
#Exporting a variable from the above method

def simple():
# Storing a method that calculates the simple interest
  principal = float(input("Input Principal amount (in dollars)? "))
#A variable asking the user to input the Principal amount. A float is used instead of an int incase of a decimal
  rate = float(input("Input rate? "))
#A variable asking the user to input the rate
  time = float(input("Input the time in years? "))
#A function asking the user to input the time in years
  R = rate/100
#A variable that divides the rate by 100 inorder to turn it into a percentage value
  rate_per_year = R * time
#Calculating the rate per year which is the percentage rate multiplied by the amount of years
  interest = principal * rate_per_year
#Calculating the interest which is the principal multiplied by the rate per year
  simple_interest = principal + interest
#Calculating the total amount, which is the interest plus the principal amount
  print(f"Your interest over {time} years with the rate of {rate}% is ${interest :.3f} ")
#Display function to display the interest amount in 3 decimal places
  print(f"Total amount including principal amount is ${simple_interest}")
#Display function to display the total amount.


def transition():
#Creating a method to store a function that lets the user know that the compounded interest calculator is coming up
  print("The next option is to calculate the compount interest")
#A Display function


def compound():
# Storing a method that calculates the compound interest
  principal = float(input("Input principal amount (in dollars)? "))
#A variable asking the user to input the Principal amount. A float is used instead of an int incase of a decimal
  rate = float(input("Input rate? "))
#A variable asking the user to input the rate
  time = float(input("Input the time in years? "))
#A function asking the user to input the time in years

  amount = int(input("Input the amount of times compounded per year? "))
#Function asking user to input the amount of times in a year the interest was compounded
  R = rate/100
#A variable that divides the rate by 100 inorder to turn it into a percentage value
  C = amount * time
#The amount of times compounded by year multiplied by the number of years
  P = R/amount
#The rate percentage divided by the amount of times compounded
  CO_interest = principal * (1 + P) ** C
#Variable to calculte the compound interest using the compound interest
  print (f" Your componded interest over {time} years, at the rate of {rate}%. Compounded {amount} time(s) is: ${CO_interest:.3f}")
#Display function to display the compound interest

def goodbye(a):
#Creating a variable to store the goodbye message. There is also a named variable which is an import of the first method
  print(f"Good bye, {a}. Thank you for using my calculator....")
#Display function to display the goodbye message






x = greeting()
#Recalling the method, and naming it inorder to use a variable in it for another method
simple()
#Recalling the method
transition()
#Recalling the method
compound()
#Recalling the method
goodbye(x)
#Recalling the method, and importing the variable from another method