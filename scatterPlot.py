import numpy as np
from bokeh.plotting import figure, show

x = np.random.random(50) * 10
y = np.random.random(50) * 100

p = figure(title='Scatter Plot',
           x_axis_label='x',
           y_axis_label='y')

p.circle(x,y,legend_label='Some randoms', color='blue', size=12)

show(p)