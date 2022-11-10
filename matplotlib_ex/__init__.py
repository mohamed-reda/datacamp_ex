import matplotlib.pyplot as plt

year = [1, 2, 4, 5, 6, 7]
pop = [2, 4, 5, 6, 7.8, 1]
# line:
# plt.plot(year, pop)

# custom line:
plt.plot(year, pop)
plt.xlabel('year')
plt.ylabel('Population')
plt.title("This is the World Population")
plt.yticks([0, 2, 4, 6, 8, 10], [0, "b", 4, 6, 8, 10])
plt.grid(True)
# dots:
# plt.scatter(year, pop)

### Histogram:
# l = [0, 0, 6, 2, 3, 4, 2, 2, 2, 5, 6, 7, 3, 5, 6, 8, 9, 6]
# plt.hist(l, bins=3)
plt.show()
