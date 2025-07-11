import numpy as np
from bokeh.layouts import row
from bokeh.plotting import figure, show

x = np.arange(0, np.pi*2, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)

p1 = figure()
p1.line(x,y1)
p1.sizing_mode = "scale_width"

p2 = figure()
p2.line(x,y2)
p2.sizing_mode = "scale_width"

p3 = figure()
p3.line(x,y3)
p3.sizing_mode = "scale_width"

show(row(children=[p1, p2, p3], sizing_mode="scale_width"))