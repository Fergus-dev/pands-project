# pands-project: Investigating the Iris Dataset with Python
by Fergus McTiernan

## About this project
In this project, I use [Python]() to investigate the Iris dataset, a commonly used dataset for learning data analysis and machine learning.

## The Iris Dataset
The Iris dataset consists of 150 samples of three different species of Iris flowers: setosa, versicolor and virginica. For each sample, there is data on four features: sepal length, sepal width, petal length, and petal width - all measured in centimeteres.

The Iris dataset seems to be a good choice for training machine learning algorithms because of its simplicity. There are only four features across three species of flowers, and [online sources](https://www.geeksforgeeks.org/iris-dataset/) claim that these features clearly distinguish one species of flower from another, so if training a machine learning model to predict a category based on the details provided, this dataset seems to be a very good choice doing so.

The simplicity of the dataset also makes it a good choice to learn data analysis through python, as it will allow me to focus on the data analysis tasks rather than getting overwhelmed or confused by a large and complicated dataset.

## How to use this project
You can follow my investigations into the Iris dataset to help yourself learn the Python programming language as it relates to data analysis by cloning this repository to your machine, or downloading my Jupyter notebook and Python script, along with the Iris dataset, from this repository individually. All necessary files are available in this repository and are labelled as follows:

  - Jupyter Notebook: analysis_notebook.ipynb
  - Python Script: analysis.py
  - Iris dataset: iris.data

If you would prefer to just run the script as a whole, then open up analysis.py on your machine (once Python is installed) and run it. You may need to [pip install](https://python.land/virtual-environments/installing-packages-with-pip) the packages I use in the script before hand, however. You can find a full list in the references section below. If you'd rather more explanation and to follow the step by step process, then use the analysis_notebook.ipynb file. I reccomend installing VS Code for this approach, in order to follow along with each stage of the coding process, as it is much more informative and easy to read due to the markdown cells that I have included in it.

  - [How to install Python](https://www.python.org/downloads/)
  - [How to install VS Code](https://code.visualstudio.com/docs/setup/windows)

## Summary of the my investigations into the Iris dataset
In analysis.ipynb and analysis.py, I take a number of key steps:
  - Dataset loading and preparation
  - Calculating summary statistics
  - Creating histograms for each variable
  - Creating scatter plots for each variable pair

  - Dataset loading and prep
    - Imported the Iris dataset from a .data file into a Pandas DataFrame.
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
    - Plotted histograms for each numeric variable to visualise their distributions
    - Combined all histograms into a single figure and saved it as ‘iris_histograms.png’

  - Creating scatter plots for each variable pair
    - Used scatter plots to visualize relationships between all pairs of numeric variables, with points color-coded by species
    - Saved the scatter plots as ‘iris_scatter_plots.png’

## Key findings
  - Summary statistics
    - The summary statistics generated show that sepal measurements show the least variation, while petal measurements show much more range and variability
  - Variable Distributions
    - Some variables exhibited more variability (e.g., ‘petal_length’), while others were more narrowly distributed.
  - Relationships Between Variables
    - Scatter plots revealed clear patterns and separations between species:
      - For example, ‘petal_length’ and ‘petal_width’ showed strong clustering by species.
      - Other pairs like ‘sepal_length’ vs. ‘sepal_width’ displayed weaker separations.

## References
- [Advantages of Python Pandas](https://data-flair.training/blogs/advantages-of-python-pandas/)
- [Determining Delimiters in Data Files](https://www.shanelynn.ie/using-pandas-dataframe-creating-editing-viewing-data-in-python/)
- [A Gentle Introduction to Summarizing Data](https://openelectiondata.net/en/academy/a-gentle-introduction-to-summarizing-data/)
- [Stack Overflow Discussion on Summarizing Data](https://stackoverflow.com/questions/43160381/printing-summary-of-results-in-python)
- [Writing to Files in Python](https://www.geeksforgeeks.org/writing-to-file-in-python/)
- [SciPy Documentation on Mode Calculation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.mode.html)
- [Matplotlib Plotting Library](https://matplotlib.org/stable/api/pyplot_summary.html)
- Python for Data Analysis by Wes McKinney (pages 283 - 286)
- [Python itertools Combinations](https://docs.python.org/3/library/itertools.html#itertools.combinations)
- [W3Schools on Python's enumerate() Function](https://www.w3schools.com/python/ref_func_enumerate.asp)
- [W3Schools on Python's map() Function](https://www.w3schools.com/python/ref_func_map.asp)

## Libraries and packages used
[pandas](https://pandas.pydata.org/)
[numpy](https://numpy.org/)
[stats from scipy](https://docs.scipy.org/doc/scipy/reference/stats.html)
[os](https://docs.python.org/3/library/os.html)
[matplotlib.pyplot](https://matplotlib.org/stable/api/pyplot_summary.html)
[combinations from itertools](https://www.geeksforgeeks.org/python-itertools-combinations-function/)


