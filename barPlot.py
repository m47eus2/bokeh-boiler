import numpy as np
from bokeh.plotting import figure, show

x = np.arange(0, 10, 1)
y = np.random.random(10) * 10

p = figure(title='Bar Plot',
           x_axis_label='x',
           y_axis_label='y')

p.vbar(x=x, top=y, width=0.5, bottom=0, color='blue')

show(p)