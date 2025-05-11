import pandas as pd
import numpy as np
from scipy import stats as st
import os
import matplotlib.pyplot as plt
from itertools import combinations

# using the Pandas library's read_csv function to read the iris.data file into a Pandas DataFrame
# I have stored the iris.data file in the current working directory, so I use the os module to change to that directory
os.chdir('C:/Users/fmtie/OneDrive/Desktop/pands/pands-project')
# now I can easily call the iris.data file by its name rather than specifying the entire path
# As mentioned above, I don't specify the delimiter, and the function will automatically take it that it is a comma
# I also specify the column names that I want to use for the DataFrame by using the name argument
# The feature names 'sepal_length', 'sepal_width', 'petal_length', 'petal_width', and the fifth column is a categoriacal value corresponding to the species of iris flower
# I was able to find the column names in the iris.names file, which is contained in the same zip foler as the iris.data file

data = pd.read_csv('iris.data', header=None, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'])

# I call the data variable in order to view its contents
data

# calculating each summary statistic for the each variable using a for loop and writing this to a text file

# I use the os.path.join() function to create the full path to the summary.txt file
summary_file_path = os.path.join(current_directory, 'summary.txt')

# creating the text file
with open(summary_file_path, 'w') as f:
    # defining the for loop to iterate through each column in the DataFrame, ensuring it only includes numeric columns
    for column in data.select_dtypes(include=[np.number]).columns:
        f.write(f"Summary statistics for {column}:\n")
        # using numpy .mean() and .median() fucntions to calculate the summary statistics for each numeric column, as well as
        # scipy's stats module to calculate the mode
        f.write(f"Mean: {data[column].mean()}\n")
        f.write(f"Median: {data[column].median()}\n")
        f.write(f"Mode: {st.mode(data[column])}\n")
        # calculating the standard deviation, range, and variance using the numpy functions .std(), .var(), and .max() and .min()
        f.write(f"Standard Deviation: {data[column].std()}\n")
        f.write(f"Range: {(data[column].max() - data[column].min())}\n")
        f.write(f"Variance: {data[column].var()}\n")
        f.write("\n")

# The summary statistics for each variable are now written to the summary.txt file in the current working directory


# plots in matplotlib reside in a figure object, so I create that first
# this will allow me to create multiple plots in the same figure, or .png file, as discussed above
# I specify the size of the figure in inches using the figsize argument, to ensure it's big enough to display all the plots clearly
fig = plt.figure(figsize=(10, 8))

# creating the four subplots and specifying the size and postiion of each
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
ax4 = fig.add_subplot(2, 2, 4)

# now I create a histogram for each of the four numeric variables in the DataFrame
# I play around with the number of bins to see which gives the best insight into the distribution of the data, and set the width so they are clear using the rwidth argument
# I also specify the color and transparency of each histogram using the color and alpha arguments
ax1.hist(data['sepal_length'], bins=3, rwidth=0.8, color='blue', alpha=0.7)
ax2.hist(data['sepal_width'], bins=4, rwidth=0.8, color='green', alpha=0.7)
ax3.hist(data['petal_length'], bins=10, rwidth=0.8, color='red', alpha=0.7)
ax4.hist(data['petal_width'], bins=5, rwidth=0.8, color='purple', alpha=0.7)

# I also add titles and labels to each of the subplots using the set_title(), set_xlabel(), and set_ylabel() methods
ax1.set_title('Sepal Length Histogram')
ax1.set_xlabel('Sepal Length')
ax1.set_ylabel('Frequency')
ax2.set_title('Sepal Width Histogram')
ax2.set_xlabel('Sepal Width')
ax2.set_ylabel('Frequency')
ax3.set_title('Petal Length Histogram')
ax3.set_xlabel('Petal Length')
ax3.set_ylabel('Frequency')
ax4.set_title('Petal Width Histogram')
ax4.set_xlabel('Petal Width')
ax4.set_ylabel('Frequency')

# I also add a main title to the figure using the suptitle() method
fig.suptitle('Iris Flower Data Histograms')

# I save the figure to a .png file in the current working directory using the savefig() method
#fig.savefig('iris_histograms.png')

# I also show the figure using the show() method, which will display the figure in a window, just to check that everything looks correct
#plt.show()

# the spacing around my plots is a bit tight and the titles are getting cut off, so I use the fig.subplots_adjust() method to adjust the spacing
# Wes McKinney outlines this method on page 287 of his book, which I've referenced in the above markdown cell
fig.subplots_adjust(hspace=.5, wspace=.5)

plt.show()

# saving adjusted version of the figure to a .png file in the current working directory
fig.savefig('iris_histograms.png')

# Firstly, I create a subset of my dataset only containing the numerical columns so I can calculate all possible pairings of the numeric variables using itertools
numeric_data = data.select_dtypes(include=[np.number])

# I then use the combinations() function from the itertools module to create all possible pairings of the numeric variables
# The '2' argument specifies that I want to create pairings of two variables at a time
column_combinations = list(combinations(numeric_data.columns, 2))

# checking the column combinations
print(column_combinations)

fig2 = plt.figure(figsize=(16, 16))

# executing the for loop by iterating through the column combinations and assigning each combination to the variables v1 and v2
# then I create a scatter plot for each combination using the scatter() method
# I also specify the color of each point in the scatter plot using the map() method to map the species to a color
for i, (v1, v2) in enumerate(column_combinations):
    # I allow for all 6 combinations by specifying a 2 x 3 grid of subplots
    ax = fig2.add_subplot(2, 3, i + 1)
    ax.scatter(numeric_data[v1], numeric_data[v2], alpha=0.7, color=data['species'].map(colors))
    ax.set_xlabel(v1)
    ax.set_ylabel(v2)
    ax.set_title(f'Scatter Plot of {v1} vs {v2}')

plt.show()

fig2.subplots_adjust(hspace=.8, wspace=.8)

fig2.savefig('iris_scatter_plots.png')