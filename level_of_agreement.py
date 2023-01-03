import numpy as np
import skfuzzy as fuzz
from matplotlib import pyplot as plt

# [0, 10]
x = np.arange(0, 1.1, 0.1)


# Generate fuzzy membership functions
Ex_St_agree = fuzz.trimf(x, [0.9, 1, 1])
St_agree = fuzz.trimf(x, [0.7, 0.9, 1])
agree = fuzz.trimf(x, [0.5, 0.7, 0.9])
Mod_agree = fuzz.trimf(x, [0.3, 0.5, 0.7])
disagree = fuzz.trimf(x, [0.1, 0.3, 0.5])
St_disagree = fuzz.trimf(x, [0.0, 0.1, 0.3])
Ex_St_disagree = fuzz.trimf(x, [0.0, 0.0, 0.1])



print(x)

plt.title('Level of agreement')
"""
b: blue
g: green
r: red
c: cyan
m: magenta
y: yellow
k: black
w: white
"""
plt.plot(x, Ex_St_agree, 'b', linewidth=1.5, label='Estemely strogly agree')
plt.plot(x, St_agree, 'g', linewidth=1.5, label='Strogly agree')
plt.plot(x, agree, 'r', linewidth=1.5, label='agree')
plt.plot(x, Mod_agree, 'c', linewidth=1.5, label='Moderately agree')
plt.plot(x, disagree, 'm', linewidth=1.5, label='Disagree')
plt.plot(x, St_disagree, 'y', linewidth=1.5, label='Strongly Disagree')
plt.plot(x, Ex_St_disagree, 'k', linewidth=1.5, label='Extremely strongly disagree')



plt.legend()


plt.savefig("images/level_of_agreement.png")
plt.show()
