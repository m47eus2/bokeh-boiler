import numpy as np
from bokeh.plotting import figure, show, curdoc

#curdoc().theme = 'dark_minimal'

x = np.arange(0, 20, 1)
y1 = x ** 1.2
y2 = x ** 1.4
y3 = x ** 1.6

p = figure(title='Line chart',
           x_axis_label='x',
           y_axis_label='y')

p.width = 1280
p.height = 720

p.line(x,y1, legend_label="Power of 1.2", line_width=2, color="blue")
p.line(x,y2, legend_label="Power of 1.4", line_width=2, color="red")
p.line(x,y3, legend_label="Power of 1.6", line_width=2, color="green")

show(p)