import matplotlib.pyplot as plt
 # GRAPH 
# x = [2, 4, 5, 6]
# y = [2, 3, 6, 7]

# plt.plot(x, y, color='green', linestyle = 'dashed', linewidth = 3, marker = 'o', markerfacecolor = 'blue', markersize=12 )

# plt.ylim(1,8)
# plt.xlim(1,8)

# x2 = [1, 2, 3, 4]
# y2 = [1, 2, 4, 4]

# plt.plot(x2, y2, label = 'Line 2')



# plt.xlabel("X-Axis")

# plt.ylabel("Y-Axis")

# plt.title("Demo Graph - Two Lines")
  
# plt.legend()

# plt.show()

#BAR CHART
left = [1,2,3,4,5]
height = [10,11,23,36,4]

tick_label = ['one', 'two', 'three', 'four', 'five']
plt.bar(left, height, tick_label = tick_label, width= 0.8, color = ['blue', 'orange'])

plt.xlabel("X-Axis")

plt.ylabel("Y-Axis")

plt.title("Demo Graph - Bar Chart")

plt.show()