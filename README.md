#MSDS 5X01 - Programming for Data Science

**MS Applied Data Science**

*Instructor:* Dr. Dimitri Yatsenko 

An introduction to programming in Python with emphasis on scientific computing, data analysis, and visualization.

The course will focus on practical problem solving, including individual assignments and group projects.

*Textbook:* Multiple sources are used for the course; all required materials and references will be provided in the lectures.

 0. Python's Standard Documentation: https://docs.python.org/3/
 1. Python's official tutorials, Beginner's Guide: https://wiki.python.org/moin/BeginnersGuide
 2. Allen B. Downey "Think Python 2e" https://greenteapress.com/wp/think-python-2e/
 3. Michael Driscoll's Python 101: https://python101.pythonlibrary.org/
 4. Wes McKinney "Python for Data Analysis, 2nd Edition" https://www.oreilly.com/library/view/python-for-data/9781491957653/
 5. Deitel, Deitel, and Deitel "Python for Programmers, 1st Edition" https://learning.oreilly.com/library/view/python-for-programmers/9780135231364/,  ISBN: 9780135231364

## Grading 
10 Assignments

|grade| percent |
|---|---|
|**A** |>=94%|
|**A-**|>=90%|
|**B+**|>=86%|
|**B**|>=82%|
|**B-**|>=78%|
|**C+**|>=74%|
|**C**|>=70%|
|**C-**|>=66%|
|**D+**|>=62%|
|**D**|>=58%|
|**F**|>=0%|


### Week 1: May 26, 28

* Command-line utilities and scripting.
* Configuring a programming environment for Python 3.6+
* Code management `git` and sharing with GitHub.
* Python Basics: Interactive work, programs, and literate programming with Jupyter.
* Statements and expressions. Assignments, variables, datatypes, and objects.
* [Assignment 01](assignments/Set01.md) - due June 2
* [Lecture 2](notebooks/001-Expressions.ipynb) - Homework 2 - due June 5 (5 pm)

### Week 2: June 2, 4

* Data structures: tuples, lists, strings, sets, dicts.
* Control flow: conditions and loops.
* Boolean logic.
* Work with strings and formatting.
* Functions.
* Introduction to algorithms.
* Comprehensions.
* Iterators and generators.
* PEP 8.
* [Lecture 3](notebooks/002-Structures.ipynb) - Homework 3 - due June 10 (5 pm) - [GitHubClassroom](https://classroom.github.com/a/wctz10P_)
* [Lecture 4](notebooks/003-Functions.ipynb) - Homework 4 - due June 12 (5 pm) - [GitHubClassroom](https://classroom.github.com/a/HFVLo876)

### Week 3: June 9, 11

* A few algorithms
* Work with files.
* The standard library.
* Python Package Index and `pip`.
* Modules and packages.
* CSV and JSON files.
* Regular expressions.
* Creating modules and packages.
* [Lecture 5](notebooks/004-Files.ipynb] - Homework 5 - due June 17 (5 pm) - 

### Week 4: June 16, 18

* Classes and object-oriented programming.
* Exceptions
* Scientific computing with `numpy` and `scipy`.
* Visualizations with `matplotlib`.


### Week 5: June 23, 25

* Operations on tabuar data with `pandas`
* Data analysis with `sklearn`.
* **Final project**

### Submitting homework through GitHub Classroom (will review in the June 9 lecture)

1. Follow the link provided in class to create the assignment repository
2. Wait (this may take many hours!) for GitHub to notify you that your repository is ready.
3. Follow the link to your repository
4. Under "Clone and download"  copy the URL. It will look something like `https://github.com/msds-5315/002-structures-dimitri-yatsenko.git`
5. Open a terminal shell on your computer and navigate to your work directory
6. Clone your homework repository with the command:
```shell
git clone https://github.com/msds-5315/002-structures-dimitri-yatsenko.git
```
 This will create a folder with the same name, e.g. `002-structures-dimitri-yatsenko`. This folder contains the contents of your assignment: programs, notebooks, files, etc.

7. Modify the contents of the folder to complete your homework
8. After completing your homework, add, commit, and submit your files:
```shell
cd <path-to-the-homework-folder>
git add -u 
git commit -m "Complete homework"
git push
```
9. Enjoy the rest of your day.
