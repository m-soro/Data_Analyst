---
layout: default
title: Anaconda
parent:  Introduction to Data Analysis
grand_parent: Modules
nav_order: 1
---

# Anaconda

The video below is a demonstration of the concepts that you are going to learn in this lesson. It will show you the significance of creating virtual environments, introduce you to the Anaconda distribution, and demonstrate the use of `conda` to create a virtual environment and install packages into it. **It's alright if you are viewing all these steps for the first time**.

In the next few pages, you'll learn the fundamentals of all the tasks demonstrated here.

<iframe width="100%" height="433" src="https://www.youtube.com/embed/VXukXZv7SCQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


>[Anaconda](https://anaconda.org/) is a distribution of packages built for data science. It comes with conda, a package and environment manager. You'll be using conda to create environments for isolating your projects that use different versions of Python and/or different packages. You'll also use it to install, uninstall, and update packages in your environments. Using Anaconda has made my life working with data much more pleasant.

The list of commands used are in the video above are:
```
conda create -n tea_facts python=3
source activate tea_facts
conda list
conda install numpy pandas matplotlib
```
Anaconda comes with the Jupyter notebook package. If you are using Miniconda, you can install Jupyter notebook as:
```
conda install jupyter notebook
```

## What is Anaconda Distribution?

Anaconda is a program to manage (install, upgrade, or uninstall) packages and environments to use with Python. It's simple to install packages with Anaconda and create virtual environments to work on multiple projects conveniently.

Even if you already have Python installed, it will be beneficial to use Anaconda/Miniconda because:

1. Anaconda comes with a bunch of data science packages; you'll be all set to start working with data.
2. Using `conda` to manage your packages and environments will reduce future issues dealing with the various libraries you'll be using.

## Python Packages

A package is a bunch of modules, where each module consists of a set of classes and function definitions. After installing a particular package, you can import and use the functions defined in that package.

If we install Anaconda, then a basic few packages are installed by default. However, you can install any more packages, if needed.

## Anaconda Distribution

Anaconda is a fairly large download (~500 MB) because it comes with Python's most common data science packages. Anaconda is a software distribution that includes the following:

* **Anaconda Navigator** - It is a graphical user interface that helps open up any installed applications, such as Jupyter notebook or VS code editor. We will learn more about the notebook in the next lesson. See a snapshot of Anaconda Navigator below:

![image](https://video.udacity-data.com/topher/2020/September/5f741d48_screenshot-2020-09-26-at-5.03.28-pm/screenshot-2020-09-26-at-5.03.28-pm.png)

* **conda** - A command-line utility for package and environment management. Mac/Linux users can use the Terminal, and Windows users can use the "**Anaconda Prompt**" to execute `conda` commands. Windows users must run the Anaconda Prompt as an Administrator. Your first command should be
```
conda --version
```
If you are not comfortable on the command line, check out the command prompt tutorial for Windows or our Linux Command Line Basics course for OSX/Linux.

* **Python** - The latest version of Python gets installed as an individual package.

Over 160 scientific packages and their dependencies are also installed.
If you don't need all the packages or need to conserve bandwidth or storage space, there is an option for you - **Miniconda**.

## Miniconda

**Either Anaconda or Miniconda is adequate for this course**. [Miniconda](https://docs.conda.io/en/latest/miniconda.html) is a smaller distribution as compared to Anaconda, which includes only conda and Python. Miniconda can do everything Anaconda is capable of, but doesn't have the preinstalled packages. You can still install any of the available packages using `conda install PACKAGENAME` on the terminal/Anaconda Prompt. Interestingly, you can anytime upgrade from Miniconda to Anaconda by using the command:
```
conda install anaconda
```
In the command above, did you notice that we followed the same `conda install PACKAGENAME` syntax? See an example below to install the Numpy package with conda on the Terminal/Anaconda Prompt. You will see a demonstration soon after understanding the setup.

## Overview - Managing Packages using either `pip` or `conda`

![image](https://video.udacity-data.com/topher/2016/October/58114536_conda-install/conda-install.png)

>Installing numpy with conda

The conda and pip both are the Python package managers. Package managers are used to installing libraries and other software on your computer. pip is the default package manager for Python libraries, whereas conda focuses only on the packages that are available from the Anaconda distribution.

>Update Note
In the newer version of Anaconda/Miniconda, both pip and conda package managers are included by default, so you do not need to install them separately.

Both `pip` and `conda` gets installed when you install either Anaconda or Miniconda. On the next page, we will see details to install Anaconda/Miniconda. However, the `pip` also comes preinstalled with the Python 2 >=2.7.9 or Python 3 >=3.4.

In case if you have Anaconda/Miniconda already installed, and don't have pip in your system, there are two ways:

1. Refer to the [Pip installation instructions](https://pip.pypa.io/en/stable/installing/)
2. Install conda first and then install pip using conda. We will see commands for this step on the very next page because we will learn to install Anaconda/Miniconda next.

## Which one should I prefer - pip or conda?

There are two points you can consider before making a choice:

1. The available packages available from the Anaconda distribution in conda focus on data science, whereas pip is for general use. Conda installs precompiled packages. For example, the Anaconda distribution comes with Numpy, Scipy, and Scikit-learn compiled with the MKL library, speeding up various math operations. But, sometimes, you may need packages other than the ones listed on the Anaconda distribution.

2. Pip can install both Python and non-Python packages. Pip can install any package listed on the Python Package Index (PyPI).

**You can (and will) still use pip alongside conda to install packages**.

## Environments

A Python environment comprises a particular version of each of the following:

* Python interpreter,
* Python-packages, and
* The utility scripts, such as pip.
It is possible to have two or more environments residing on the same computer *virtually*. If you are using Anaconda, you are in the `base(root)` environment by-default.

![image](https://video.udacity-data.com/topher/2020/September/5f741e67_screenshot-2020-09-26-at-5.04.55-pm/screenshot-2020-09-26-at-5.04.55-pm.png)

>The default base(root) environment in Anaconda

![image](https://video.udacity-data.com/topher/2016/October/58114552_conda-create-env/conda-create-env.png)

>Creating an environment with conda

Along with managing packages, Conda is also a virtual environment manager. It's similar to [virtualenv](https://virtualenv.pypa.io/en/stable/) and [pyenv](https://github.com/yyuu/pyenv), other popular environment managers.

## Why do you need a Virtual Environment?

Each virtual environment remains isolated from other virtual environments, and the default “system” environment. **Environments allow you to separate and isolate the packages you are using for different projects**. Often you’ll be working with code that depends on different versions of some library. For example, you could have code that uses new features in Numpy, or code that uses old features that have been removed. It’s practically impossible to have two versions of Numpy installed at once. Instead, you should make an environment for each version of Numpy then work in the appropriate environment for the project.

This issue also happens a lot when dealing with Python 2 and Python 3. You might be working with old code that doesn’t run in Python 3 and new code that doesn’t run in Python 2. Having both installed can lead to a lot of confusion and bugs. It’s much better to have separate environments.

You can also export the list of packages in an environment to a file, then include that file with your code. This allows other people to easily load all the dependencies for your code. Pip has similar functionality with `pip freeze > requirements.txt`.

## Installing Anaconda

Anaconda is available for Windows, Mac OS X, and Linux. Follow the links below to get started:

1. Download the installer from https://www.anaconda.com/download/. Choose the Python 3.7 or higher version, and the appropriate 64/32-bit installer. If you already have Python installed on your computer, this won't break anything. Instead, the default Python used by your scripts and programs will be the one that comes with Anaconda.

2. Refer the installation instructions [here](https://docs.anaconda.com/anaconda/install/)

3. Verify the installation [here](https://docs.anaconda.com/anaconda/install/verify-install/) for your respective OS

After installation, you’re automatically in the default conda environment with all packages installed which you can see below. You can check out your own install by entering the following command into your terminal.

```
conda list
```

## List of Applications Installed with Anaconda
As we read on the previous page, the following packages will get installed with Anaconda:

* **Anaconda Navigator** - a GUI for managing your environments and packages
* **conda** - a command-line utility
* **Python** - The latest version of Python gets installed as an individual package.
* **Anaconda Prompt** - [Only for Windows] a terminal where you can use the command-line interface to manage your environments and packages
* A bunch of applications, such as **Spyder**. It is an IDE geared toward scientific development. In total, over 160 scientific packages and their dependencies are also installed.

To avoid errors later, it's best to update all the packages in the default environment. Open the Terminal/ Anaconda Prompt application. In the prompt, run the following commands:

```
conda upgrade conda
conda upgrade --all
```

and answer yes when asked if you want to install the packages. The packages that come with the initial install tend to be out of date, so updating them now will prevent future errors from out of date software.

>Note: In the previous step, running `conda upgrade conda` should not be necessary because `--all` includes the conda package itself, but some users have encountered errors without it.

In the rest of this lesson, you'll learn to use commands in your Terminal/Anaconda Prompt. I highly suggest you start working with command-line utility first, then later use the GUI if you'd like. Once you get acquainted with the command-line utility, refer to the [Starter Guide for Anaconda distribution (GUI)](https://docs.anaconda.com/_downloads/9ee215ff15fde24bf01791d719084950/Anaconda-Starter-Guide.pdf).

## Troubleshooting Resources

If you are facing difficulty in installing and running conda, refer to the FAQ - [Should I add Anaconda to the macOS/Linux/Windows PATH?](https://docs.anaconda.com/anaconda/user-guide/faq/). Additionally, the following links might be useful:

1. Linux/macOS -

* If you are seeing the "conda command not found" and are using ZShell, you have to add `export PATH="/Users/USERNAME/opt/anaconda/bin:$PATH"` to your .zsh_config file.

2.Windows users -

* ['export' is not recognized as an internal or external command](https://stackoverflow.com/questions/26368306/export-is-not-recognized-as-an-internal-or-external-command)
* ['Conda' is not recognized as internal or external command](https://stackoverflow.com/questions/44515769/conda-is-not-recognized-as-internal-or-external-command)

## How to Install pip Package Manager

If you have successfully installed Anaconda/Miniconda, possibly you will have conda (and pip) automatically installed on your system. If `pip` is not there, we recommend you install the pip as well because you will be able to run `pip` commands only after installing it.

```
# Check if pip is already installed, by running this command on Terminal/Anaconda Prompt
pip --version

# Once you have conda installed, run the command below on Terminal/Anaconda Prompt
conda install pip
```

>Update Note
In newer version of Anaconda/Miniconda, both pip and conda package managers are included by default, so you do not need to install them separately.

## Managing Packages

**Install Packages**

Once you have Anaconda installed, managing packages is fairly straightforward. To install a package, type the following command in your terminal.

```
conda install PACKAGE_NAME
```

For example, to install numpy, type `conda install numpy`.

You can install multiple packages at the same time. For example, the command below will install all three packages simultaneously.
```
conda install numpy scipy pandas
```
It's also possible to specify which version of a package you want by adding the **version number** such as `conda install numpy=1.10`.

Conda also automatically installs dependencies for you. For example `scipy` uses and requires `numpy`. If you install just `scipy` (`conda install scipy`), Conda will also install `numpy` if it isn't already installed.

## Remove Packages

Most of the commands are pretty intuitive. To uninstall, use
```
conda remove PACKAGE_NAME
```
## Update Packages

To update a package, use
```
conda update package_name
```

If you want to update all packages in an environment, which is often useful, use `conda update --all`. And finally, to list installed packages, it's `conda list` which you've seen before.

## Search a Package to Install

If you don't know the exact name of the package you're looking for, you can try searching with `conda search *SEARCH_TERM*`. For example, I know I want to install [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/), but I'm not sure of the exact package name. So, I try `conda search *beautifulsoup*`. Note that your shell might expand the wildcard `*` before running the conda command. To fix this, wrap the search string in single or double quotes like  `conda search '*beautifulsoup*'`.

It returns a list of the Beautiful Soup packages available with the appropriate package name, `beautifulsoup4`.

## Additional Resource

Refer to the [Conda Command reference guide](https://conda.io/projects/conda/en/latest/commands.html) to know more about conda commands, and compare them with `pip` and `virtualenv` commands.


## Managing Environments

As you saw on the previous page, conda can be used to create environments to isolate your projects. To create an environment, use the following command in your Terminal/Anaconda Prompt.

```
conda create -n env_name [python=X.X] [LIST_OF_PACKAGES]
```

Here -n env_name sets the name of your environment (-n for name) and LIST_OF_PACKAGES is the list of packages you want to be installed in the environment. If you wish to install a specific version of Python to be installed, say 3.7, use `python=3.7`. For example, to create an environment named `my_env` with Python 3.7, and install NumPy and Keras in it, use the command below.
```
conda create -n my_env python=3.7 numpy Keras
```

When creating an environment, you can specify which version of Python to install in the environment. This is useful when you're working with code in both Python 2.x and Python 3.x. To create an environment with a specific Python version, use either of the following commands:
```
conda create -n py3_env python=3
```
or
```
conda create -n py2_env python=2
```
I actually have both of these environments on my personal computer. I use them as general environments not tied to any specific project, but rather for general work with each Python version easily accessible. These commands will install the most recent version of Python 3 and 2, respectively. To install a specific version, use `conda create -n py python=3.6` for Python 3.6.

## Entering (Activate) an environment
Once you have an environment created, you can enter into it by using:
```
# For  conda 4.6 and later versions on Linux/macOS/Windows, use
conda activate my_env

#For conda versions prior to 4.6 on Linux/macOS, use
source activate my_env

#For conda versions prior to 4.6 on Windows, use
activate my_env
```

When you're in the environment, you'll see the environment name in the terminal prompt. Something like `(my_env) ~ $`.

## List the Installed Packages in the Current Environment

The environment has only a few packages installed by default, plus the ones you installed when creating it. You can check this out with

`conda list`

Installing packages in the environment is the same as before: `conda install package_name`. Only this time, the specific packages you install will only be available when you're in the environment.

## Deactivate an Environment
To leave the environment, type `conda deactivate` (on OSX/Linux) or `deactivate` (Windows).

```
# For  conda 4.6 and later versions on Linux/macOS/Windows, use
conda deactivate

#For conda versions prior to 4.6 on Linux/macOS, use
source deactivate

#For conda versions prior to 4.6 on Windows, use
deactivate
```
## Additional Resources
* [Managing virtual environments and packages with pip](https://docs.python.org/3/tutorial/venv.html)
* [Managing virtual environments with conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#managing-environments)
* [A comprehensive cheat sheet of Conda 4.6 commands](https://docs.conda.io/projects/conda/en/latest/_downloads/843d9e0198f2a193a3484886fa28163c/conda-cheatsheet.pdf)
* [A comprehensive cheat sheet of Conda version prior to 4.6 commands](https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf)

## Saving and loading environments

A really useful feature is sharing environments so others can install all the packages used in your code, with the correct versions. Let's see all the package-names, including the Python version present in the current environment, using the command:
```
conda env export
```
![image](https://video.udacity-data.com/topher/2016/October/5811639e_conda-env-export/conda-env-export.png)

>Exported environment printed to the terminal

In the above image, you can see the name of the environment, and all the dependencies (along with versions) are listed. You can save all the above information to a [YAML](http://www.yaml.org/) file, `environment.yaml`, and later share this file with other users over GitHub or other means. This file will get created (or overwritten) in your current directory.
```
conda env export > environment.yaml
```
The second part of the export command above, `> environment.yaml` writes the exported text to the environment.yaml. This file can now be shared using Github repository (or any other means), and others will be able to create the same environment you used for the project.

## Create an environment

To create an environment from an environment file, use the following command:
```
conda env create -f environment.yaml
```
The above command will create a new environment with the same name listed in `environment.yaml`.

## Listing environments

If you forget what your environments are named (happens to me sometimes), use either of the commands below to list out all the environments you've created.
```
conda env list
conda info --envs
```

## List the packages inside an environment

To view the list of packages, run the following command in your terminal / Anaconda Prompt,:
```
# If the environment is not activated
conda list -n env_name

# If the environment is activated
conda list

# To see if a specific package, say `scipy` is installed in an environment
conda list -n env_name scipy
```

## Removing an environment
If there are environments you don't use anymore, use the command below to remove the specified environment (here, named `env_name`).
```
conda env remove -n env_name
```

## Summary

At this moment, you must have completed the following steps before moving to the next lesson:

1. Install and navigate through the Anaconda
2. Download Python packages in Anaconda Terminal
3. Setup and manage one or more environments

Below are a few best practices that you can consider to incorporate in your programming habit.

## Using Environments

One thing that’s helped me tremendously is having separate environments for Python 2 and Python 3. I used the commands below to create two separate environments - py2_env and py3_env,
```
conda create -n py2_env python=2
conda create -n py3_env python=3`
```

**I created the same env too with numpy, pandas and matplotlib**

Now, I have a general use environment for each Python version. In each of those environments, I've installed most of the standard data science packages (NumPy, SciPy, Pandas, etc.). Remember that when you set up an environment initially, you'll only start with the standard packages in addition to whatever packages you specify in your `conda create` statement.

I’ve also found it useful to create environments for each project I’m working on. It works great for non-data related projects too, like web apps with Flask. For example, I have an environment for my personal blog using [Pelican](http://docs.getpelican.com/en/stable/).

## Sharing Environments

When sharing your code on GitHub, it's good practice to make an environment file and include it in the repository. You can do this using conda as:
```
conda env export > environment.yaml
```

## Share the List of Dependencies

For users not using conda, you may want to share the list of packages installed in the current environment. You can use pip to generate such a list as requirements.txt file using:
```
pip freeze > requirements.txt
```
Later, you can share this `requirements.txt` file with other users over Github. Once a user (or yourself) switches to another environment, you can install all the packages mentioned in the requirements.txt file using:

```
pip install -r requirements.txt
```
You can learn more [here](https://pip.pypa.io/en/stable/reference/pip_freeze/) about using `pip` instead of `conda`. This will make it easier for people to install all the dependencies for your code.

## Recommended Read

* To learn more about conda and how it fits in the Python ecosystem, check out this article by Jake Vanderplas: [Conda myths and misconceptions](https://jakevdp.github.io/blog/2016/08/25/conda-myths-and-misconceptions/).
* Here's the [conda glossary documentation](https://docs.conda.io/projects/conda/en/latest/glossary.html) for your reference.

## Python versions at Udacity

Most Nanodegree programs at Udacity, including DAND, will be (or are already) using Python 3 almost exclusively.

## Why we're using Python 3
* Jupyter has switched to Python 3 only
* Python 2.7 is being [retired](https://pythonclock.org/)
* Python 3 has been out for over 10 years, and there are very few dependencies (and none in this program) that are incompatible.

At this point, there are enough new features in Python 3 that it doesn't make much sense to stick with Python 2 unless you're working with old code. All new Python code should be written for version 3. Read more [here](https://wiki.python.org/moin/Python2orPython3).

## The main breakage between Python 2 and 3

For the most part, Python 2 code will work with Python 3. Of course, most new features introduced with Python 3 versions won't be backwards compatible. The place where your Python 2 code will fail most often is the print statement.

For most of Python's history including Python 2, printing was done like so:
```
print "Hello", "world!"
> Hello world!
```
This was changed in Python 3 to a function.
```
print("Hello", "world!")
> Hello world!
```
The print function was back-ported to Python 2 in version 2.6 through the __future__ module:
```
# In Python 2.6+
from __future__ import print_function
print("Hello", "world!")
> Hello world!
```
The `print` statement doesn't work in Python 3. If you want to print something and have it work in both Python versions, you'll need to import `print_function` in your Python 2 code.

Use Python 3 in DAND

[Top](#)
