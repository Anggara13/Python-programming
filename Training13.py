# # 4. Matplotlib (Data Visualization)
# Why data visualization? A picture is worth a thousand words. Matplotlob is well-known library in python for visualization. Other library: seaborn, bokeh, plotly, even pandas can visualize.
# 
# There are 2 options in using matplotlib:
# 1. pyplot: does not explicitly specify the customization of the axis, the plot is simpler
# 2. pylab: is a combination of pyplot+numpy used in advanced graphics
# 
# Types of data visualization: 
# 1. Barchart 2. Histogram 3. Pie chart 4. Scatter 5. Line chart 6. Boxplot/Box-and-whisker plot
# 
# There is also so called magic function such as %matplotlib notebook & %matplotlib inline 

# **1. Line Chart**

# Start from the basic plot
import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(0,10) #Prepare data
plt.plot(x,x, color='black',label='linear')
#Add Legend
plt.legend()
#Show plot
plt.show()

# Multiple graph
plt.plot([1, 2, 3], [3, 6, 9],linestyle='--')
plt.plot([1, 2, 3], [2, 4, 9],linestyle=':')
plt.show()

# In the above example, we only 1 plot/image. How if more than 1 plot? PAKE SUPPLOTS
# Basically there are 3 steps: 1. Initialize figure and subfigure/axis 2. plot the data 3. save figure (if required)

# a. initialize figure
fig=plt.figure(figsize=(6,6)) # Make 1 image with multiple plots Figsize to adjust the size of the image in inches
# initialize subfigure -> It depends with how many plots that we want to visualize
ax1 = fig.add_subplot(121) # add_subplot(xyz): x=the number of rows, y=the number of columns, and z=which section
ax2 = fig.add_subplot(122) 
# So there are 1 row, 2 columns, meaning that there are 2 sections, 1. left & 2. right

# b. Plot data
ax1.plot([1,2,3,4],[4,3,2,1],label='ax1')
ax1.legend()
ax2.plot([1,2,3,4],[1,2,3,4],label='ax2')
# ax2.legend() -> See what the effect is
plt.show()

# c. Save data
plt.savefig('trial.jpg')
plt.savefig('trial.pdf', transparent=True) # If you want the background to be transparent, not white
