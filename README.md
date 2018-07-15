#### This is a test repo for getting familiar with Github

# Some things to consider for the BW script templates repo

## 1. Folder structure :file_folder:
### a) Less nested option
Files could be less nested, eg
* script-templates/device_type/client_name_script.py
* script-templates/device_type/client_name_data.csv
* script-templates/device_type/client_name_plot.pdf

### b) More nested option
Files could be nested in more folders, eg
* script-templates/device_type/basic/script.R
* script-templates/device_type/basic/data.csv
* script-templates/device_type/basic/plot.pdf

## 2. READMEs :clipboard:
### a) Less READMEs
1 main README in root folder, listing all the devices

### b) More READMEs
README for each script, listing things like dependencies and describing the sample datasets?

## 3. Dependencies :white_check_mark:
How do we highlight things like needing to install packages (in the script, in a readme etc?)
See packrat:
- https://rstudio.github.io/packrat/
- https://rstudio.github.io/packrat/walkthrough.html

## 4. Data :chart_with_upwards_trend:
Because the repositories are public, we want fake data sets that show the structure of how the data should look.

## 5. Wikis :raising_hand:
We could have Wikis for useful code snippets (rather than whole scripts) and best practice type things.
