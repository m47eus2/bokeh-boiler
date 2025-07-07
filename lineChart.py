import numpy as np
from bokeh.plotting import figure, show

x = np.arange(0, 10, 1)
y1 = x ** 2
y2 = x ** 3
y3 = x ** 4

p = figure(title='Line chart',
           x_axis_label='x',
           y_axis_label='y')

p.line(x,y1, legend_label="Power of 2", line_width=2, color="blue")
p.line(x,y2, legend_label="Power of 3", line_width=2, color="red")
p.line(x,y3, legend_label="Power of 4", line_width=2, color="green")

show(p)