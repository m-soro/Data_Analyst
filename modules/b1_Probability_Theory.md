---
layout: default
title: Probability Theory
parent:  Practical Statistics
grand_parent: Modules
nav_order: 1
---
## Probability Theory

Probability Exercise

[My Probability Notebook](https://nbviewer.jupyter.org/github/m-soro/Data_Analyst/blob/main/modules/practical_statistics/Probability_Theory.ipynb)

Probability
Here you learned some fundamental rules of probability. Using notation, we could say that the outcome of a coin flip could either be T or H for the event that the coin flips tails or heads, respectively.

Then the following rules are true:

1. **P**(**H**) = 0.5


2. **1** - **P**(**H**) = **P**(**not H**) = 0.5

where **not H** is the event of anything other than heads. Since, there are only two possible outcomes, we have that **P**(**not H**) = **P**(**T**). In later concepts, you will see this with the following notation: **¬H**.

3. Across multiple coin flips, we have the probability of seeing **n** heads as **P**(**H**)**^n** . This is because these events are independent.

We can get two generic rules from this:

1. The probability of any event must be between 0 and 1, inclusive.

2. The probability of the complement event is 1 minus the probability of an event. That is the probability of all other possible events is 1 minus the probability an event itself. Therefore, the sum of all possible events is equal to 1.

3. If our events are independent, then the probability of the string of possible events is the product of those events. That is the probability of one event AND the next AND the next event, is the product of those events.

**Looking Ahead**
You will be working with the **Binomial Distribution**, which creates a function for working with coin flip events like the first events in this lesson. These events are independent, and the above rules will hold.

[top](#)
