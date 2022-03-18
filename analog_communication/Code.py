# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 20:41:31 2022

@author: 20812018100700
"""

# import basis libraries
import matplotlib.pyplot as plt
import numpy as np




"""

Define Basic Functions.

  1.  unit step function
  2.  Gate Function
  3.  line plot
  4.  triangular function

"""

def u(t):
    """Unit step function"""
    return 1 * (t >= 0)

def gate(t, A=1):
    """    Gate Function"""
    # = 1, -a <= f  <= A"
    # = 0, else
    
    return 1 * (abs(t) <= A)

def linear(t):
    """line X = Y """
    return 1* (abs(t)) *(t<1)*(t>0)

def tri(t):
    """ triangular pulse"""
    return (1 - abs(t)) * (abs(t) < 1)



def plot_main_func():
    functions = [u, gate, linear, tri]
    t = np.linspace(-4, 4, 1000)

    plt.figure(figsize=(16, 8)) 
    for i, function in enumerate(functions, start = 1):
        plt.subplot(2, 2, i)
        plt.plot(t, function(t), '-b')
        plt.ylim((-0.5, 1.1))
        plt.grid()
        plt.title(function.__doc__)
    
    plt.tight_layout()
    plt.show()




"""
    define Proplems Functions 
"""

def S1(t):
    """ Signal 1"""
    return gate(t-3, 3) + gate(t-3, 1)

def S2(t):
    """ Signal 2"""
    return 2*u(-t+6) + 2*tri(t-3)

def S3(t):
    """ Signal 3"""
    return 4*linear(0.5*t)+4*gate(t-3) + 4*linear(0.5*(-t+6))

def S4(t):
    """ Signal 4"""
    return   (-4* tri((1/3)*(t-3))+4) * u(-t+6)

def S5(t):
    """ Signal 5 """
    return  (-4* tri(t-3)+4) * u(-t +6)

def S6(t):
    """ Signal 6"""
    return 4* (  linear(-0.5*(t-2)) +  linear(0.5*(t-4)) + u(-t)  )
    
"""
    plot the Problems func
"""
def plot_problems_functions():
    functions = [S1, S2, S3, S5, S5, S6]
    t = np.linspace(-1, 7, 10000)
    
    plt.figure(figsize=(16, 8)) 
    for i, function in enumerate(functions, start = 1):
        plt.subplot(2, 3, i)
        plt.plot(t, function(t), 'black')
        plt.ylim((-0.2, 4.25))
        plt.xticks(range(-1, 7) )
        plt.grid()
        plt.title(function.__doc__)
    
    plt.tight_layout()
    plt.savefig('all_fun.jpg')
    plt.show()
    
    
"""
    plot the solution
"""
    
def plot_solution_func():
    t = np.linspace(-15, 15, 100000)

    # the operation in the function 
    shift = [-t+2, t-1, 2*t-1, -2*t, 0.5*(t-2), -0.5*(t-1)]
    
    # the functions
    functions = [S1, S2, S3, S4, S5, S6]
    
    # Conditioning Y axes
    y_M = [ 2.5, 4.5, 4.5, 4.5, 4.5, 4.5 ]
    
    # Conditioning X axes
    x_R = [(-5, 3), (1, 8), (0, 5), (-4, 1), (5, 11), (-12, 5)]
    
    plt.figure(figsize=(16, 8)) 
    i = 1
    for t_, fun, y, x in zip(shift, functions, y_M, x_R):
        plt.subplot(2, 3, i)
        plt.plot(t, fun(t_), 'black')
        plt.ylim((-0.2, y))
        plt.xlim(x)
        plt.grid()
        plt.title("Signal {} solution".format(i))
        i+=1
    
    plt.tight_layout()
    plt.savefig('res_all_fun.jpg')
    plt.show()

def main():
    print("%10s"%("hellow "))
    print("what do you want to show:")
    print("1. the main 4 functions")
    print("2. the 6 problem functions")
    print("3. the solution of problem functions")
    print("*-*-"*15, end = "\n\n")
    
    try:
        ans = int(input("enter your choise number >>"))
        if ans in [1, 2, 3]:
            if ans == 1:
                plot_problems_functions()
                
            elif ans == 2:
                plot_problems_functions()
                
            elif ans == 3:
                plot_solution_func()
                
        else:
            print("please chose number from 1 to 3")
            main()
    
                
        
    except:
        print("please enter valus number")
        main()
        
    main()


if __name__ == "__main__":
    main()