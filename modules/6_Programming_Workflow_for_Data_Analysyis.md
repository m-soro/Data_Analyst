---
layout: default
title: Programming Work Flow for Data Analysis
parent:  Introduction to Data Analysis
grand_parent: Modules
nav_order: 6
---
## About IPython

[IPython](http://ipython.org/) is actually what provides the interactive Python kernel we use in Jupyter notebook. And in fact, we can use IPython outside of Jupyter notebook with its command-line interface in our terminal. This is very convenient and awesome for quick modifications, exploration, experimentation, and even running Python scripts!


To use IPython's command-line interface, just type in `ipython` in your terminal. This should work if you already have Jupyter notebook installed. Like we always did in the Jupyter notebook, let's import our packages and load into a dataset.

![image](https://video.udacity-data.com/topher/2017/October/59dcd9af_ipython-a1/ipython-a1.png)

Even though we are in the terminal, we can still view datasets the same way with `head`.

![image](https://video.udacity-data.com/topher/2017/October/59dcd9cd_ipython-a2/ipython-a2.png)

And although you're in IPython, you can still use command line commands! So we can do things like checking our directory for other files and renaming them.

![image](https://video.udacity-data.com/topher/2017/October/59dcc4cf_ipython-a3/ipython-a3.png)

Using IPython in your terminal can be very convenient for quick changes to your files. For example, if you wanted to change the column names in a dataset before sending off a csv file.

![image](https://video.udacity-data.com/topher/2017/October/59dcc4d9_ipython-a4/ipython-a4.png)

Visualizations here are also the same, except there's no `% matplotlib inline` since that's specific to Jupyter notebook. To have our visualizations show, we need to call `plt.show()`.

![image](https://video.udacity-data.com/topher/2017/October/59dcc4e4_ipython-a5/ipython-a5.png)

Entering that will open the plot in another window like this.

![image](https://video.udacity-data.com/topher/2017/October/59dcc509_ipython-a6/ipython-a6.png)

One thing I do in IPython all the time is test or experiment with different functions, algorithms, or just Python. Sometimes, I even do a quick check here to remember how a function works before reading documentation. (Although reading documentation is a VERY good idea!)

![image](https://video.udacity-data.com/topher/2017/October/59dcc514_ipython-a7/ipython-a7.png)

This was just a quick overview to expose you to a different tool you can use to practice your new Python for data analysis skills. If you'd like to learn more, make sure to check out the documentation linked above!

## Scripting Your Analysis
Being able to write and run scripts is invaluable for programming tasks and projects.

You can write your code in a text editor and then run the file in your terminal. Here's a simple example printing column names from the census income dataset. if you save your file as a .py file with the code shown on the right, you can run it as shown on the left. Make sure you are in the same directory you saved this file in!

![image](https://video.udacity-data.com/topher/2017/October/59dd0e0c_script-columns-simple/script-columns-simple.png)

Ideally, you'd group your analysis into functions and run them in your main function. This helps you organize your code and generalize if possible.

![image](https://video.udacity-data.com/topher/2017/October/59dd0e1a_script-columns-functions/script-columns-functions.png)

The script below creates a double histogram of ages for people with lower and higher incomes.

![image](https://video.udacity-data.com/topher/2017/October/59dd0f08_script-plot/script-plot.png)

You can imagine how `plot_hist` could be reused if we had more double histograms. This function could even be more generalized. If we were creating a script for many visualizations for this dataset, the query logic we have in the main function should probably move to a different function. If this project got really big, we could even separate our code into different files or modules to make it even more organized.

These were just simple examples to expose you to a different workflow. Writing and running scripts from your terminal is a very flexible and powerful way to program. This is more ideal as a development environment than Jupyter Notebook - which still works and is very useful, but more suited for things like reports.

I strongly recommend getting familiar with a good text editor and using the terminal if you aren't already. Then, you could do things like automating scripts to pull data from a database every morning to deliver daily insights! Even if you don't do anything fancy like that, it will still be very valuable to be familiar with a good text editor and terminal.

[top](#)
