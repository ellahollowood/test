
# coding: utf-8

# In[140]:

#bokeh basics
from bokeh.plotting import figure
from bokeh.io import output_notebook, show, export_svgs
from bokeh.models import ColumnDataSource, Range1d
import pandas as pd
import numpy as np


# In[78]:

df = pd.read_csv('data.csv')
df.head()


# # Editable variables

# In[79]:

#filename = 'un_bar.html'

page_width = 596
page_height = 160

y_baseline = 0
y_maxline = 800
numTickY = 5


# # Bar chart code

# In[80]:

output_notebook()


# In[147]:

#source
source = ColumnDataSource(df)
source.data['xLoc'] = [x+1 for x in source.data['index']]

countries = df['code'].tolist()
xLoc = df.index.values.tolist()
xLoc = [x+1 for x in xLoc]

#Set up figure
f = figure(x_range = countries, tools = '')
#Remove toolbar
f.toolbar.logo = None

#Set up plot width and height
f.plot_width = page_width
f.plot_height = page_height

#set range of numbers that appear on y axis
f.y_range = Range1d(start = y_baseline, end = y_maxline)
f.yaxis[0].ticker.desired_num_ticks = numTickY

#Style axis ticks
f.yaxis.major_tick_in = 1
#Removes x ticks
f.xaxis.major_tick_line_alpha = 0
#removes minor axis ticks
f.axis.minor_tick_line_color = None
#removes x grid lines
f.xgrid.grid_line_color = None

#Set tick line and grid color
f.yaxis.major_tick_line_color = '#919191'
f.ygrid.grid_line_color = '#919191'
f.yaxis.axis_line_alpha = 0

#Text sizes of labels
f.axis.major_label_text_font_size = "6pt"
f.axis.major_label_text_font = 'Apex New'
f.axis.major_label_text_font_style = 'bold'

#remove outline
f.outline_line_color = None

#create bar chart
f.vbar(x = 'code', width = 0.7, top = 'million_people', color="#F8B617", source = source)

show(f)


# # SVG export

# In[145]:

#Export as svg
f.output_backend = 'svg'
export_svgs(f, filename="python-plot.svg")


# In[ ]:



