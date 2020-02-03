# RFK-Calculator-For-ODEs
The goal of this program is to simulate the RKF equation in python, # creating a table of the x and y values over a number of times of iterations (user-inputted) # and plotted into a graph.

Team 6 - Jamie (Graham) Reichenberger, Tristan Janisse. Natsuki Abe 
Professor Ricardo Citro – CST305 - MWF 3:20-4:30  
January 26, 2020 

# Set up instructions:
## 1. Install Python 2.7 on computer

## 2. Download Github code into your computer as a python file

## 3. Run the command "python " with name of the file in your terminal

## 4. Input your data... then ejoy the calculations, table, and plot!

 

 
# Responsibilities/Tasks Completed by Each Member 
Jamie Graham took leadership over the code writing, but all members had view and contribution to programming. Natsuki Abe  took leadership over mathematical computation, but everyone participated in completing that portion. Tristan Janisse took leadership over documentation, but everyone contributed and added to the completed work. It was a solid team effort and all team members contributed to every portion of the assignment.
# System Performance Context Description 
The software used include PyCharm, and Python 2.7. The python libraries necessary are Matplotlib, Math, and Prettytable. To be able to use this software, the system requires an OS that meets the requirements of Python 2.7 installed on their computer. The user can execute the python file using the Python command in their terminal at that point. The main library that this solution is using is called odeint which is a powerful C++ library that is known for high performance in terms of accuracy, efficiency, and speed. The performance is competitive with plain C and Fortran90 code as the performance measured as runtime required to perform 200,000 Runge-Kutta4 steps for the Lorenz system.  When tested on Intel Hardware(Core i5 and Xeon E5) the applications have basically equivalent performance. This proves odeint gives the competitive performance needed for our solution to help our users. The library is also designed proficiently with a modularized design that has high flexibility for abstraction and modularization, with no added run-time costs. (Mulansky, M., & Ahnert, K.). 
# Mathematical Approach for Solving it 
Runge kutta method is one of the methods to solve ordinary equations but only first order differential equations can be solved with this method and it is known to be better approximated than Euler’s method. Runge kutta methods approximates y value for a given x. In order to solve an ordinary equation with Runge-Kutta-Fehlberg method, first we need to find x and y values for k1, k2, k3, and k4. The formulas for that are: 
<details>
<summary>"Click to expand"</summary>
  x0, y0, and h are given
  k1 = f(x0, y0)
  k2 = f(x0+h2, y0+h2k1)
  k3 = f(x0+h2, y0+h2k2)
  k4  = f(x0+h, y0+hk3)

</details>
After we find x and y values for k1, k2, k3, and k4, we need to plug x and y values for k1, k2, k3, and k4 into the original equation in order to find k1, k2, k3, and k4 values. After that, we need to plug k1, k2, k3, and k4 values into this formula in order to find y1:
<details>
<summary>"Click to expand"</summary>
  y1 = y0 + h6(k1+2k2+2k3+k4)
The formula for x1 is:
  x1 = x0+h
  f(x,y) = ye-x-e-x           x0= 1   y0 =2     h=0.05
  k1 = f(x,y) =2e-1-e-1=0.36788
  k2 =f(x+0.05/2, y+(0.05/2)k1) =2.00919e-1.025-e-1.025=0.36209
  k3 =f(x+0.05/2, y+(0.05/2)k2) =2.00905e-1.025-e-1.025=0.36204
  k4 =f(x+0.05, y+(0.05)k3) =2.0181e-1.05-e-1.05=0.35628
  y1=y0+h/6(k1+2(k2)+2(k3)+k4)=2+(0.05/6)(0.36788+2(0.36209)+2(0.36204)+0.35628=2.0181
  x1=x0+h=1+0.05=1.05
 
  x1=1.05   y1=2.0181    h=0.05
  k1 =f(x,y) =2.0181e-1.05-e-1.05=0.35627
  k2 =f(x+0.05/2, y+(0.05/2)k1) =2.02701e-1.75-e-1.075=0.35052
  k3 =f(x+0.05/2, y+(0.05/2)k2) =2.02687e-1.075-e-1.075=0.35047
  k4 =f(x+0.05, y+(0.05)k3) =2.03563e-1.1-e-1.1=0.34473
 </details>
 
 
# Approach for Implementation 
The plotting python package is Plotly. Plotly is a popular 2D plotting Python library that produces quality figure and interactive enviornments across platforms. It can used for Python, IPython shells, web application services, Jupyter notebook, and some graphical user interface toolkits. 
Imported as such: 
  Import matplotlib.pyplot as plt 
# Pseudo code
<details>
<summary>"Click to expand"</summary>
  Find X0 (initial x), Y0 (initial y), H (h value), and N (number of times run)
  Use X0 and Y0 values to conduct RKF equation. 
  Use RKF 1st Order equation to find K1
  Use RKF 2nd Order equation to find K2
  Use RKF 3rd Order equation to find K3
  Use RKF 4th Order equation to find K4
  Use X0, Y0, K1, K2, K3, K4, and H to find the new X1 and Y1 values
  Set X0 = X1 and Y0 = Y1
  Repeat this process for all of N times
  Print table of X and Y values
  Finally, plot results with plotly – plot X vs. Y values
 </details>

 
References 
Matplotlib Documentation. (n.d.). Retrieved from https://matplotlib.org/ 
Mulansky, M., & Ahnert, K. (n.d.). Odeint library. Retrieved from  
http://www.scholarpedia.org/article/Odeint_library 
Zeltkevic, M. (1998, April 15). Retrieved from 
http://web.mit.edu/10.001/Web/Course_Notes/Differential_Equations_Notes/node5.html
 

