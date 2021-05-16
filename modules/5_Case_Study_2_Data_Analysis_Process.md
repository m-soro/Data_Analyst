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

## Jupyter Notebooks

1. [Assessing](https://nbviewer.jupyter.org/github/m-soro/Data_Analyst/blob/main/modules/data_analysis_process/case_study_2/assessing.ipynb)

2. [Cleaning Column Labes](https://nbviewer.jupyter.org/github/m-soro/Data_Analyst/blob/main/modules/data_analysis_process/case_study_2/cleaning_column_labels.ipynb) - Drop extraneous columns and standardize all columns e.g lower case and replace spaces with underscores

3. [Filter, Drop Nulls, Dedupe](https://nbviewer.jupyter.org/github/m-soro/Data_Analyst/blob/main/modules/data_analysis_process/case_study_2/filter_drop_dedupe.ipynb)

4. [Inspect Data Types](https://nbviewer.jupyter.org/github/m-soro/Data_Analyst/blob/main/modules/data_analysis_process/case_study_2/inspect_datatypes.ipynb)

5. [Fixing Data Types Pt 1 - `cyl`](https://nbviewer.jupyter.org/github/m-soro/Data_Analyst/blob/main/modules/data_analysis_process/case_study_2/fix_datatypes_cyl.ipynb)

6. [Fixing Data Types Pt 2 - 'air_pollution_score'](https://nbviewer.jupyter.org/github/m-soro/Data_Analyst/blob/main/modules/data_analysis_process/case_study_2/fix_datatypes_air_pollution.ipynb) - splitting row with string values into two rows then append them to original dataframe, then convert them to ints. Used pandas `apply` function.

[top](#)
