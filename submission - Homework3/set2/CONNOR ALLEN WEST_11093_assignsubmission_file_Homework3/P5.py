import argparse

parser = argparse.ArgumentParser()
g = 9.81
t = parser.add_argument('0.6')
v0 = parser.add_argument('3')
y = (v0*t)-(0.5*g*t**2)
print(y)