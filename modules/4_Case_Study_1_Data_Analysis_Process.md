---
layout: default
title: Data Analysis Process - Case Study 1
parent:  Introduction to Data Analysis
grand_parent: Modules
nav_order: 4
---

## Welcome To The Data Analysis Process - Case Study 1



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

[Assessing - Jupyter Notebook](modules/data_analysis_process/case_study_1/assessing_quiz.ipynb)

## Appending and NumPy

<iframe width="100%" height="653" src="https://www.youtube.com/embed/fdpKvovBMe4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

[Why is C so fast?](https://stackoverflow.com/questions/418914/why-is-c-so-fast-and-why-arent-other-languages-as-fast-or-faster)

Here are nice, short readings on how NumPy was created.

* [History of SciPy](https://scipy.github.io/old-wiki/pages/History_of_SciPy.html)
* Origin of NumPy on page 13 of [Guide to NumPy](http://csc.ucdavis.edu/~chaos/courses/nlp/Software/NumPyBook.pdf)

[Appending and NumPy - Jupyter Notebook](modules/data_analysis_process/case_study_1/appending.ipynb)
* Used [`np.repeat()`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.repeat.html) to create color column.

## Renaming columns

<iframe width="100%" height="561" src="https://www.youtube.com/embed/3Oo4gUP2_Rw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

* Index does not support mutable operations, in the video all of the column names are assigned to a new list then the list was modified and re assigned as the new columns.

[EDA Visuals -Jupyter Notebook](modules/data_analysis_process/case_study_1/eda_visuals.ipynb)

## Pandas Groupby

<iframe width="100%" height="561" src="https://www.youtube.com/embed/aWc18hHpXRk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Learn more about [pandas Groupby](https://pandas.pydata.org/pandas-docs/stable/groupby.html) and view its documentation [here](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.groupby.html).
