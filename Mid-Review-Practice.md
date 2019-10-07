# Review 1: Basics of Programming in Python

#### 1. Name four data types in Python.

#### 2. *Control flow structures* define what statements get executed and in what order. Name three different control flow structures in Python.

#### 3. What do a `list` and a `tuple` have in common?

#### 4. What is the principal difference between a `list` and a `tuple`?

#### 5. Which of the following three variables has a value of type `list` after executing the following code:

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
p = city["population"]
```
Which of the following data types is `city`: 
`list`, `tuple`, `dict`, `set`, or `int`?

#### 7. If you see the following statement:
```
g.append(30)
```
Which of the following data types is `g`:
`list`, `tuple`, `dict`, `set`, or `int`?


#### 8. In the following expression, which arithmetic operator will be calculated first?
```python
a = b - r * 2 ** c % 3
```

#### 9. And which operator will be evaluated last before the assignment?
```python
a = b - r * 2 ** c % 3
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

#### 13. You have the following `for` loop:

```python
for i in seq:
    print(i)
```

Which of the following data types can `seq` be? 
* an integer
* a tuple
* a dict
* a float
* a set
* a string

#### 14. Write code that prints numbers from 0 to 100

```
0
1
2
...
98
99
100
```

#### 15. Write code that adds all numbers from 1 to 100

#### 16. What is the Python standard library? Name three modules from the standard library.

#### 17. Apply de Morgan's Law to simplify the following expression:

```python
if not(a != 3 and a > 0):
    print(a)
```

#### 18. Apply de Morgan's Law to simplify the following expression:

```python
if not(a is not None and a >= 10 or a not in {1, 2, 3}):
    print(a)
```

#### 19. Define the function `flip_coin()` that prints either "heads" or "tails" at random. 
Which module do you need to import?

#### 20. Define the function `flip_coins(n)` which is prints `"heads"` or `"tails"` `n` times.
How do you make it so that calling `flip_coins()` with no arguments flips only once?

#### 21.  The following code snippet has a bug and won't run. How should you fix it?

```python
for i in range(10):
print(i * 3)
```

#### 22. Why do the following expressions evaluate to `False` and `True`, respectively?

```python
"one" > "two"   

"three" > "four" 
```

#### 23. Define the function `print_square(side)` so that calling `print_square(7)` would print 

```
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #
```

#### 24. Define the function `print_triangle(side)` so that calling `print_triangle(7)` would print 

```
# 
# # 
# # # 
# # # # 
# # # # # 
# # # # # # 
# # # # # # #
```

#### 25. Define the function `print_triangles(side, number)` so that calling `print_triangle(6, 3)` would print three triangles with side 6.

```
# 
# # 
# # # 
# # # # 
# # # # # 
# # # # # # 

# 
# # 
# # # 
# # # # 
# # # # # 
# # # # # # 

# 
# # 
# # # 
# # # # 
# # # # # 
# # # # # # 
```

#### 26. Define the function `print_pyramid(side)` so that calling `print_pyramid(6)` would print a pyramid with sides 6 like so:

```
# 
# # 
# # # 
# # # # 
# # # # # 
# # # # # # 
# # # # # 
# # # # 
# # # 
# #
# 
```

#### 27. Define the function `validate_triangle(a, b, c)`, which should return `True` if the numers of `a`, `b`, and `c` could be the sides of a triangle.

Hint: In a flat triangle, no one side is longer than the sum of the two others.

These tests should pass:

```python
assert validate_triangle(3, 4, 5)
assert validate_triangle(3, 4, 2)
assert not validate_triangle(3, 7, 3)
assert not validate_triangle(10, 4, 4)
```

#### 28. Define the function `eliminate_zeros(array)` that takes a sequence (list or tuple)  of numbers and returns the list that omits all zeros from the original list.

These tests should pass:

```python
assert eliminiate_zeros((3, 4, 5, 0, 7, 0)) == [3, 4, 5, 7] 
assert eliminiate_zeros([0, 0, -7.5, 3, 5, 0, 7, -7.3]) ==  [-7.5, 3, 5, 7, -7.3] 
```

#### 29. Define the function `nones_to_zeros(array)` that takes a sequence (list or tuple) of numbers and `None`s and returns the same list with all `None`s replaced with zeros.

These tests should pass:

```python
assert nones_to_zeros((3, 4, 5, None, 7, None)) == [3, 4, 5, 0, 7, 0] 
assert nones_to_zeros([None, None, -7.5, 3, 5, None, 7, -7.3]) ==  [0, 0, -7.5, 3, 5, 0, 7, -7.3] 
```

#### 30. Define the function `acronym` that returns a string containing the first letters of each word in its input, capitalized.

It must pass the following `assert`

```python
assert acronym("University of Saint Thomas") == "UOST"
```

#### 31. Modify `acronym` to ignore the words `"of"` and `"the"`.

It must pass the following `assert`

```python
assert acronym("University of Saint Thomas") == "UST"
assert acronum("The Museum of Fine Arts") == "MFA"
```

#### 32. Write the code that computes the average length of words in English.
* Use the `english-words.txt` file from previous assignments

#### 33. Write the code that computes what fraction of English words are four-letter words.
* Use the `english-words.txt` file from previous assignments

#### 34. Write the code that computes the mean and median populations of the top 1000 US cities.
* Read the `us-cities.json` file from previous assignments
* Import the `statistics` module from the standard library

#### 35. Write code that saves information about Texas cities into a JSON file.
* Read the `us-cities.json` file from previous assignments
* Create a new json file, `texas-cities.json` and write out only the Texas cities into it.
