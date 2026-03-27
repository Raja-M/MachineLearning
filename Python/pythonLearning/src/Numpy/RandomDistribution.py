from numpy import random
import numpy as np

x = random.randint(100)
print(x)

x = random.rand()#a random float between 0 and 1
print(x)

x = random.rand(5)
print(x)

x = random.rand(3, 5)
print(x)

x=random.randint(100, size=(5))
print(x)

x = random.randint(100, size=(3, 5))#2D array with 3 rows
print(x)

x = random.choice([3, 5, 7, 9])
print(x)

x = random.choice([3, 5, 7, 9], size=(3, 5))
print(x)
#data distribution, p-probability for the value
x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5))
print(x)
#random permitations
arr = np.array([1, 2, 3, 4, 5])
random.shuffle(arr)
print(arr)

arr = np.array([1, 2, 3, 4, 5])
print(random.permutation(arr))

#seaborn distribution

# import matplotlib.pyplot as plt
# import seaborn as sns

# sns.displot([0, 1, 2, 3, 4, 5])
# plt.show()

# sns.displot([0, 1, 2, 3, 4, 5], kind="kde")
# plt.show()

#normal distribution
# x = random.normal(loc=1, scale=2, size=(2, 3))
# print(x)

# sns.displot(random.normal(size=1000), kind="kde")
# plt.show()
