---
layout: default
title: Binomial Distribution
parent:  Practical Statistics
grand_parent: Modules
nav_order: 2
---
## Binomial Distribution

<iframe width="100%" height="664" src="https://www.youtube.com/embed/9gjCYs8f_PU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

[My Binomial Distribution Notebook](https://nbviewer.jupyter.org/github/m-soro/Data_Analyst/blob/main/modules/practical_statistics/Binomial_Distribution.ipynb)

The **Binomial Distribution** helps us determine the probability of a string of independent 'coin flip like events'.

The [probability mass function](https://en.wikipedia.org/wiki/Probability_mass_function) associated with the binomial distribution is of the following form:

![formula](/practical_statistics/formula.png)

where **n** is the number of events, **x** is the number of "successes", and **p** is the probability of "success".

We can now use this distribution to determine the probability of things like:

* The probability of 3 heads occurring in 10 flips.
* The probability of observing 8 or more heads occurring in 10 flips.
* The probability of not observing any heads in 20 flips.

**Looking Ahead**

The truth is that in practice, you will commonly be working with data, which might follow a binomial distribution. So it is less important to calculate these probabilities (though this can be useful in some cases), and it is more important that you understand what the Binomial Distribution is used for, as it shows up in a lot of modeling techniques in machine learning, and it can sneak up in our datasets with tracking any outcome with two possible events. You will get some practice with this in the **Python Probability Practice** lesson.

One of the most popular places you see the Binomial distribution is in [logistic regression](https://en.wikipedia.org/wiki/Logistic_regression), which you will learn about in the last lesson of this statistics course.

In the next section, you will begin to work with events that aren't independent. The events we have seen so far haven't influenced one another, but it turns out the real world is usually more complicated than this. The next section will introduce the idea of dependence, and you will learn even more with Bayes rule in the following section.

[top](#)
