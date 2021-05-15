---
layout: default
title: The Data Analysis Process
parent:  Introduction to Data Analysis
grand_parent: Modules
nav_order: 3
---
# The Data Analysis Process

[Jupyter Notebooks](#jupyter-notebooks)

<iframe width="100%" height="433" src="https://www.youtube.com/embed/1EzlGH4Biu0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


## Welcome to the Data Analysis Process

This is the first part of a three-lesson series on Python for Data Analysis. In this lesson, you will learn about the data analysis process and practice investigating different datasets with Python and pandas. In the next two lessons, you will perform case studies where you will thoroughly analyze two datasets and learn more about NumPy, Pandas, and Matplotlib.

This lesson is aimed at helping you quickly understand what happens at each step in the data analysis process. Though you will do a bit of coding just to build your intuition, a deeper dive of each individual topic is provided throughout the rest of this data analysis program.

**Programming and Python**

These lessons require some familiarity with Python. Here is an awesome free course you can take to learn or refresh your programming and Python skills!

[Introduction to Python Programming](https://www.udacity.com/course/introduction-to-python--ud1110)

**Other Helpful Resources**

* [NumPy and Pandas](https://classroom.udacity.com/courses/ud170) by Udacity to learn all about using NumPy and pandas.
* [Python for Data Analysis](http://www.ruxizhang.com/uploads/4/4/0/2/44023465/python_for_data_analysis.pdf) is one of the best resources for learning NumPy, Pandas, and Matplotlib, as it was written by the creator of the libraries you will be learning about, Wes McKinney. This is an exhaustive guide to using these libraries. Personally, I own two copies: one for work and one for home.

You will be putting these skills to use throughout the rest of this nanodegree program.

## Problems Solved by Data Analysts

<iframe width="100%" height="653" src="https://www.youtube.com/embed/zbjRiYSSR_Y" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


Intelligent analysis of data can result in some awesome stuff!

### Applications of Data Analysis
* [Facebook's blog post](https://research.fb.com/exposure-to-diverse-information-on-facebook-2/) and [paper](https://research.fb.com/publications/exposure-to-ideologically-diverse-information-on-facebook/) on exposure to ideologically diverse information
* [Article](http://www.dezyre.com/article/how-big-data-analysis-helped-increase-walmart-s-sales-turnover/109) on how Walmart used big data analysis to increase sales
* [Wikipedia](https://en.wikipedia.org/wiki/Bill_James) page on how Bill James applied data analysis to baseball
* [Numerate's post](https://www.businesswire.com/news/home/20100527005551/en/Numerate%E2%80%99s-Ranking-Technology-Pharmaceutical-Gains-U.S.-Patent) on using data analysis to design pharmaceutical drugs

## Data Analysis Process Overview

<iframe width="100%" height="653" src="https://www.youtube.com/embed/qdV4sifMmWI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

We organized the data analysis process into five steps: Question, Wrangle, Explore, Draw Conclusions, and Communicate. Below is a review of the key points, but feel free to move ahead. We will practice each step as we go through the next sections, and you will get the whole process down in no time.

**Step 1: Ask questions**
Either you're given data and ask questions based on it, or you ask questions first and gather data based on that later. In both cases, great questions help you focus on relevant parts of your data and direct your analysis towards meaningful insights.

**Step 2: Wrangle data**
You get the data you need in a form you can work with in three steps: gather, assess, clean. You gather the data you need to answer your questions, assess your data to identify any problems in your data’s quality or structure, and clean your data by modifying, replacing, or removing data to ensure that your dataset is of the highest quality and as well-structured as possible.

**Step 3: Perform EDA (Exploratory Data Analysis)**
You explore and then augment your data to maximize the potential of your analyses, visualizations, and models. Exploring involves finding patterns in your data, visualizing relationships in your data, and building intuition about what you’re working with. After exploring, you can do things like remove outliers and create better features from your data, also known as **feature engineering**.

**Step 4: Draw conclusions (or even make predictions)**
This step is typically approached with machine learning or inferential statistics that are beyond the scope of this course, which will focus on drawing conclusions with descriptive statistics.

More on machine learning: [Machine Learning Engineer Nanodegree](https://www.udacity.com/course/machine-learning-engineer-nanodegree--nd009)

**Step 5: Communicate your results**
You often need to justify and convey meaning in the insights you’ve found. Or, if your end goal is to build a system, you usually need to share what you’ve built, explain how you reached design decisions, and report how well it performs. There are many ways to communicate your results: reports, slide decks, blog posts, emails, presentations, or even conversations. Data visualization will always be very valuable.

Before walking through each of these steps with real datasets using Python, let's build a bit of intuition for each step!

## Packages Overview

<iframe width="100%" height="653" src="https://www.youtube.com/embed/sCQoQsmI3F0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

One of the biggest reasons that Python is considered the standard language for data science is its powerful packages. **NumPy**, **Pandas**, and **Matplotlib** are three core packages for data analysis that we'll be learning to use in this course.

**Note**: This course aims to introduce these packages with a learning by doing approach as we go through the data analysis process. If you'd like full lessons on NumPy and Pandas, you can find them in lessons 2 and 3 of this [free course](https://classroom.udacity.com/courses/ud170). You can skip the first lesson, which analyzes data with pure Python.

## Asking Questions

<iframe width="100%" height="653" src="https://www.youtube.com/embed/EvhIgrXtOao" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Data Wrangling and EDA

<iframe width="100%" height="653" src="https://www.youtube.com/embed/EQXfxbUup0o" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Gathering Data

<iframe width="100%" height="653" src="https://www.youtube.com/embed/JsVg95-amjI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


[Link](https://classroom.udacity.com/nanodegrees/nd002/parts/af503f34-9646-4795-a916-190ebc82cb4a) to Data Wrangling Course.

## Exploring Data with Visuals

<iframe width="100%" height="653" src="https://www.youtube.com/embed/0i_9t4Wi0Og" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Plotting with Pandas

<iframe width="100%" height="653" src="https://www.youtube.com/embed/kR7KZFqciFE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

You can refer to the Pandas Visualization documentation [here](https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html).

## Drawing Conclusions

<iframe width="100%" height="653" src="https://www.youtube.com/embed/Glctk6ahdFU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Communicating Results

<iframe width="100%" height="653" src="https://www.youtube.com/embed/tmAlVZCbgFA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


## Communicating Results Example

<iframe width="100%" height="653" src="https://www.youtube.com/embed/Ae_UOATWmDM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


## Jupyter Notebooks

### [Reading Csv](https://github.com/m-soro/Data_Analyst/blob/main/modules/data_analysis_process/data_analysis_process/reading_csv.ipynb)

### [Assessing](https://github.com/m-soro/Data_Analyst/blob/main/modules/data_analysis_process/data_analysis_process/assessing.ipynb)

### [Cleaning](https://github.com/m-soro/Data_Analyst/blob/main/modules/data_analysis_process/data_analysis_process/cleaning_practice.ipynb)

### [Communicate Quiz](https://github.com/m-soro/Data_Analyst/blob/main/modules/data_analysis_process/data_analysis_process/communicate_quiz.ipynb)

### [Conclusions](https://github.com/m-soro/Data_Analyst/blob/main/modules/data_analysis_process/data_analysis_process/conclusions_quiz.ipynb)


[top](#)
