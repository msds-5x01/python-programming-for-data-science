# Test 1: Basics of Programming in Python

Please feel free to search for answers in reference materials in books or online. However please work individually and do not ask anyone else for the solutions.

## Section 1. Basic statements and expressions. (1 point each, 0.5 for partial answers)

#### 1. What will be the data types of `a` and `b` after evaluating the following code snippet:
```python
a = 3
b = a / 7
```

#### 2. *Control flow structures* define what statements get executed and in what order. What control structures make use of statements `continue` and `break`. 

#### 3. What features do the types `set` and a `dict` have in common?

#### 4. Name three differences between the types `list` and `set`?

#### 5. Which of the following variables will a value of type `tuple` after executing the following code (there coule be more than one choice)

```python
a = {1, 2, 3}
b = "1, 2, 3"
c = (1, 2, 3)
d = [1, 2, 3]
e = 1, 2, 3
```
`a`, `b`, `c`, `d`, or `e`?

#### 6. If you see the following expression:
```
city["population"] = 37_310
```
Which of the following data types is `city`: 
`list`, `tuple`, `dict`, `set`, `int`, or `float`?

#### 7. If you see the following statement:
```
g.add(item)
```
Which of the following data types is `g`:
`list`, `tuple`, `dict`, `set`, or `int`?


#### 8. In the following expression, which arithmetic operator will be calculated first?
```python
a = (b - r) * 2 ** c % 3
```

#### 9. And which operator will be evaluated last before the assignment?
```python
a = (b - r) * 2 ** c % 3
```

#### 10. Imagine you are given the variables `name` and `occupation` that are created like this:
```python
name = "Alice"
occupation = "student"
```

Write a python statement that uses `name` and `occupation` to print
```
Alice is a student.
```

#### 11. Imagine you are given the variable `person` that is created like this:

```python
person = {'name': 'Alice', 'occupation': 'student'}
```

Write a python statement that uses `person` to print
```
Alice is a student.
```

#### 12. How can you find out the data type of an object in python?

#### 13. You have the following list comprehension:

```python
array = [item for item in seq]    
```

Which of the following data types can `seq` be? 
* an `int`
* a `tuple`
* a `dict`
* a `float`
* a `set`
* a `string`

#### 14. What is the Python standard library? Name three modules from the standard library.

#### 15. Apply de Morgan's Law to simplify the logical expression in this `if` statement:

```python
if not(answer == "yes" or not file_is_found):
    print(a)
```

#### 16. Apply de Morgan's Law to simplify the following expression:

```python
if not(a is not None and a >= 0 and a != b):
    print(a)
```

#### 17.  The following code snippet has a bug and won't run. How should you fix it?

```python
for i in range(10):
    print(i * 3)
if i == 3:
    break
```

#### 18. What will the following code print and why?

```python
a = "False"
if a:
    print("Yes")
else
    print("No")
```

## 2 Simple programs: 5 points each

#### 19. Write code that prints a countdown from 100 to 0

```
100
99
98
...
2
1
0
```

#### 20. Write code that calculates and prints the sum all odd numbers from 1 to 99

#### 21. Define the function `roll_dice()` that returns a random number between 1 and 6. 
**Hint:** Which module do you need to import?

#### 22. Define the function `roll_dice(n)` that returns `n` random numbers between 1 and 6.
How do you make it so that calling `roll_dice()` with no arguments will flip two dice?

#### 23. Define the function `print_square_frame(side)` so that calling `print_square_frame(7)` would print 

```
# # # # # # #
#           #
#           #
#           #
#           #
#           #
# # # # # # #
```

You can assume that `side >= 2`.



#### 24. Define the function `print_rectangle(width, height)` so that calling `print_rectangle(6, 4)` would print 

```
# # # # # # 
# # # # # #  
# # # # # #  
# # # # # #  
```

#### 25. Define the function `print_diamond(side)` so that calling `print_diamond(5)` would print 
```
    #
   # #
  # # #
 # # # #
# # # # #
 # # # #
  # # #
   # #
    #
```

#### 26. Define the function `print_stairs(step, number)` so that calling `print_stairs(2,  5)` would print five stairs of with sides 2 as follows.

```
# # 
# #
# # # #
# # # #  
# # # # # #  
# # # # # # 
# # # # # # # # 
# # # # # # # # 
# # # # # # # # # #
# # # # # # # # # #  
```
And `print_stairs(5, 2)` would produce
```
# # # # #
# # # # # 
# # # # #
# # # # #
# # # # #
# # # # # # # # # #
# # # # # # # # # #
# # # # # # # # # #
# # # # # # # # # #
# # # # # # # # # #
```

#### 27. Define the function `is_right_triangle(a, b, c)`, which should return `True` if the numers of `a`, `b`, and `c` could be the sides of a right triangle.

Hint: In a right triangle, the square of one side is the sum of the squares of the two others.

These tests should pass:

```python
# these are right triangles, the function should return True
assert is_right_triangle(3, 4, 5)
assert is_right_triangle(8, 17, 15)
assert is_right_triangle(25, 24, 7)

# These are not right triangles, the function should return False
assert not is_right_triangle(3, 7, 3)
assert not is_right_triangle(10, 4, 4)
```

## 3. More difficult programs (10 points each)

#### 28. Define the function `clamp_zero(array)` that takes a sequence (list or tuple)  of numbers and returns the same list with all negative numbers replaces with zeros.
These tests should pass:

```python
assert clamp_zero((-3, 4, -5, 0, 9, -7, 0)) == [0, 4, 0, 0, 9, 0, 0] 
assert clamp_zero([0, 0, -7.5, 3, 5, 0, 7.2, -7.3]) ==  [0, 0, 0, 3, 5, 0, 7.2, 0] 
```

#### 29. Define the function `str_to_num` that takes a sequence (list or tuple) of numbers represented as strings and returns the same list with the same numbers represented as floats. Empty strings should become zeros.

These tests should pass:

```python
assert str_to_num(("3", "4", "5.5", "-7.7")) == [3, 4, 5.5, -7.7] 
assert str_to_num(["3", "", "-3.15", "0"]) ==  [3, 0, -3.15, 0] 
```

#### 30. Define the function `left_typed` that takes a string and returns `True` if the string can be typed with the left hand on the QWERTY keyboard with typical hand placement.  The keys reached by the left hand are `qwertasdfgzxcvb`.

It must pass the following `assert`

```python
assert left_typed("verterbrates") 
assert not left_typed("bacteria")
```

#### 31. Define the function `word_lengths` that takes a string and returns a list containing the lengths of all its words:

It must pass the following `assert`

```python
assert word_lengths("University of Saint Thomas") == [10, 2, 5, 6]
assert word_lengths("The Museum of Fine Arts") == [3, 6, 2, 4, 4]
```

#### 32. Write the code that computes the fraction of English words containing the letter `e`.
* Use the `english-words.txt` file from class assignments
* To verify, my answer was: 67.85%

#### 33. Write code that measures the **median** length of words in the English language
* Use the `english-words.txt` file from class assignments
* **Hint:** You may need to import a module from the standard library to compute the median.
* To verify, my answer was: 8

## 4. Challenging (15 points each)

For the final two problems, you will need to use the `us-cities.json` file from the class assignments. You will also need the list of US capitals. I provide below the code that creates a dictionary where the keys are state names and the values of capital city names.


```python
capitals_text = """
Montgomery, Alabama
Juneau, Alaska
Phoenix, Arizona
Little Rock, Arkansas
Sacramento, California
Denver, Colorado
Hartford, Connecticut
Dover, Delaware
Tallahassee, Florida
Atlanta, Georgia
Honolulu, Hawaii
Boise, Idaho
Springfield, Illinois
Indianapolis, Indiana
Des Moines, Iowa
Topeka, Kansas
Frankfort, Kentucky
Baton Rouge, Louisiana
Augusta, Maine
Annapolis, Maryland
Boston, Massachusetts
Lansing, Michigan
Saint Paul, Minnesota
Jackson, Mississippi
Jefferson City, Missouri
Helena, Montana
Lincoln, Nebraska
Carson City, Nevada
Concord, New Hampshire
Trenton, New Jersey
Santa Fe, New Mexico
Albany, New York
Raleigh, North Carolina
Bismarck, North Dakota
Columbus, Ohio
Oklahoma City, Oklahoma
Salem, Oregon
Harrisburg, Pennsylvania
Providence, Rhode Island
Columbia, South Carolina
Pierre, South Dakota
Nashville, Tennessee
Austin, Texas
Salt Lake City, Utah
Montpelier, Vermont
Richmond, Virginia
Olympia, Washington
Charleston, West Virginia
Madison, Wisconsin
Cheyenne, Wyoming
"""
capitals = dict(s.split(', ')[::-1] for s in capitals_text.splitlines() if s)
```

#### 35. Write code that saves information about capital cities into a JSON file.
* Read the `us-cities.json` file from the class assignments
* Create a new json file, `capital-cities.json` and write out only the state capitals into it.
* Note that `us-cities.json` does not contain some of the capitals because they either did not make the list of most populous cities or because they are listed differently (e.g. Nashville-Davidson for Nashville, Kentucky). Simply skip these capitals. So your `capital-cities.json` will contain some 44 entries rather than 50.

#### 36. Write code that saves information about the biggest city in each state a JSON file.
* Read the `us-cities.json` file from the class assignments
* Create a new json file, `biggest-cities.json` and write out only the state's biggest city into it.
* **Hint**: you can use the fact that the the cities in `us-cities.json` are sorted by population. Therefore, the first city that you encounter from a given state is the biggest city for that state.

### Extra credit (+10 points)

#### 37. Write the code that prints US state capitals that are also the most populous cities in their respective states.

