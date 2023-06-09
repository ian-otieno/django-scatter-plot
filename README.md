# django-scatter-plot with statistics

This is a Django view that generates a scatter plot using plotly and displays statistics such as mean, mode, median, standard deviation, and coefficient of correlation. The view uses the numpy and statistics libraries to calculate these statistics.

## set up

To use this view, you'll need to have plotly installed in your Django project. You can install it using pip
pip install plotly

## usage

To use this view in your Django project, you can copy the scatter_view function into one of your views files and create a URL pattern that maps to it. 

## output

When you visit the URL for the scatter_view, you'll see a scatter plot with the following statistics displayed in the title:

Mean: the mean of the x-values and y-values, rounded to two decimal places
Mode: the mode of the x-values and y-values
Median: the median of the x-values and y-values
Standard Deviation: the standard deviation of the x-values and y-values, rounded to two decimal places
Coefficient of Correlation: the coefficient of correlation between the x-values and y-values, rounded to two decimal places
The plot and statistics are generated using the data x=[1, 2, 3] and y=[4, 2, 5] in this example. You can modify the code to use your own data.