---
layout: default
title: Hypothesis Testing
parent:  Practical Statistics
grand_parent: Modules
nav_order: 9
---

## Hypothesis Testing

<iframe width="100%" height="805" src="https://www.youtube.com/embed/9GbHHpiK6wk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


## Setting Up Hypothesis Tests - Part I

<iframe width="100%" height="805" src="https://www.youtube.com/embed/NpZxJg4S6X4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

In this video, you learned a few rules for setting up null and alternative hypotheses:

1. The <img src="https://render.githubusercontent.com/render/math?math=\large H_0 "> is true before you collect any data.

2. The <img src="https://render.githubusercontent.com/render/math?math=\large H_0 "> usually states there is no effect or that two groups are equal.

 3. The <img src="https://render.githubusercontent.com/render/math?math=\large H_0 "> and <img src="https://render.githubusercontent.com/render/math?math=\large H_1 "> are competing, non-overlapping hypotheses.

4. <img src="https://render.githubusercontent.com/render/math?math=\large H_1 ">is what we would like to prove to be true.

5. <img src="https://render.githubusercontent.com/render/math?math=\large H_0 "> contains an equal sign of some kind - either <img src="https://render.githubusercontent.com/render/math?math=\large\ = , ≤, ≥">.

6. <img src="https://render.githubusercontent.com/render/math?math=\large H_1 "> contains the opposition of the null - either <img src="https://render.githubusercontent.com/render/math?math=\large\ != , >, <">.


You saw that the statement, "Innocent until proven guilty" is one that suggests the following hypotheses are true:

* <img src="https://render.githubusercontent.com/render/math?math=\large H_0 ">: Innocent

* <img src="https://render.githubusercontent.com/render/math?math=\large H_1 ">: Guilty

We can relate this to the idea that "innocent" is true before we collect any data. Then the alternative must be a competing, non-overlapping hypothesis. Hence, the alternative hypothesis is that an individual is guilty.

## Setting Up Hypothesis Tests - Part II

<iframe width="100%" height="805" src="https://www.youtube.com/embed/nByvHz77GiA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Because we wanted to test if a new page was better than an existing page, we set that up in the alternative. Two indicators are that the null should hold the equality, and the statement we would like to be true should be in the alternative. Therefore, it would look like this:

<img src="https://render.githubusercontent.com/render/math?math=\large H_0: \mu_1 ≤ \mu_2">

<img src="https://render.githubusercontent.com/render/math?math=\large H_1: \mu_1 > \mu_2">

Here <img src="https://render.githubusercontent.com/render/math?math=\large\mu_1"> represents the population mean return from the new page. Similarly, <img src="https://render.githubusercontent.com/render/math?math=\large\mu_2"> represents the population mean return from the old page.

Depending on your question of interest, you would change your null and alternative hypotheses to match.

### Quiz- Set up Hypothesis:

### Q1

| Statement                                                                        | Hypothesis  | Reasoning                             |
|----------------------------------------------------------------------------------|-------------|---------------------------------------|
| The average height of all people in the world is different than 68 inches tall.  | Alternative | Conclusion after collecting some data |
| The average height of all people in the world is less than 68 inches tall.       | Alternative | Conclusion after collecting some data |
| The average height of all people in the world is less than or equal to 68 inches | Null        | Has zero effect -- "Equal to"         |
| The impact of Drug A is on average the same as Drug B.                           | Null        | Has zero effect --  "same"            |
| Drug A will on average have a larger impact than Drug B.                         | Alternative | Greater than -- "large"               |

### Q2

Consider the following statement:

"Dyson air purifiers are the best."

Which set of hypotheses could accurately test this statement?

Answer:
* Null: Dyson air purifiers are not the best.
* Alternative: Dyson air purifiers are the best.

### Q3

Consider the following statement:

"The average height of a human is smaller than or equal to 70 inches."

Which set of hypotheses below is correctly set up based on this assertion?

Answer:
* Null: The average height of a human is not greater than 70 inches.
* Alternative: The average height of a human is greater than 70 inches.

## Types of Errors - Part I

<iframe width="100%" height="805" src="https://www.youtube.com/embed/aw6GMxIvENc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## QUIZ QUESTION

There are two types of errors that are possible in hypothesis testing: Type I Errors and Type II Errors. Type I Errors are considered the worst type of error. Just based on this information, can you guess which truth/decision combo is each type of error?

| TRUTH/DECISION                                  | ERROR TYPE |
|-------------------------------------------------|------------|
| Truth: Innocent, Decision: Guilty               | Type 1     |
| Truth: Guilty, Decision: Innocent Type II Error | Type 2     |
| Truth: Innocent, Decision: Innocent             | No error   |
| Truth: Guilty, Decision: Guilty No Error        | No error   |

## Types of Errors - Part II

<iframe width="100%" height="805" src="https://www.youtube.com/embed/mbdSQ5CjdFs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Type I Errors

**Type I errors** have the following features:

1. You should set up your null and alternative hypotheses, so that the worse of your errors is the type I error.

2. They are denoted by the symbol **α**.

3. The definition of a type I error is: Deciding the alternative (<img src="https://render.githubusercontent.com/render/math?math=\large H_1 ">) is true, when actually (<img src="https://render.githubusercontent.com/render/math?math=\large H_0 ">) is true.

4. Type I errors are often called **false positives**.

5. Commonly these rates are 1-5%.

## Type II Errors

1. They are denoted by the symbol **β**.

2. The definition of a type II error is: Deciding the null (<img src="https://render.githubusercontent.com/render/math?math=\large H_0 ">) is true, when actually (<img src="https://render.githubusercontent.com/render/math?math=\large H_1 ">) is true.

3. Type II errors are often called **false negatives**.

4. Frequently people will talk about the "power" of a statistical test as 1 - beta (or 1 minus the type two error rate). This is the ability of an individual to correctly choose the alternative hypothesis.

In the most extreme case, we can always choose one hypothesis (say always choosing the null) to ensure that a particular error never occurs (never a type I error assuming we always choose the null). However, more generally, there is a relationship where with a single set of data decreasing your chance of one type of error, increases the chance of the other error occurring.

### Quiz: Types of Errors

n the following set of quizzes, you will be doing a recap and combination of the ideas that have been covered so far. Putting all of these pieces together is important for fully understanding hypothesis testing.

Consider we are interested in testing if the average revenue for a new marketing campaign is better than the previous marketing campaign.

We set up the null and alternative hypotheses in the following way:

![image](/practical_statistics/009.png)

where <img src="https://render.githubusercontent.com/render/math?math=\large \mu_o ">is the mean revenue of the old campaign, and <img src="https://render.githubusercontent.com/render/math?math=\large \mu_n ">is the mean revenue of the new campaign.

**Describe the Null hypothesis and Alternative Hypothesis**

* The null is that the mean revenue of the new campaign is less than or equal to the mean revenue of the old campaign.
* The alternative is that the mean revenue of the new campaign is larger than the mean revenue of the old campaign.

**Match the statement with the type of errors**

|                              STATEMENT                              |     ERROR     |
|:-------------------------------------------------------------------:|:-------------:|
| Deciding the new page is better, but really the old page is better. | Type I Error  |
| Deciding the old page is better, but really the new page is better. | Type II Error |

Let's try another situation. Consider you are testing a new cancer drug to see if it reduces tumor sizes in patients. Let <img src="https://render.githubusercontent.com/render/math?math=\large \mu_n "> be the average reduction in tumor size under the new drug. Let <img src="https://render.githubusercontent.com/render/math?math=\large \mu_o "> be the average reduction in tumor size under the old drug.

We set up the null and alternative hypotheses in the following way:

![image](/practical_statistics/009.png)

What does the null hypothesis suggest?

* The old treatment will reduce tumors as well or better than new treatments (on average).

Another way to state the null hypothesis

* The null is that the old drug works as well or better than the new drug.

Match the Errors

| STATEMENT                                                                                                               | ERROR         |
|-------------------------------------------------------------------------------------------------------------------------|---------------|
| Based on the study results we decide the new drug is better, but really the old drug is better at reducing tumor sizes. | Type I Error  |
| Based on the study results we decide the old drug is better, but really the new drug is better at reducing tumor sizes. | Type II Error |

## Types of Errors - Part III

<iframe width="100%" height="743" src="https://www.youtube.com/embed/Z-srkCPsdaM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


### Type I Errors

Type I errors have the following features:

1. You should set up your null and alternative hypotheses, so that the worst of your errors is the type I error.
2. They are denoted by the symbol **α**.
3. The definition of a type I error is: **Deciding the alternative is true, when actually the null is true.**
4. Type I errors are often called **false positives**.

### Type II Errors
1. They are denoted by the symbol **β**.
2. The definition of a type II error is: **Deciding the null is true when actually the alternative is true.**
3. Type II errors are often called false negatives.

### Parachute Example

This example let you see one of the most extreme cases of errors that might be committed in hypothesis testing. In a type I error an individual died. In a type II error, you lost 30 dollars.

In the hypothesis tests you build in the upcoming lessons, you will be able to choose a type I error threshold, and your hypothesis tests will be created to minimize the type II errors after ensuring the type I error rate is met.


![image](https://video.udacity-data.com/topher/2018/November/5bf30fdd_screen-shot-2018-11-19-at-11.32.05-am/screen-shot-2018-11-19-at-11.32.05-am.png)

## Common Types of Hypothesis Tests

<iframe width="100%" height="743" src="https://www.youtube.com/embed/8hv8KnvQ6JY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

You are always performing hypothesis tests on **population parameters**, never on statistics. Statistics are values that you already have from the data, so it does not make sense to perform hypothesis tests on these values.

Common hypothesis tests include:

1. Testing a population mean [(One sample t-test)](http://sites.utexas.edu/sos/guided/inferential/numeric/claim/one-sample-t/).

2. Testing the difference in means [(Two sample t-test)](https://www.isixsigma.com/tools-templates/hypothesis-testing/making-sense-two-sample-t-test/)

3. Testing the difference before and after some treatment on the same individual [(Paired t-test)](http://www.statstutor.ac.uk/resources/uploaded/paired-t-test.pdf)

4. Testing a population proportion [(One sample z-test)](http://stattrek.com/statistics/dictionary.aspx?definition=one-sample%20z-test)

5. Testing the difference between population proportions [(Two sample z-test)](https://onlinecourses.science.psu.edu/stat414/node/268)

You can use one of these sites to provide a t-table or z-table to support one of the above approaches:

* [t-table](https://s3.amazonaws.com/udacity-hosted-downloads/t-table.jpg)
* [t-table or z-table](http://www.z-table.com/t-value-table.html)

There are literally hundreds of different hypothesis tests! However, instead of memorizing how to perform all of these tests, you can find the statistic(s) that best estimates the parameter(s) you want to estimate, you can bootstrap to simulate the sampling distribution. Then you can use your sampling distribution to assist in choosing the appropriate hypothesis.

## How Do We Choose Between Hypotheses?

<iframe width="100%" height="433" src="https://www.youtube.com/embed/JkXTwS-5Daw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

In order to put this idea to practice, let's do an example. Follow along with the screencast below to see how this works. The video says the average height of coffee drinkers, but it is actually the average height of all individuals in the coffee dataset - some who drink coffee, but some who do not drink coffee.

After you work through the screencast, there is walk through of a second method we might use to choose between the competing hypotheses on the next concept. In this second screencast, you will use the common logic used in hypothesis testing. The video below uses the logic you gained in the earlier confidence interval lesson.

<iframe width="100%" height="433" src="https://www.youtube.com/embed/MghT95b6LbQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


Notice the variable upper is the same as the variable high in the video.

Using your confidence interval, you can simply look at if the interval falls in the null hypothesis space or in the alternative hypothesis space to choose which hypothesis you believe to be true.

In the above case, our interval was entirely below 70, which would suggest the null (the population mean is less than 70) is actually true.

## Simulating From the Null Hypothesis

In the previous lesson on confidence intervals, we saw how we could simulate a sampling distribution for a statistic by bootstrapping our sample data.

Alternatively, in hypothesis testing, we could simulate a sampling distribution from the null hypothesis using characteristics that would be true if our data were to have come from the null.

**Hypothesis tests are about an entire population of interest.**
