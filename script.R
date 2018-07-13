# Set working directory
setwd("~/Documents/Tools/RStudio/267_ScriptTemplates/bar_charts/UN")

# Load libraries
library(tidyverse)

# Load data
data <- read_csv("sample.csv")

# Define variables
x <- reorder(data$code, -data$million_people)
y <- data$million_people
width <- 0.73
fill <- "#FBB800"
min_value <- 0
max_value <- 800
y_limits <- c(min_value, max_value)
breaks <- c(0, 200, 400, 600, 800)

# Plot chart
plot <- ggplot(data,aes(x = x, 
                        y = y)) + 
        geom_bar(stat = "identity", fill = fill, width = width) + # width and spacing of bars
        expand_limits(y = y_limits) + # min and max of y axis
        scale_y_continuous(breaks = breaks) + # intervals for y axis breaks
        geom_hline(yintercept= 0, colour = "black", size = 0.5) + # thick baseline
        theme_minimal() +
        theme(panel.grid.major.y = element_line(colour = "#8D8D8D", size = 0.1), # colour and width of horizontal grid lines
              panel.grid.major.x = element_blank(), # remove gridlines
              panel.grid.minor = element_blank(), # remove gridlines
              axis.title.x=element_blank(), # remove x axis title
              axis.title.y=element_blank(), # remove y axis title
              axis.text.x = element_text(size = 5), # adjust size of x axis labels
              axis.text.y = element_text(vjust=-0.5, hjust=-0.8, size = 5), # position of y axis labels
              plot.margin = margin(1, 1.5, 1, 2,"cm")) # set margins
plot

# Save chart to right dimensions
ggsave("plot.pdf", width = 6.8, height = 1.84, units = "in")

# NB. STYLING LEFT TO DO
# font
# continue the horizontal gridlines underneath y axis labels
# adjust distance of country code labels from x axis