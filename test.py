
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]

# Line Chart
plt.figure(figsize=(6, 4))
plt.plot(x, y, marker='o', linestyle='-', color='b')
plt.xlabel("Days")
plt.ylabel("Marks")
plt.title("Line Chart")
plt.show()