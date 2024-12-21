
import matplotlib.pyplot as plt
import math

y = []
x = list(range(0, 361))

def f(x):
   return math.sin(math.radians(x))

# create x values
for n in x:
   y = y + [f(n)]

plt.plot(x, y)
plt.show()
