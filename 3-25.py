import matplotlib.pyplot as plt

y = []
x = list(range(-100,101))

def f(x):
   return x * x - 3

# create x values
for n in x:
   y = y + [f(n)]

plt.plot(x, y)
plt.show()
