import matplotlib.pyplot as py

# input_vals = [1,2,3,4,5]
# squares = [1,4,9,16,25]
# py.plot(input_vals,squares, linewidth = 5)
#
# #setting chart and axis labels
# py.title("Square Numbers", fontsize = 14)
# py.xlabel("Value", fontsize = 14)
# py.ylabel("Square of Value", fontsize = 14)
#
# #tick size
# py.tick_params(axis='both', labelsize = 14)
#
# py.show()

#######scatter plot
#scatter with custom color
#py.scatter(x_val, y_val, c=(0,0,0.8), edgecolor = 'none', s=40)

x_val = list(range(1,1001))
y_val = [x**2 for x in x_val]
py.scatter(x_val, y_val, c=y_val, cmap=py.cm.Blues, edgecolor = 'none', s=40)
#setting chart and axis labels
py.title("Square Numbers", fontsize = 14)
py.xlabel("Value", fontsize = 14)
py.ylabel("Square of Value", fontsize = 14)

#tick size
py.tick_params(axis='both', which='major', labelsize = 14)
py.axis([0,1100,0,1100000])
py.show()
