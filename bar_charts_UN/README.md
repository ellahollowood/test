### CONTENTS

This folder includes:
- :speech_balloon: Two scripts for creating bar charts on some of our UN projects. 1 in R, 1 in python.
- :page_facing_up: Sample data, so you can try it out with something that works first
- :bar_chart: An example of what the resulting plot should look like AND an example of what the final design that we're trying to recreate in code looks like

----

#### Unfinished business
We've tried to script as much as possible of the styling in code, but there's some things we haven't managed yet.

Here's the design we're aiming for:
![alt text](https://github.com/ellahollowood/test/blob/master/bar_charts/UN/Design.png)

And here's the R plot:
![alt text](https://github.com/ellahollowood/test/blob/master/bar_charts/UN/R%20Plot.png)

Here's a list of the bits of styling left to do:
- Label font
- Horizontal line thickness
- Continue the horizontal gridlines underneath the y axis labels
- Adjust the distance of the country code labels from the x axis

If you think you can add these details in, please:
1. Create a branch and work on the update the script
2. Commit this to the master when you're ready
3. Update this README file

Thanks!

### PYTHON BAR CHART

#### Working in python

First make sure python is installed on your computer. You can do this by navigating to your terminal and typing:
```
python
```
If it is not installed on your computer you will see:

```
'python' is not recognized as an internal or external command, operable program or batch file.
```
In which case you need to [download python here.](https://www.python.org/getit/)

If you do have python, make sure it's Python 3 by typing:

```
python -V
```

If not, got to the [python download page](https://www.python.org/getit/) to get the latest version.

### Creating chart

Files to download need:
- `requirements.txt` contains the required dependencies to run the code
- `data.csv` which will contain the data for your bar chart
- `python-plot.py` contains the python code to create the bar chart

Make sure these files are downloaded and in the same folder somewhere easy to find. 

First you need to navigate to the folder location on your terminal by using `cd`. For example:

```
cd/Desktop/GitHub/test/bar_charts_UN
```

Once in the folder, load the requirements doc.
```
 pip install -r requirements.txt
```

Now you're ready to create the chart. In your terminal type:
```
python python-plot.py
```

Once run, you should have a `python-plot.svg` ready to use.
