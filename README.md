#### This is a test repo for getting familiar with Github

# Some things to consider for the BW script templates repo

## 1. Folder structure
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

## 2. READMEs
### a) Less READMEs
1 main README in root folder, listing all the devices

### b) More READMEs
README for each script, listing things like dependencies and describing the sample datasets?

## 3. Dependencies
How do we highlight things like needing to install packages (in the script, in a readme etc?)
--> packrat https://rstudio.github.io/packrat/

## 4. Wikis
We could have Wikis for useful code snippets (rather than whole scripts) and best practice type things.
