---
layout: default
title: Confidence Intervals
parent:  Practical Statistics
grand_parent: Modules
nav_order: 8
---

## Confidence Intervals

<iframe width="100%" height="874" src="https://www.youtube.com/embed/gICzUhMVymo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

You can interpret your confidence interval as We are `95%` confident, the `population mean` falls between the bounds that you find. Notice that the percent and the parameter can both change depending on what you are building your confidence interval for, and what percentage you cutoff in each tail.

[Confidence Intervals Part 1](https://nbviewer.jupyter.org/github/m-soro/Data_Analyst/blob/main/modules/practical_statistics/Confidence_Intervals_Part_1.ipynb)

## Difference in Means

* Estimating difference in two parameters

<iframe width="100%" height="774" src="https://www.youtube.com/embed/8hrWGzjyhck" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

>Note at the end `diffs` should be `diff` when building the interval.

In this video, you built a confidence interval for the difference of the average heights for coffee drinkers and non-coffee drinkers. The interval was built at a 95% confidence level, and since the difference did not contain zero, this suggested there was truly a difference in the average heights in the population of coffee drinkers as compared to non-coffee drinkers.

Specifically, we can be `95`% confident that the `difference in the average heights for coffee drinkers as compared to non-coffee drinkers` was in the provided interval of 0.59 to 2.37 inches.

Notice the similarity of the wording to the last confidence interval you built. The highlighted portions signify the two parts that can change in your conclusions:

1. The confidence level.
2. The parameter you are capturing with your interval.

[Confidence Interval Part 2 - Sampling Distributions and Difference in Means](https://nbviewer.jupyter.org/github/m-soro/Data_Analyst/blob/main/modules/practical_statistics/Sampling_Distributions_Difference_in_Means.ipynb)

## Confidence Interval Applications

<iframe width="100%" height="722" src="https://www.youtube.com/embed/C0wgmeRx9yE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Practical vs Statistical Significance

<iframe width="100%" height="774" src="https://www.youtube.com/embed/RKHD1wzxxPA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Here, you learned about **practical** and **statistical** significance.

Using confidence intervals and hypothesis testing, you are able to provide **statistical significance** in making decisions.

However, it is also important to take into consideration **practical significance** in making decisions. **Practical significance** takes into consideration other factors of your situation that might not be considered directly in the results of your hypothesis test or confidence interval. Constraints like space, time, or money are important in business decisions. However, they might not be accounted for directly in a statistical test.

## Traditional Confidence Intervals

<iframe width="100%" height="433" src="https://www.youtube.com/embed/DmZwYHuz2eM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

One educated, but potentially biased opinion on the traditional methods is that these methods are no longer necessary with what is possible with statistics in modern computing, and these methods will become even less important with the future of computing. Therefore, memorizing these formulas to throw at a particular situation will be a glazed-over component of this class. However, there are resources below should you want to dive into a few of the hundreds if not thousands of hypothesis tests that are possible with traditional techniques.

To learn more about the traditional methods, see the documentation here on the Stat Trek site on the corresponding hypothesis tests. In the left margin of this [Stat Trek page](http://stattrek.com/hypothesis-test/hypothesis-testing.aspx), you will see a drop-down list of the hypothesis tests available, as shown in the image below.

![img](https://video.udacity-data.com/topher/2017/November/5a00d275_screen-shot-2017-11-06-at-1.14.05-pm/screen-shot-2017-11-06-at-1.14.05-pm.png)

Each of these hypothesis tests is linked to a corresponding confidence interval, but again the bootstrapping approach can be used in place of any of these! Simply by understanding what you would like to estimate, and simulating the sampling distribution for the statistic that best estimates that value.

## Traditional Confidence Interval Methods

<iframe width="100%" height="774" src="https://www.youtube.com/embed/eZ8lyiumXDY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

In this video you saw a comparison of the traditional method for calculating a difference of means using a python built in to the bootstrapping method you have been using throughout this lesson.

With large sample sizes, these end up looking very similar. With smaller sample sizes, using a traditional methods likely has assumptions that are not true of your interval. Small sample sizes are not ideal for bootstrapping methods though either, as they can lead to misleading results simply due to not accurately representing your entire population well.

## Other Language Associated with Confidence Intervals

<iframe width="100%" height="774" src="https://www.youtube.com/embed/9KYVRx7-llg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Quiz

Imagine we build a confidence interval for a population mean to obtain a confidence interval with an upper bound of 20 and a confidence interval width of 8. Use this information to provide the value to each of the corresponding additional values.

| Description                            | Value | Solution               |
|----------------------------------------|-------|------------------------|
| Upper Bound of the Confidence Interval |   20  | Given                  |
| Lower Bound of the Confidence Interval |   12  | Upper Bound - CI width |
| The Margin of Error                    |   4   | CI width/2             |
| The Sample Mean                        |   16  | (Upper + Lower)/2      |

**Increasing your sample size will narrow your confidence interval, and increasing your confidence level will widen your interval.**

## Correct Interpretations of Confidence Intervals

* What you **can say?**
* What you **CAN'T say?**

<iframe width="100%" height="774" src="https://www.youtube.com/embed/IhYv_SlN7e8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Quizzes - Interpreting Confidence Intervals:

#### Q1

Below are many interpretations of a confidence interval, but which is correct? What can we say from the ending results? Regardless of which page is "better," only one of these interpretations is possible from the results we obtain from a confidence interval.

| Choices                                                                                                                    | Answer |
|----------------------------------------------------------------------------------------------------------------------------|--------|
| We are 95% confident that if a user receives Page A they are more likely to click than if they receive Page B.             |  False |
| If a user receives Page A they are more likely to click than if they receive Page B.                                       |  False |
| We are 95% confident that the proportion of users that click through using Page A is higher than the average using Page B. |  True  |

* Remember you cannot talk about individual users with confidence intervals. Confidence intervals are for an aggregate about a population like a proportion or average.


#### Q2

As a second check, try another interpretation question about whether a clinical drug works. Which of the below is a statement that you could make about the drug?

|                                                Choices                                               | Answer |
|:----------------------------------------------------------------------------------------------------:|:------:|
| We are 95% confident the drug will work for all patients that try it.                                |  False |
| There is a 95% chance that if an individual takes a drug it will work for them.                      |  False |
| We are 95% confident that on average the drug will work for the members of this specific population. |  True  |

* For drugs to be approved, they must be rigorously tested, they are usually recommended for a particular population, and they will work on average. It is an overstatement to say that a drug will work for everyone or for any one individual.

## Quiz - Check for Big Ideas

| Statement                                                                                                                                                                     | Term                    |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|
| Sampling with replacement.                                                                                                                                                    | Bootstrapping           |
| Confidence intervals provide a range of values that are possible for a   ___ .                                                                                                | Parameter               |
| The distribution of a statistic (any statistic).                                                                                                                              | Sampling Distribution   |
| By simulating the distribution of our statistic(s) of interest using bootstrapping, we can remove the bottom 1.5% and top 1.5% of the sampling distribution to build a   __ . | 97% Confidence Interval |

## Recap
In this lesson, you learned:

1. How to use your knowledge of bootstrapping and sampling distributions to create a confidence interval for any population parameter.

2. You learned how to build confidence intervals for the population mean and difference in means, but really the same process can be done for any parameter you are interested in.

3. You also learned about how to use Python built-in functions to build confidence intervals, but that these rely on assumptions like the Central Limit Theorem.

4. You learned about the difference between **statistical significance** and **practical significance**.

5. Finally, you learned about other language associated with confidence intervals like **margin of error** and **confidence interval width**, and how to correctly interpret your confidence intervals. Remember, confidence intervals are about parameters in a population, and not about individual observations.

---

**What's Next**

The topics of confidence intervals and hypothesis testing essentially do the same thing, but depending on who you talk to or what source you are reading from, it is important to understand both.

In the next lesson, you will be learning about hypothesis testing!

[Top](#)
