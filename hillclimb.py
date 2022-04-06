import math
import matplotlib.pyplot as plot
x=0.1
h=0.2
print("X values:")
while True:
    print(x)
    next_node=x+h
    if (math.sin(next_node)<=math.sin(x)):
        break
    x=next_node
print("The max value of X is:",x)
print("The max value of the height Y is:",math.sin(x))