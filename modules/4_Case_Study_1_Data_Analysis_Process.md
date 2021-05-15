---
layout: default
title: Data Analysis Process - Case Study 1
parent:  Introduction to Data Analysis
grand_parent: Modules
nav_order: 4
---

# The Data Analysis Process - Case Study 1

[Jupyter Notebook for Case Study 1](#jupyter-notebooks)

<iframe width="100%" height="653" src="https://www.youtube.com/embed/DkjRzNwjSfo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

In this first case study, you'll perform the entire data analysis process to investigate a dataset on wine quality. Along the way, you'll explore new ways of manipulating data with NumPy and Pandas, as well as powerful visualization tools with Matplotlib.

<iframe width="100%" height="653" src="https://www.youtube.com/embed/V-iPdJfrscQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


We're going to investigate this [dataset](https://archive.ics.uci.edu/ml/datasets/Wine+Quality) on physicochemical properties and quality ratings of red and white wine samples. Let's take a closer look at its attributes and pose some questions for our analysis!

<iframe width="100%" height="653" src="https://www.youtube.com/embed/r7BHGq_0P9Q" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Reading CSV files isn't always the same process - you won't always know what to expect. Sometimes there could be different delimiters, missing column labels, blank lines, comments, header text, etc. Most of the time, quick trial and error with Pandas does the trick. Alternatively, you can inspect the file with a text editor or spreadsheet program, like Google Sheets. Although, this is not recommended for large files, as they could really slow or crash the program. A [better way](https://askubuntu.com/questions/261900/how-do-i-open-a-text-file-in-my-terminal) to inspect large files would be with your terminal. (You don't need to know about this for this lesson.)

## Assessing Data

Using Pandas, explore `winequality-red.csv` and `winequality-white.csv` in the Jupyter notebook below to answer quiz questions below the notebook about these characteristics of the datasets:

* number of samples in each dataset
* number of columns in each dataset
* features with missing values
* duplicate rows in the white wine dataset
* number of unique values for quality in each dataset
* mean density of the red wine dataset

This data was originally taken from [here](https://archive.ics.uci.edu/ml/datasets/Wine+Quality).

## Appending and NumPy

<iframe width="100%" height="653" src="https://www.youtube.com/embed/fdpKvovBMe4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

[Why is C so fast?](https://stackoverflow.com/questions/418914/why-is-c-so-fast-and-why-arent-other-languages-as-fast-or-faster)

Here are nice, short readings on how NumPy was created.

* [History of SciPy](https://scipy.github.io/old-wiki/pages/History_of_SciPy.html)
* Origin of NumPy on page 13 of [Guide to NumPy](http://csc.ucdavis.edu/~chaos/courses/nlp/Software/NumPyBook.pdf)


* Used [`np.repeat()`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.repeat.html) to create color column.

## Renaming columns

<iframe width="100%" height="561" src="https://www.youtube.com/embed/3Oo4gUP2_Rw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

* Index does not support mutable operations, in the video all of the column names are assigned to a new list then the list was modified and re assigned as the new columns.


## Pandas Groupby

<iframe width="100%" height="561" src="https://www.youtube.com/embed/aWc18hHpXRk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Learn more about [pandas Groupby](https://pandas.pydata.org/pandas-docs/stable/groupby.html) and view its documentation [here](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.groupby.html).

## Pandas cut

You can create a categorical variable from a quantitative variable by creating your own categories. [pandas' cut](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.cut.html) function let's you "cut" data in groups.

Using this, create a new column called `acidity_levels` with these categories:

Acidity Levels:
* High: Lowest 25% of pH values
* Moderately High: 25% - 50% of pH values
* Medium: 50% - 75% of pH values
* Low: 75% - max pH value

Here, the data is being split at the 25th, 50th, and 75th percentile. Remember, you can get these numbers with pandas' `describe()`! After you create these four categories, you'll be able to use groupby to get the mean quality rating for each acidity level.

![image](/modules/data_analysis_process/case_study_1/001.png)

## Pandas Query

Another useful function that we’re going to use is pandas' `query` function.

In the previous lesson, we selected rows in a dataframe by indexing with a mask. Here are those same examples, along with equivalent statements that use `query()`.

```python
# selecting malignant records in cancer data
df_m = df[df['diagnosis'] == 'M']
df_m = df.query('diagnosis == "M"')

# selecting records of people making over $50K
df_a = df[df['income'] == ' >50K']
df_a = df.query('income == " >50K"')
```

The examples above filtered columns containing strings. You can also use query to filter columns containing numeric data like this.

```python
# selecting records in cancer data with radius greater than the median
df_h = df[df['radius'] > 13.375]
df_h = df.query('radius > 13.375')
```

## Type & Quality Plot - Part 1

<iframe width="100%" height="561" src="https://www.youtube.com/embed/iRCS1sE78KI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

You can make aesthetically pleasing data visualizations with [seaborn](https://seaborn.pydata.org/). Here are some cool [examples](https://seaborn.pydata.org/examples/index.html).

## Type & Quality Plot - Part 2

<iframe width="100%" height="561" src="https://www.youtube.com/embed/Ui1rF6McOBA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Matplotlib Example

Below is the Type and Quality Plot created with Matplotlib. As you can see, Matplotlib gives us much more control over our visualizations.

![image](https://video.udacity-data.com/topher/2017/September/59c9f20c_matplotlib-preview-plot/matplotlib-preview-plot.png)

Before we jump into the making of this plot, let's walk through a simple example using Matplotlib to create a bar chart. We can use pyplot's [bar](https://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.bar) function for this.


[Quiz-Visualizing in Matplotlib](modules/data_analysis_process/case_study_1/matplotlib_example.ipynb)

## Type & Quality Plot with Matplotlib

Below is the code used to create this plot with Matplotlib.

https://video.udacity-data.com/topher/2017/September/59ca8967_matplotlib-preview-plot/matplotlib-preview-plot.png

[Example Plot](modules/data_analysis_process/case_study_1/plotting_type_quality.ipynb)

## Jupyter Notebooks

1. [Assessing](https://github.com/m-soro/Data_Analyst/blob/main/modules/data_analysis_process/case_study_1/assessing_quiz.ipynb)

2. [Appending and NumPy](https://github.com/m-soro/Data_Analyst/blob/main/modules/data_analysis_process/case_study_1/appending.ipynb)

3. [EDA Visuals](https://github.com/m-soro/Data_Analyst/blob/main/modules/data_analysis_process/case_study_1/eda_visuals.ipynb)

4. [Pandas cut and groupby](https://github.com/m-soro/Data_Analyst/blob/main/modules/data_analysis_process/case_study_1/conclusions_groupby_quiz.ipynb)

5. [Pandas query and groupby](https://github.com/m-soro/Data_Analyst/blob/main/modules/data_analysis_process/case_study_1/conclusions_query_quiz.ipynb)

6. [Matplotlib Example](https://github.com/m-soro/Data_Analyst/blob/main/modules/data_analysis_process/case_study_1/matplotlib_example.ipynb)

7. [Wine Visualizations Matplotlib](https://github.com/m-soro/Data_Analyst/blob/main/modules/data_analysis_process/case_study_1/wine_visualizations.ipynb)

8. [Type and Quality Visualization Matplotlib](https://github.com/m-soro/Data_Analyst/blob/main/modules/data_analysis_process/case_study_1/plotting_type_quality.ipynb)

[top](#)
