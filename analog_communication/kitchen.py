import matplotlib.pyplot as plt
import numpy as np


t = np.linspace(0, 1, 1000)
A = 2
f0 = 5

x = A*np.cos(2*np.pi*f0*t)

plt.plot(t, x, 'r*')
plt.title(r'x(t) = 2\cos(2\pi 5t)')
plt.xlabel(r't (in s)')
plt.grid()


t = np.linspace(-4, 4, 10000)
x = np.sinc(t)
plt.plot(t, x, '-b')
plt.title(r'x(t) = sinc(t)')
plt.xlabel(r't (in s)')
plt.grid()



def p(t, A):
    """Basic rectangular pulse"""
    return 1 * (abs(t) < A/2)

+

def sgn(t):
    """Sign function"""
    return 1 * (t >= 0) - 1 * (t < 0)

def u(t):
    """Unit step function"""
    return 1 * (t >= 0)

functions = [p, pt, sgn, u]

t = np.linspace(-2, 2, 1000)

plt.figure()
for i, function in enumerate(functions, start=1):
    plt.subplot(2, 2, i)
    plt.plot(t, function(t+1), '-b')
    plt.ylim((-0.5, 1.1))
    plt.grid()
    plt.title(function.__doc__)
plt.tight_layout()
plt.show()

def gate(w, t):
    w = w/2
    return u(t+w)*u(-t+w)

def plo(f, title = "Function"):
    plt.plot(t, f, '-b')
    plt.ylim((-2.25, 2.25))
    plt.title(title)
    plt.tight_layout()
    plt.grid()
    plt.show()

h = u(t+2)
g = u(-t+2)

plo(h)
plo(gate(4)+ gate(2))


plt.plot(t, gate(2,2), '-b')
plt.ylim((-0.25, 1.25))
plt.title(function.__doc__)
plt.tight_layout()

t = np.linspace(-4, 7, 10000)


def Xt(t):
    return 1* (abs(t)) *(t<1)*(t>0)
plo(Xt(-t), "Function 1")


l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = [7, 8, 9]

for i, j, k in zip(l1, l2), l3:
    print("{} : {} : {}".format(i, j, k) )

