#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
a = np.loadtxt('Output_vacancies_Li-bcc-5-5-2.txt',usecols=5)
plt.hist(a,100)
z
plt.show()