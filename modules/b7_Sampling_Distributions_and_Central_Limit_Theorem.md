---
layout: default
title: Sampling Distributions and Central Limit Theorem
parent:  Practical Statistics
grand_parent: Modules
nav_order: 7
---

## Descriptive Statistics VS Inferential Statistics

 * **Descriptive** - is about describing our collected data using the measures discussed throughout this lesson: measures of center, measures of spread, shape of our distribution, and outliers. We can also use plots of our data to gain a better understanding.

 ---

 * **Inferential** -  is about using our collected data to draw conclusions to a larger population. Performing inferential statistics well requires that we take a sample that accurately represents our population of interest.

A common way to collect data is via a survey. However, surveys may be extremely biased depending on the types of questions that are asked, and the way the questions are asked. This is a topic you should think about when tackling the the first project.

1. **Population** - our entire group of interest.
2. **Parameter** - numeric summary about a population
3. **Sample** - subset of the population
4. **Statistic** numeric summary about a sample

**QUIZ QUESTION**
Identify the population, parameter, sample, and statistic for the below scenario:

Consider we are interested in the average number of hours slept by all Udacity students (100,000 students). I send an email to all Udacity students, but I only receive 5,000 response emails. The average amount of sleep of those that responded was 6.8 hours of sleep.

**Population** `All Udacity Students`
**Parameter** `We cannot know for sure`
**Sample** `5,000 Udacity students`
**Statistic** `6.8 hours of sleep`


>Statistics and parameters are generally the mean or proportion for a group. Statistics being the value for the sample. Parameters being the value for the population. The population is our entire group of interest, while a sample is the selected subset of the population.

A **sampling distribution** is the distribution of a statistic.

![image](/practical_statistics/003.png)
![image](/practical_statistics/004.png)
![image](/practical_statistics/005.png)

[Sampling Distributions Quiz](https://nbviewer.jupyter.org/github/m-soro/Data_Analyst/blob/main/modules/practical_statistics/Sampling_Distributions_Quiz.ipynb)

[Sampling Distributions Solutions](https://nbviewer.jupyter.org/github/m-soro/Data_Analyst/blob/main/modules/practical_statistics/Sampling_Distributions_Solutions.ipynb)


## Sampling Distributions Notes

We have already learned some really valuable ideas about sampling distributions:

First, we have defined sampling distributions as the distribution of a statistic.

This is fundamental - I cannot stress the importance of this idea. We simulated the creation of sampling distributions in the previous ipython notebook for samples of size 5 and size 20, which is something you will do more than once in the upcoming concepts and lessons.

Second, we found out some interesting ideas about sampling distributions that will be iterated later in this lesson as well. We found that for proportions (and also means, as proportions are just the mean of 1 and 0 values), the following characteristics hold.

The sampling distribution is centered on the original parameter value.

The sampling distribution decreases its variance depending on the sample size used. Specifically, the variance of the sampling distribution is equal to the variance of the original data divided by the sample size used. This is always true for the variance of a sample mean!

In notation, we say if we have a random variable, <img src="https://render.githubusercontent.com/render/math?math=\LARGE\bar{X}">, with variance of <img src="https://render.githubusercontent.com/render/math?math=\LARGE\sigma^{2}">, then the distribution of <img src="https://render.githubusercontent.com/render/math?math=\LARGE\bar{X}"> (the sampling distribution of the sample mean) has a variance of <img src="https://render.githubusercontent.com/render/math?math=\LARGE\frac{\sigma^{2}}{n}">


## Notation

![image](/practical_statistics/notation_img.png)

[Notation Quiz](https://nbviewer.jupyter.org/github/m-soro/Data_Analyst/blob/main/modules/practical_statistics/Notation.ipynb)


​
