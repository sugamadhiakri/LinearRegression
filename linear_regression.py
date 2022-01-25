# Import the necessary libraries
from cProfile import label
from tkinter.tix import Tree
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import threading

# Read and parse the data
data = pd.read_csv("Salary_Data.csv")

# Extract the dependent and independent variable
X = data['YearsExperience']
Y = data['Salary']


# Convert the data into numpy array
xArray = np.array(X)
yArray = np.array(Y)

def train():

    # Calculate the mean of the variables 
    xMean = np.mean(X)
    yMean = np.mean(Y)

    numerator = 0
    denominator = 0
    for i in range(len(xArray)):
        numerator += (xArray[i] - xMean) * (yArray[i] - xMean)
        denominator += (xArray[i] - xMean) ** 2

    # Calculate the slope
    m = numerator / denominator

    # Calcualte the Intersept
    b = yMean - m * xMean

    return m,b

def plotEquation(m,b):
    # Plot the salary/Experience data points
    plt.scatter(X,Y)

    # Plot the derived linear equation
    xPlane = np.linspace(int(xArray.min()), int(xArray.max()), int(yArray.max()))
    yPlane = m * xPlane + b
    plt.plot(xPlane, yPlane, '-r')
    # Show the plotting
    plt.grid()
    plt.show()

def displaySalary(m,b):
    try:
        while True:
            e = float(input("Enter your Years of Experience: "))
            # Calculate the salary
            salary = m * e + b
            print("Your estimated salary is: ", int(salary))
    except KeyboardInterrupt:
        exit()

if __name__ == "__main__":
    m,b = train()
    plotEquation(m,b)

    
    t1 = threading.Thread(target=displaySalary, args=(m,b))
    
    t1.start()
    





