#***************************************************************************#
# Team 6: Jamie Graham, Natsuki Abe, Tristan Janisse
# Professor: Citro
# Class: CST-315
# Date: 2.2.20
# Project Name: RKF Calculation
# Project Goals: The goal of this program is to simulate the RKF equation in python,
# creating a table of the x and y values over a number of times of iterations (user-inputted)
# and plotted into a graph.
# Input: First x and y value, h, and number of times ODE is iterated
# Output: Table of RKF calculated values and plotted graph.
#****************************************************************************#

# Libraries required:
# math - to create our ODE
# matplotlib - to plot our table
# prettytable - to make our table easy to read

import math
from prettytable import PrettyTable
import plotly.express as plt

#*****************************************************************************************************#
# Function Name: rkf1 - RKF Method 1
# Function Goal: Complete First Order Runge-Kutta calculation to find k1.
# Input: x and y
# Output: k1
# Mathematical Discussion: This function is designed to replace the first order step of Runge-Kutta. It
# fills in the x and y values to the ODE (Ordinary Differential Equation) function and returns the k1 value
# that will be used to calculate y1 and x1 values. The first values are from the user, next x and y are recalculated
# based on the new x and y values calculated.
#*****************************************************************************************************#
def rkf1(x, y):
    k1 = ODE(x,y)
    return k1;


#*****************************************************************************************************#
# Function Name: rkf2 - RKF Method 2
# Function Goal: Complete First Order Runge-Kutta calculation to find k1.
# Input: x, y, h, k1
# Output: k2
# Mathematical Discussion: This function is designed to replace the second order step of Runge-Kutta. It
# fills in the x, y, h, and k1 values to the ODE (Ordinary Differential Equation) function and returns the k2 value
# that will be used to calculate y1 and x1 values. The first values are from the user, next x and y are recalculated
# # based on the new x and y values calculated.
#*****************************************************************************************************#
def rkf2(x,y,h, k1):
    k2 = ODE((x + h/2), (y+(h/2) * k1))
    return k2


#*****************************************************************************************************#
# Function Name: rkf3 - RKF Method 3
# Function Goal: Complete First Order Runge-Kutta calculation to find k1.
# Input: x, y, h, k2
# Output: k3
# Mathematical Discussion: This function is designed to replace the third order step of Runge-Kutta. It
# fills in the x, y, h, and k2 values to the ODE (Ordinary Differential Equation) function and returns the k3 value
# that will be used to calculate y1 and x1 values. The first values are from the user, next x and y are recalculated
# # # based on the new x and y values calculated.
#*****************************************************************************************************#
def rkf3(x,y, h, k2):
    k3 = ODE((x + (h/2)), (y + (h/2) * k2))
    return k3

#*****************************************************************************************************#
# Function Name: rk4 - RFK Method 4
# Function Goal: Complete First Order Runge-Kutta calculation to find k1.
# Input: x, y, h, k3
# Output: k4
# Mathematical Discussion: This function is designed to replace the fourth order step of Runge-Kutta. It
# fills in the x, y, h, and k3 values to the ODE (Ordinary Differential Equation) function and returns the k4 value
# that will be used to calculate y1 and x1 values. The first values are from the user, next x and y are recalculated
# # # # based on the new x and y values calculated.
#*****************************************************************************************************#
def rkf4(x,y, h, k3):
    k4 = ODE((x+h), (y + (h*k3)))
    return k4

#*****************************************************************************************************#
# Function Name: CalculateY1
# Function Goal: This function is designed to take the original equation that y1 = y + (h/6 * (k1 *2k2 *3k3 + k4)
# to find the y1 value that can be later used in plot
# Input: y, h, k1, k2, k3, k4
# Output: y1
# Mathematical Discussion: This function is designed to replace the final caluclation step of Runge-Kutta. It
# fills in all of the values needec to the ODE (Ordinary Differential Equation) function and returns the y1 value.
#*****************************************************************************************************#
def CalculateY1(y, h, k1, k2, k3, k4):
  return y + (h * (k1 + (2*k2) + (3*k3) + k4) /6)


#*****************************************************************************************************#
# Function Name: CalculateX1
# Function Goal: This function is designed to take the original equation that x1 = x + h to find the x1
# value that can be later used in plot
# Input: x, h
# Output: x1
# Mathematical Discussion: This function is designed to replace the first order step of Runge-Kutta. It
# fills in the x and y values to the ODE (Ordinary Differential Equation) function and returns the k1 value
# that will be used to calculate y1 and x1 values.
#*****************************************************************************************************#
def CalculateX1(x, h):
  return x + h;


#*****************************************************************************************************#
# Function Name: ODE
# Function Goal: This function is designed to be continously called upon by the 4 RKF methods. It contains
# the equation that was given for this program. This program is reusable in the sense that if the equation changes
# then only the function would need to be changed for the program to do as intended.
# Input: x, y
# Output: dy  (derivative of y that has been calculated with x and y values)
# Mathematical Discussion: This function is designed to replace the first order step of Runge-Kutta. It
# fills in the x and y values to the ODE (Ordinary Differential Equation) function and returns the k1 value
# that will be used to calculate y1 and x1 values.
#*****************************************************************************************************#
def ODE (x,y):
    dy = y*(1/math.exp(x)) - (1/math.exp(x))
    return dy

#*****************************************************************************************************#
# Function Name: Main
# Function Goal: The main defines the inputs from user, calls the methods, creates the table, and plots the graph
# Input: None
# Output: None
#*****************************************************************************************************#
def main():
    x = float(input("Input inital value for x: (as float, in units): ")) # test case was 1
    y = float(input("Input inital value for y (as float, in units): ")) # test case was 2
    h = float(input("Input h value (as float, in units): ")) # test case was 0.05
    n = int(input("Input number n times you want this program to run (as int, in units): ")) # test case was 3
    table = PrettyTable()
    table.field_names = ["X", "Y"]

    for i in range(n):
        k1 = rkf1(x,y)
        k2 = rkf2(x,y,h, k1)
        k3 = rkf3(x,y,h, k2)
        k4 = rkf4(x,y,h, k3)

        y1 = CalculateY1(y, h, k1, k2, k3, k4)
        x1 = CalculateX1(x, h)

        # Here is where the initial x and y values are redefined by calculated x and y for next iteration
        y = y1;
        x = x1;

        table.add_row([x,y])
        plot = plt.line(x=[x], y=[y],
        title = "RKF X vs. Y values")



    print(table) #print end results

    plot.show()


main()
