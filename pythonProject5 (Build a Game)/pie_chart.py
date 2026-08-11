from math import pi
import pandas
from bokeh.palettes import Category20c
from bokeh.plotting import figure, output_file, show
from bokeh.transform import cumsum

#Create Output html file
output_file("pie.html")
#Reading the csv data in Pandas form
data = pandas.read_csv("C:\\Users\\CHIKO\\Downloads\\countries.csv")
#Referencing the columns with the necessary data
country = data["Country"]
population = data["Population"]

#Configuring size, colour and creating the new plot with parameters
data['angle'] = data['Population'] / data['Population'].sum() * (2 * pi)
data['color'] = Category20c[len(data)]
p = figure(plot_height = 400, title = "Top 10 Countries By Population", toolbar_location = None, tools = "hover",
           tooltips = "@Country: @Population", x_range = (-0.5, 1.0))
p.wedge(x = 25, y = 12.5, radius = 0.6,
        start_angle = cumsum('angle', include_zero = True), end_angle = cumsum('angle'),
        line_color = "whote", fill_color = 'color', legend_field = 'Country', source = data)

#Setting optional parameters
p.axis.axis_label = None
p.axis.visible = True
p.grid.grid_line_color = None
#Display final result
show(p)