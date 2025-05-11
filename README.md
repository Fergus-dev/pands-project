# pands-project: Investigating the Iris Dataset with Python
by Fergus McTiernan

## About this project
In this project, I use [Python]() to investigate the Iris dataset, a commonly used dataset for learning data analysis and machine learning.

## The Iris Dataset
The Iris dataset consists of 150 samples of three different species of Iris flowers: setosa, versicolor and virginica. For each sample, there is data on four features: sepal length, sepal width, petal length, and petal width - all measured in centimeteres.

The Iris dataset seems to be a good choice for training machine learning algorithms because of its simplicity. There are only four features across three species of flowers, and [online sources](https://www.geeksforgeeks.org/iris-dataset/) claim that these features clearly distinguish one species of flower from another, so if training a machine learning model to predict a category based on the details provided, this dataset seems to be a very straightforward way of doing so.

For the same reason, It could be a good choice for performing data analysis tasks in python, because when producing scatter plots or histograms, being able to see clear distinctions in the features between species will let us know we are doing this correctly. It will also allow me to focus on the data analysis tasks, rather than getting overwhelmed or confused by a large and complicated dataset.

## How to use this project
You can follow my investigations into the Iris dataset to help yourself learn the Python programming language as it relates to data analysis by cloning this repository to your machine, or downloading my Jupyter notebook and Python script, along with the Iris dataset. All necessary files are available in this repository and are labelled as follows:

  - Jupyter Notebook: analysis_notebook.ipynb
  - Python Script: analysis.py
  - Iris dataset: iris.data

You will need to have Python installed on your machine in order to run the script, and I reccomend also installing VS Code in order to follow along with each stage of the coding process, as it is much more informative and easy to read due to the markdown cells that I have included in it.

  - How to install Python
  - How to install VS Code

## Summary of the my investigations into the Iris dataset
In analysis.ipynb and analysis.py, I take a number of key steps:
  - Dataset loading and preparation
  - Calculating summary statistics
  - Creating histograms for each variable
  - Creating scatter plots for each variable pair

  - Dataset loading and prep
    - Imported the Iris dataset from a ‘.data’ file into a Pandas DataFrame.
    - Assigned column names: ‘sepal_length’, ‘sepal_width’, ‘petal_length’, ‘petal_width’, and ‘species’.
  
  - Calculating summary statistics
    - Calculated and saved key summary statistics for each numeric variable:
      - Mean
      - Median
      - Mode
      - Standard deviation
      - Variance
      - Range
    - Wrote these results to a text file, ‘summary.txt’.

  - Creating histograms for each variable
    - Plotted histograms for each numeric variable to visualize their distributions
    - Combined all histograms into a single figure and saved it as ‘iris_histograms.png’

  - Creating scatter plots for each variable pair
    - Used scatter plots to visualize relationships between all pairs of numeric variables, with points color-coded by species
    - Saved the scatter plots as ‘iris_scatter_plots.png’

## Key findings
  - Summary statistics
  - TBC
  - Variable Distributions
    - Some variables exhibited more variability (e.g., ‘petal_length’), while others were more narrowly distributed.
  - Relationships Between Variables
    - Scatter plots revealed clear patterns and separations between species:
      - For example, ‘petal_length’ and ‘petal_width’ showed strong clustering by species.
      - Other pairs like ‘sepal_length’ vs. ‘sepal_width’ displayed weaker separations.

