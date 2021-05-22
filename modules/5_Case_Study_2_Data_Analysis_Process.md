---
layout: default
title: Data Analysis Process - Case Study 2
parent:  Introduction to Data Analysis
grand_parent: Modules
nav_order: 5
---

# Overview

[Jupyter Notebook for Case Study 2](#jupyter-notebooks)

<iframe width="100%" height="561" src="https://www.youtube.com/embed/2X8GJyZUlDo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Welcome To The Data Analysis Process - Case Study 2

In this second case study, you'll be analyzing [fuel economy data provided by the EPA](https://www.epa.gov/compliance-and-fuel-economy-data/data-cars-used-testing-fuel-economy), or Environmental Protection Agency.

### What is Fuel Economy?

Excerpt from Wikipedia page on Fuel Economy in Automobiles:

>The fuel economy of an automobile is the fuel efficiency relationship between the distance traveled and the amount of fuel consumed by the vehicle. Consumption can be expressed in terms of volume of fuel to travel a distance, or the distance travelled per unit volume of fuel consumed.

## Data Overview

<iframe width="100%" height="561" src="https://www.youtube.com/embed/u_qB4w4kL1o" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Data Source

Below are the web pages from this video. Note that the datasets we'll be working with are slightly simpler than those found here.

* [EPA Fuel Economy Testing](https://www.epa.gov/compliance-and-fuel-economy-data/data-cars-used-testing-fuel-economy)
* [DOE Fuel Economy Data](http://www.fueleconomy.gov/feg/download.shtml/)
* [Documentation Pdf](https://www.fueleconomy.gov/feg/EPAGreenGuide/GreenVehicleGuideDocumentation.pdf)

## Types of Merges

So far, we've learned about appending dataframes. Now we'll learn about [pandas Merges](https://pandas.pydata.org/pandas-docs/stable/merging.html#database-style-dataframe-joining-merging), a different way of combining dataframes. This is similar to the database-style "join." If you're familiar with SQL, this [comparison with SQL](https://pandas.pydata.org/pandas-docs/stable/comparison_with_sql.html#compare-with-sql-join) may help you connect these two.

Here are the four types of merges in pandas. Below, "key" refers to common columns in both dataframes that we're joining on.

1. Inner Join - Use intersection of keys from both frames.
2. Outer Join - Use union of keys from both frames.
3. Left Join - Use keys from left frame only.
4. Right Join - Use keys from right frame only.

Below are diagrams to visualize each type.

![image](https://video.udacity-data.com/topher/2017/October/59d3e866_inner-outer/inner-outer.png)

![image](https://video.udacity-data.com/topher/2017/October/59d3e874_left-right/left-right.png)

## Jupyter Notebooks

1. [Assessing](https://nbviewer.jupyter.org/github/m-soro/Data_Analyst/blob/main/modules/data_analysis_process/case_study_2/assessing.ipynb)

2. [Cleaning Column Labes](https://nbviewer.jupyter.org/github/m-soro/Data_Analyst/blob/main/modules/data_analysis_process/case_study_2/cleaning_column_labels.ipynb) - Drop extraneous columns and standardize all columns e.g lower case and replace spaces with underscores

3. [Filter, Drop Nulls, Dedupe](https://nbviewer.jupyter.org/github/m-soro/Data_Analyst/blob/main/modules/data_analysis_process/case_study_2/filter_drop_dedupe.ipynb)

4. [Inspect Data Types](https://nbviewer.jupyter.org/github/m-soro/Data_Analyst/blob/main/modules/data_analysis_process/case_study_2/inspect_datatypes.ipynb)

5. [Fixing Data Types Pt 1 - `cyl`](https://nbviewer.jupyter.org/github/m-soro/Data_Analyst/blob/main/modules/data_analysis_process/case_study_2/fix_datatypes_cyl.ipynb)

6. [Fixing Data Types Pt 2 - `air_pollution_score`](https://nbviewer.jupyter.org/github/m-soro/Data_Analyst/blob/main/modules/data_analysis_process/case_study_2/fix_datatypes_air_pollution.ipynb) - splitting row with string values into two rows then append them to original dataFrame, then convert them to ints. Used pandas `apply` function.

7. [Fixing Data Types Pt3 - `city_mpg`,`hwy_mpg`,`cmb_mpg`](https://nbviewer.jupyter.org/github/m-soro/Data_Analyst/blob/main/modules/data_analysis_process/case_study_2/fix_datatypes_mpg_greenhouse.ipynb) - used loop to correct data types. Result: final clean data.

8. [Exploring with Visuals](https://nbviewer.jupyter.org/github/m-soro/Data_Analyst/blob/main/modules/data_analysis_process/case_study_2/exploring_visuals.ipynb) - used scatter plots and histograms.

9. [Drawing Conclusions](https://nbviewer.jupyter.org/github/m-soro/Data_Analyst/blob/main/modules/data_analysis_process/case_study_2/drawing_conclusions.ipynb) - used scatter plots and histograms. [Udacity's Solution](https://nbviewer.jupyter.org/github/m-soro/Data_Analyst/blob/main/modules/data_analysis_process/case_study_2/drawing_conclusions_solutions.ipynb)

10. [Merging Datasets](https://nbviewer.jupyter.org/github/m-soro/Data_Analyst/blob/main/modules/data_analysis_process/case_study_2/merging_data.ipynb) - perform inner merge based on car models in 2008 and 2018.

11. [Results Merge](https://nbviewer.jupyter.org/github/m-soro/Data_Analyst/blob/main/modules/data_analysis_process/case_study_2/results_merged.ipynb) - using `idxmax()` or filtering dataframe to find the most improved vehicle.


[top](#)
