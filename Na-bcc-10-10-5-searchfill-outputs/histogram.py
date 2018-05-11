#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
a = np.loadtxt('Output_vacancies_Au-fcc-10-5-5.txt',usecols=5)
plt.hist(a,100)
plt.show()
print(a)
