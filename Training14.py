import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data_visualization=pd.read_csv('dataset_visualization.csv')
data_visualization

# 2. Scatter Chart
#Scatter chart can answer the question "How important data visualization is?"
#Let's see above example in dataset_visualization We use 3 data: dinos, aways, and stars. Let's see the statistics of those data. You will notice that those statistics are similar. But is it enough just to believe in statistics only?
dino=data_visualization['dataset']== "dino"
dinos=data_visualization[dino]
away=data_visualization["dataset"]=="away"
aways=data_visualization[away]
star=data_visualization["dataset"]=="star"
stars=data_visualization[star]

dinos.describe()
aways.describe()
stars.describe()

# Let's use visualize them using scatter plot
dinos.plot.scatter('x', 'y')
aways.plot.scatter('x', 'y')
stars.plot.scatter('x', 'y')
plt.show()