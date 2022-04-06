import math
import matplotlib.pyplot as plot
def step_h(h):
    return 0.01*math.cos(h)
x=0.1
while True:
    print(x)
    next_node=x+step_h(x)
    if (math.sin(next_node)<=math.sin(x)):
        break
    x=next_node
print("The max value of X is:",x)
print("The max value of the height Y is:",math.sin(x))