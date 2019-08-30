Problem Set 1
------

Sign up onto checkio.org and begin solving all problems in the Elementary category. 

1. Define the function `first_even(array)` that returns the first even elements from the its input argument, which is a list.

```python
def first_even(array): 
    # write your code here
    return 


# test:
assert first_even([1, 3, 7, 8, 4, 3, 7]) == 8
```

2. Define the function `avg_even(array)` that return the average value of all the even values in the list `array`.

```python
def avg_even(array):
    # write your code here
    return 

# test
assert avg_even([1, 3, 7, 2, 8, 3, 7, 6, 0]) == 4.0
```

3. Define the function `avg_skip(array, n_skip)` that returns the averge value of the numbers in the list `array` after skipping the first `n_skip` elements. 

```python
def avg_skip(array, n_skip):
   #  write your code here 
   return 

# test
assert avg_skip([1, 2, 7, 6, 5, 5], 2) == 5.75
```

4. Define the function `compute_trinomial(a, x)` that returns the value of the trinomial `a[2]*x^2 + a[1]*x + a[0]`.

```python
def compute_trinomial(a, x):
    # write your code here
    return 

# test
assert compute_trinomial([-7, 2, 1], 2) == 1.0
```

5. Extend the function above to `compute_polynomial(a, x)` that works for polynomials of any degree: `a[0] + a[1]*x + a[2]*x^2 + ... +a[n]*x^n`.

```python
def compute_polynomial(a, x):
    # write your code here
    return 

# test 
assert compute_trinomial([-7, 2, 1, 1], 2) == 9.0
```

6. Define the function `largest_rise(array)` that prints the largest number that is precided by a negative number in the input list:

``` python
# test
assert largest_rise([-3, 2, -7, 3, 9, -1, 0, 11]) == 3
```

7. Write a function `count_backwards` that counts from 100 to 0 by fives, printing the numbers.

```pyhon
# test
count_backwards()
100
95
90
85
...
```

8. Define the function `rock_paper_scissors(s1, s2)` where `s1` and `s2` both containing one of the following values `'paper'`, `'rock'`, or `'scissors`. Following the rules of the hand game Rock-Paper-Scissors, the function should return `1` if `s1` wins, `-1` if `s2` wins, and `0` if it's a draw.

```python
assert rock_paper_scissors('rock', 'paper') == -1
assert rock_paper_scissors('scissors', 'paper') == 1
assert rock_paper_scissors('paper', 'paper') == 0
```

9. Define the function `match_pattern(pattern, str)` that returns `True` when `str` matches `pattern` and `False` otherwise. A string matches the pattern if it has the same length and all the characters are the same but any dots `.` in `pattern` match any character in `str`:

```python
assert match_word('Houston', 'Houston') == True
assert match_word('houston', 'Houston') == False
assert match_word('..UST..', 'HOUSTON') == True
assert match_word('.i..i..i..i', 'Mississippi') == True
assert match_word('Data Science', 'Data Sc.ence') == False
```

10. Use the `match_pattern` function from Problem 9 to define the function `find_match` that returns the first string from a sequence of strings that matches the pattern. If no match is found return `None`: 

```python
assert match_word('..UST..', ['Houston', 'NASA', 'UST', 'HOUSTON', 'Bayou']) == 'HOUSTON'
```

11. Define the function `second_biggest(array)` that returns the second biggest number of the list of numbers `array`:

```python
assert second_biggest([93, 30, 39, 37, 78, 11, 7, 67, 63, 50, 92]) == 92
assert second_biggest([-1, -2, -3, -4, -5]) == -2

```

12. Define the function `middle(a, b, c)`, which returns the middle value of its three numerical inputs, i.e. the number that neither larger nor smaller than any of the other two

```python
assert middle(1, 2, 3) == 2
assert middle(-1, 3, -1) == -1
assert middle(0, -3, 7) == 0
assert middle(-3, -3, 4) == -3
```

13. Define the function `longest` that returns the longest string from a sequence of strings. If two strings have the same length, then only the first one should be consdered.

```python
assert longest(['one', 'two', three', 'four', 'five', 'six']) == 'three'
```

14. Define the function `shortest_and_longest` that returns the the tuple of shortest and longest strings from a sequence of strings. If two strings have the same length, then only the first one should be considered. 

```python
assert shortest_and_longest(['one', 'two', three', 'four', 'five', 'six']) == ('one', 'three')
```
