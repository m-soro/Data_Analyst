---
layout: default
title: Jupyter
parent:  Introduction to Data Analysis
grand_parent: Modules
nav_order: 2
---
# Jupyter Notebook - First Demonstration

<iframe width="100%" height="433" src="https://www.youtube.com/embed/qiYDWFLyXvg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## What are Jupyter Notebooks?

Welcome to this lesson on using Jupyter notebooks. The notebook is a web application that allows you to combine explanatory text, math equations, code, and visualizations all in one easily sharable document. For example, here's one of my favorite notebooks shared recently, b[inary black hole signals in LIGO open data](https://www.gw-openscience.org/GW150914data/LOSC_Event_tutorial_GW150914.html) detected by the [LIGO experiment](https://www.ligo.caltech.edu/news/ligo20160211). You could download the data, run the code in the notebook, and repeat the analysis, in effect detecting the gravitational waves yourself! You can view a few more tutorial notebooks at [Gravitational Wave Open Science Center homepage](https://www.gw-openscience.org/tutorials/).

Notebooks have quickly become an essential tool when working with data. You'll find them being used for [data cleaning and exploration](http://nbviewer.jupyter.org/github/jmsteinw/Notebooks/blob/master/IndeedJobs.ipynb), visualization, [machine learning](http://nbviewer.jupyter.org/github/masinoa/machine_learning/blob/master/04_Neural_Networks.ipynb), and [big data analysis](http://nbviewer.jupyter.org/github/tdhopper/rta-pyspark-presentation/blob/master/slides.ipynb). Here's an [example notebook](https://github.com/mcleonard/blog_posts/blob/master/body_fat_percentage.ipynb) I made for my personal blog that shows off many of the features of notebooks. Typically you'd be doing this work in a terminal, either the normal Python shell or with IPython. Your visualizations would be in separate windows, any documentation would be in separate documents, along with various scripts for functions and classes. However, with notebooks, all of these are in one place and easily read together.

Notebooks are also rendered automatically on GitHub. It’s a great feature that lets you easily share your work. There is also http://nbviewer.jupyter.org/ that renders the notebooks from your GitHub repo or from notebooks stored elsewhere.

## Literate Programming
Notebooks are a form of [literate programming](http://www.literateprogramming.com/) proposed by Donald Knuth in 1984. With literate programming, the documentation is written as a narrative alongside the code instead of sitting off by its own. In Donald Knuth's words,

>Instead of imagining that our main task is to instruct a computer what to do, let us concentrate rather on explaining to human beings what we want a computer to do.

After all, code is written for humans, not for computers. Notebooks provide exactly this capability. You are able to write documentation as narrative text, along with code. This is not only useful for the people reading your notebooks, but for your future self coming back to the analysis.

Just a small aside: recently, this idea of literate programming has been extended to a whole programming language, [Eve](http://www.witheve.com/).

## How Notebooks Work

Jupyter notebooks grew out of the [IPython](https://ipython.org/) project started by Fernando Perez. IPython is an interactive shell, similar to the normal Python shell but with great features like syntax highlighting and code completion. Originally, notebooks worked by sending messages from the web app (the notebook you see in the browser) to an IPython kernel (an IPython application running in the background). The kernel executed the code, then sent it back to the notebook. The current architecture is similar, drawn out below.

![https://video.udacity-data.com/topher/2016/October/5817c83b_notebook-components/notebook-components.png]

The central point is the notebook server. You connect to the server through your browser and the notebook is rendered as a web app. Code you write in the web app is sent through the server to the kernel. The kernel runs the code and sends it back to the server, then any output is rendered back in the browser. When you save the notebook, it is written to the server as a JSON file with a `.ipynb` file extension.

The great part of this architecture is that the kernel doesn't need to run Python. Since the notebook and the kernel are separate, code in any language can be sent between them. For example, two of the earlier non-Python kernels were for the R and Julia languages. With an R kernel, code written in R will be sent to the R kernel where it is executed, exactly the same as Python code running on a Python kernel. IPython notebooks were renamed because notebooks became language agnostic. The new name Jupyter comes from the combination of Julia, Python, and R. If you're interested, here's a [list of available kernels](https://github.com/jupyter/jupyter/wiki/Jupyter-kernels).

Another benefit is that the server can be run anywhere and accessed via the internet. Typically you'll be running the server on your own machine where all your data and notebook files are stored. But, you could also set up a server on a remote machine or cloud instance like Amazon's EC2. Then, you can access the notebooks in your browser from anywhere in the world.


## Installing Jupyter Notebook

The Jupyter notebooks automatically get installed with the Anaconda distribution. You'll be able to use notebooks from the default environment.

If you are using Miniconda, there are multiple ways you can install the Jupyter notebook. You can install Jupyter notebooks in a conda environment using the following commands in your Terminal/Anaconda Prompt:

```python
# First, verify if you have Python and conda installed
# If the command below shows an error, try installing it first using `conda install python=3`
python --version
conda --version

# Use either of the commands below to install notebook
conda install jupyter notebook
conda install -c conda-forge notebook
```
If you are using pip, you can install Jupyter notebook with:
```python
# First, verify if you have pip installed. In recent versions of Python 2 >=2.7.9 or Python 3 >=3.4, pip comes preinstalled.
# If the `pip` command below shows an error, try installing pip from https://pip.pypa.io/en/stable/installing/
python --version
pip --version


# Use either of the commands below to install notebook
pip install notebook
pip install jupyter notebook
```
To run the notebook, run the following command at the Terminal (Mac/Linux) or Command Prompt (Windows) / Anaconda Prompt (Windows):
```python
jupyter notebook
```

## Launching the Notebook Server

To start a notebook server using a command-line interface, open the Terminal/Anaconda prompt, and navigate to the directory where you'd like to create notebook files (`.ipynb`). You can confirm the present working directory using `pwd`.
```
cd <directory_path>
pwd
```
Next, enter the following command in your terminal/Anaconda prompt
```
jupyter notebook
```
The command above will start the Notebook server in the current directory. Typically you'd want to start the server in the directory where your existing-notebooks reside. However, you can navigate through your file system to where the notebooks are present.

## Unable to Start the Jupyter Notebook Server?

Try troubleshooting the problem with the help of this post - [What to do when things go wrong?](https://jupyter-notebook.readthedocs.io/en/stable/troubleshooting.html#what-to-do-when-things-go-wrong)

![image](https://video.udacity-data.com/topher/2020/September/5f7319f6_screenshot-2020-09-29-at-3.15.16-pm/screenshot-2020-09-29-at-3.15.16-pm.png)

## Notebook Server Walkaround

When you run the `jupyter notebook` command (try it yourself!), the server home should open in your browser. By default, the notebook server runs at `http://localhost:8888`. If you aren't familiar with this, `localhost` means your computer and `8888` is the port the server is communicating on. As long as the server is still running, you can always come back to it by going to http://localhost:8888 in your browser.

If you start another server, it'll try to use port `8888`, but since it is occupied, the new server will run on port `8889`. Then, you'd connect to it at `http://localhost:8889`. Every additional notebook server will increment the port number like this.

If you tried starting your own server, it should look something like this:

![image](https://video.udacity-data.com/topher/2016/November/5818e181_notebook-server/notebook-server.png)

## Create a New Notebook

Over on the right, you can click on "New" to create a new notebook, text file, folder, or terminal. The list under "Notebooks" shows the kernels you have installed. Here I'm running the server in a Python 3 environment, so I have a Python 3 kernel available. You might see Python 2 here. I've also installed kernels for Scala 2.10 and 2.11 which you see in the list. See this [documentation](https://ipython.readthedocs.io/en/latest/install/kernel_install.html) for how to install kernels if you ever need to do so.

## Jupyter Notebook Server Tabs

The tabs at the top show *Files*, *Running*, and *Cluster*. Files shows all the files and folders in the current directory. Clicking on the Running tab will list all the currently running notebooks. From there you can manage them.

Clusters previously was where you'd create multiple kernels for use in parallel computing. Now that's been taken over by ipyparallel so there isn't much to do there.

## Notebook Conda Package

You should consider installing the Notebook Conda package to help manage your environments. Run the following terminal command:
```
conda install nb_conda
```
After successful installation of the nb_conda package, if you run the notebook server from a conda environment, you'll also have access to the "Conda" tab shown below. Here you can manage your environments from within Jupyter. You can create new environments, install packages, update packages, export environments, and much more.

![image](https://video.udacity-data.com/topher/2016/December/58473bf5_conda-tab/conda-tab.png)

Additionally, with `nb_conda` installed you will be able to access any of your conda environments when choosing a kernel. For example, the image below shows an example of creating a new notebook on a machine with several different conda environments:

![image](https://video.udacity-data.com/topher/2016/December/584739ab_conda-environments/conda-environments.png)

## Shutting down Jupyter

You can shutdown individual notebooks by marking the checkbox next to the notebook on the server home and clicking "Shutdown." Make sure you've saved your work before you do this though! Any changes since the last time you saved will be lost. You'll also need to rerun the code the next time you run the notebook.

![image](https://video.udacity-data.com/topher/2016/December/58474142_notebook-shutdown/notebook-shutdown.png)

You can shutdown the entire server by pressing control + C twice in the terminal. Again, this will immediately shutdown all the running notebooks, so make sure your work is saved!

![image](https://video.udacity-data.com/topher/2016/December/58474185_server-shutdown/server-shutdown.png)

## Notebook Interface

You can create a new notebook by clicking “new” and then choosing a kernel, such as python3.

![image](https://video.udacity-data.com/topher/2020/September/5f7319b0_screenshot-2020-09-29-at-3.15.27-pm/screenshot-2020-09-29-at-3.15.27-pm.png)

The command above will create a new notebook in a new browser tab, named `Untitled.ipynb`, as shown below:

![image](https://video.udacity-data.com/topher/2020/September/5f731d7e_new-notebook/new-notebook.png)

Feel free to try this yourself and poke around a bit.

You’ll see a little box outlined in green. This is called a cell. Cells are where you write and run your code. You can also change it to render Markdown, a popular formatting syntax for writing web content. I'll cover Markdown in more detail later. In the toolbar, click “Code” to change it to Markdown and back. The little play button runs the cell, and the up and down arrows move cells up and down.


![image](https://s3.amazonaws.com/content.udacity-data.com/courses/ud1111/notebook+interface.mp4)

When you run a code cell, the output is displayed below the cell. The cell also gets numbered, you see In [1]: on the left. This lets you know the code was run and the order if you run multiple cells. Running the cell in Markdown mode renders the Markdown as text.

### The tool bar

Elsewhere on the tool bar, starting from the left:

* The anachronistic symbol for "save," the floppy disk. Saves the notebook!
* The + button creates a new cell
* Then, buttons to cut, copy, and paste cells.
* Run, stop, restart the kernel
* Cell type: code, Markdown, raw text, and header
* Command palette (see next)
* Cell toolbar, gives various options for cells such as using them as slides

## Command palette

The little keyboard is the command palette. This will bring up a panel with a search bar where you can search for various commands. This is really helpful for speeding up your workflow as you don't need to search around in the menus with your mouse. Just open the command palette and type in what you want to do. For instance, if you want to merge two cells:

![image](https://s3.amazonaws.com/content.udacity-data.com/courses/ud1111/command+palette.mp4)

## More things
At the top you see the title. Click on this to rename the notebook.

Over on the right is the kernel type (Python 3 in my case) and next to it, a little circle. When the kernel is running a cell, it'll fill in. For most operations which run quickly, it won't fill in. It's a little indicator to let you know longer running code is actually running.

Along with the save button in the toolbar, notebooks are automatically saved periodically. The most recent save is noted to the right of the title. You can save manually with the save button, or by pressing escape then s on your keyboard. The escape key changes to command mode and s is the shortcut for "save." I'll cover command mode and keyboard shortcuts later.

In the "File" menu, you can download the notebook in multiple formats. You'll often want to download it as an HTML file to share with others who aren't using Jupyter. Also, you can download the notebook as a normal Python file where all the code will run like normal. The [Markdown](https://daringfireball.net/projects/markdown/) and [reST](http://docutils.sourceforge.net/rst.html) formats are great for using notebooks in blogs or documentation.

![image](https://video.udacity-data.com/topher/2016/December/58473c56_notebook-download/notebook-download.png)

## Code Cells
Most of your work in notebooks will be done in code cells. This is where you write your code and it gets executed. In code cells, you can write any code, assigning variables, defining functions and classes, importing packages, and more. Any code executed in one cell is available in all other cells.

To give you some practice, I created a notebook you can work through. Download the notebook Working With Code Cells below then run it from your own notebook server. Your browser might try to open the notebook file without downloading it. If that happens, right-click on the link then choose "Save Link As...". There are two ways to open the downloaded notebook locally:

In your terminal, change to the directory with the notebook file, then enter jupyter notebook.
If you have a Notebook server already up and running, you can either put the newly-downloaded file into the current working directory or use the “Upload” option in the NOtebook server.

[Top](#)
