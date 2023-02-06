import matplotlib.pyplot as plt
import numpy as np
#inital question
compoundfrequency = input('''
Please type in how often you would like your investment to compound: 
daily
monthly
annually
''')
#starts code
if compoundfrequency == 'annually':
    #asks for starting principal
    P = float(input('Enter your starting principal: '))
    #asks for investment rate
    r = float(input('Enter your interest rate as a decimal(ex. 8% would be 0.08):  '))
    #creates the xvalues array
    IVterm = int(input('Enter your total investment period in years: '))
    #lets say i enter 70
    #creates the array
    Xvalues = []
    #for loop adds in the values from 0 to IVterm 
    for z in range(0,IVterm+1):
      Xvalues += [z]
    #creates Yvalues array
    Yvalues = []
    #compound frequency per year
    n = 1
    #adds in the y values using the functions
    for i in range(0, len(Xvalues)):
      Yvalues.append(P*(pow((1+r/n) , (n*Xvalues[i]))))
    #plots the graph

    plt.xlabel("Years")
    plt.ylabel("Money")   

    plt.bar(Xvalues,Yvalues)
    plt.show()
  

    for i in range(0, len(Xvalues)-1):
      print('The amount of money you will have is $' + str(P*(pow((1+r/n) , (n*Xvalues[i])))) + ' after ' + str(Xvalues[i]) + ' years.')

elif compoundfrequency == 'monthly':
    #asks for starting principal
    P = float(input('Enter your starting principal: '))
    #asks for investment rate
    r = float(input('Enter your interest rate as a decimal(ex. 8% would be 0.08):  '))
    #creates the xvalues array
    IVterm = int(input('Enter your total investment period in years: '))
    #lets say i enter 70
    Xvalues = []
    for z in range(0,IVterm+1):
      Xvalues += [z]

    Yvalues = []
    n = 12
    for i in range(0, len(Xvalues)):
      Yvalues.append(P*(pow((1+r/n) , (n*Xvalues[i]))))

    plt.xlabel("Years")
    plt.ylabel("Money") 

    plt.bar(Xvalues,Yvalues)
    plt.show()
  
    for i in range(0, len(Xvalues)-1):
      print('The amount of money you will have is $' + str(P*(pow((1+r/n) , (n*Xvalues[i])))) + ' after ' + str(Xvalues[i]) + ' years.')

elif compoundfrequency == 'daily':
    #asks for starting principal
    P = float(input('Enter your starting principal: '))
    #asks for investment rate
    r = float(input('Enter your interest rate as a decimal(ex. 8% would be 0.08):  '))
    #creates the xvalues array
    IVterm = int(input('Enter your total investment period in years: '))
    #lets say i enter 70
    Xvalues = []
    for z in range(0,IVterm+1):
      Xvalues += [z]

    Yvalues = []
    #n is 365 since it is compounded every day. 365 days in a year
    n = 365
    for i in range(0, len(Xvalues)):
      Yvalues.append(P*(pow((1+r/n) , (n*Xvalues[i]))))

    plt.xlabel("Years")
    plt.ylabel("Money") 

    plt.bar(Xvalues,Yvalues)
    plt.show()

    for i in range(0, len(Xvalues)):
      print('The amount of money you will have is $' + str(P*(pow((1+r/n) , (n*Xvalues[i])))) + ' after ' + str(Xvalues[i]) + ' years.')
#if user types in the wrong input
else:
    print('The frequency that you have chosen is not allowed. Please type either daily, monthly, or division')