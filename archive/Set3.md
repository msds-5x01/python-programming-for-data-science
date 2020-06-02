# Homework Set 3

Good news! Michael Driscoll's Python 101 is available online: https://python101.pythonlibrary.org/


## The Standard Library
Learn about the Python standard library, i.e. the collection of modules that are distributed with Python: https://docs.python.org/3/library/

For example, review the documentation for modules `math`, `statistics`, `random`, `csv`, `json`, and `datetime`. What functionality do they provide? 

Select two modules from the standard library that seem useful to you. In class, describe why you found them useful.

In addition to the standard library, over a hundred thousand other packages can be installed from the [Python Package Index](pypi.org) using the [`pip` utility](https://packaging.python.org/tutorials/installing-packages/).

## US Cities
A nice person on the web published a list of 1000 US cities in the JSON format: https://gist.githubusercontent.com/Miserlou/c5cd8364bf9b2420bb29/raw/2bf258763cdddd704f8ffd3ea9a3e81d25e2c6f6/cities.json

Use the `url.requests` module to download the file and save it as `us-cities.json`.


```python
import urllib.request
url = 'https://gist.githubusercontent.com/Miserlou/c5cd8364bf9b2420bb29/raw/2bf258763cdddd704f8ffd3ea9a3e81d25e2c6f6/cities.json'
filename = 'us-cities.json'

urllib.request.urlretrieve(url, filename)
```




    ('us-cities.json', <http.client.HTTPMessage at 0x7fa75460edd8>)



Use the `ls` shell utility to verify that the file has downloaded


```python
ls -l *json 
```

    -rw-r--r-- 1 dimitri dimitri 244212 Sep 25 10:20 us-cities.json


You may now use the [`json` module](https://docs.python.org/3/library/json.html) to read the list as a `list` of `dict`s


```python
import json

filename = 'us-cities.json'
with open(filename) as f:
    cities = json.load(f)
```

The cities are ordered by their population. Let's look at the four biggest cities.


```python
cities[:4]
```




    [{'city': 'New York',
      'growth_from_2000_to_2013': '4.8%',
      'latitude': 40.7127837,
      'longitude': -74.0059413,
      'population': '8405837',
      'rank': '1',
      'state': 'New York'},
     {'city': 'Los Angeles',
      'growth_from_2000_to_2013': '4.8%',
      'latitude': 34.0522342,
      'longitude': -118.2436849,
      'population': '3884307',
      'rank': '2',
      'state': 'California'},
     {'city': 'Chicago',
      'growth_from_2000_to_2013': '-6.1%',
      'latitude': 41.8781136,
      'longitude': -87.6297982,
      'population': '2718782',
      'rank': '3',
      'state': 'Illinois'},
     {'city': 'Houston',
      'growth_from_2000_to_2013': '11.0%',
      'latitude': 29.7604267,
      'longitude': -95.3698028,
      'population': '2195914',
      'rank': '4',
      'state': 'Texas'}]



Here are the last four cities:


```python
cities[-4:]
```




    [{'city': 'Keizer',
      'growth_from_2000_to_2013': '14.4%',
      'latitude': 44.9901194,
      'longitude': -123.0262077,
      'population': '37064',
      'rank': '997',
      'state': 'Oregon'},
     {'city': 'Spanish Fork',
      'growth_from_2000_to_2013': '78.1%',
      'latitude': 40.114955,
      'longitude': -111.654923,
      'population': '36956',
      'rank': '998',
      'state': 'Utah'},
     {'city': 'Beloit',
      'growth_from_2000_to_2013': '2.9%',
      'latitude': 42.5083482,
      'longitude': -89.03177649999999,
      'population': '36888',
      'rank': '999',
      'state': 'Wisconsin'},
     {'city': 'Panama City',
      'growth_from_2000_to_2013': '0.1%',
      'latitude': 30.1588129,
      'longitude': -85.6602058,
      'population': '36877',
      'rank': '1000',
      'state': 'Florida'}]



Or use the [`random` module](https://docs.python.org/3/library/random.html) to pick a city at random:


```python
import random
help(random.choices)
```

    Help on method choices in module random:
    
    choices(population, weights=None, *, cum_weights=None, k=1) method of random.Random instance
        Return a k sized list of population elements chosen with replacement.
        
        If the relative weights or cumulative weights are not specified,
        the selections are made with equal probability.
    



```python
random.choices(cities, k=4)
```




    [{'city': 'Berwyn',
      'growth_from_2000_to_2013': '5.1%',
      'latitude': 41.85058739999999,
      'longitude': -87.7936685,
      'population': '56758',
      'rank': '638',
      'state': 'Illinois'},
     {'city': 'Owensboro',
      'growth_from_2000_to_2013': '7.7%',
      'latitude': 37.7719074,
      'longitude': -87.1111676,
      'population': '58416',
      'rank': '617',
      'state': 'Kentucky'},
     {'city': 'Niagara Falls',
      'growth_from_2000_to_2013': '-10.8%',
      'latitude': 43.0962143,
      'longitude': -79.0377388,
      'population': '49468',
      'rank': '754',
      'state': 'New York'},
     {'city': 'Prescott',
      'growth_from_2000_to_2013': '18.1%',
      'latitude': 34.5400242,
      'longitude': -112.4685025,
      'population': '40590',
      'rank': '907',
      'state': 'Arizona'}]



Or select four cities with probability proportional to their populations. This is equivalent to picking a random person and asking what city they live in.


```python
city_populations = [int(city['population']) for city in cities]
random.choices(cities, k=4, weights=city_populations)
```




    [{'city': 'Fort Wayne',
      'growth_from_2000_to_2013': '1.0%',
      'latitude': 41.079273,
      'longitude': -85.1393513,
      'population': '256496',
      'rank': '76',
      'state': 'Indiana'},
     {'city': 'Charlotte',
      'growth_from_2000_to_2013': '39.1%',
      'latitude': 35.2270869,
      'longitude': -80.8431267,
      'population': '792862',
      'rank': '16',
      'state': 'North Carolina'},
     {'city': 'Orlando',
      'growth_from_2000_to_2013': '31.2%',
      'latitude': 28.5383355,
      'longitude': -81.3792365,
      'population': '255483',
      'rank': '77',
      'state': 'Florida'},
     {'city': 'San Bernardino',
      'growth_from_2000_to_2013': '13.0%',
      'latitude': 34.1083449,
      'longitude': -117.2897652,
      'population': '213708',
      'rank': '100',
      'state': 'California'}]



`cities` has the growth rate as a string. You can convert it to a number using the `float` constructor but first you need to strip the `%`:


```python
float(cities[3]['growth_from_2000_to_2013'].rstrip('%'))
```




    11.0



Here is a function to compute distances between cities:


```python
import math
def route_length(cities): 
    """
    distance of a route between any number of cities in kilometers
    :param cities: list of dicts with fields 'city', 'state', 'longitude', 'latitude' 
    :return: length of the route connecting the cities
    """
    earth_radius = 6371
    assert len(cities) >=2, 'at least two cities are requied'
    
    city1 = cities[0]
    total = 0.0
    for city2 in cities[1:]:
        x1, y1 = math.radians(city1['longitude']), math.radians(city1['latitude'])
        x2, y2 = math.radians(city2['longitude']), math.radians(city2['latitude'])
        total += math.asin(math.sqrt(
            math.sin((x2 - x1) / 2)**2 + 
            math.cos(y1) * math.cos(y2) * math.sin((y2 - y1) / 2)**2))
        city1 = city2
    return total * 2 * earth_radius
```


```python
route = [cities[i] for i in (3, 7, 11, 13, 17, 3)]

print("Route:")
for point, city in enumerate(route):
    print("  {point}: {city}, {state}".format(point=point, **city))

distance = route_length(route)
print(f"Total distance: {distance:.0f} km")

```

    Route:
      0: Houston, Texas
      1: San Diego, California
      2: Indianapolis, Indiana
      3: San Francisco, California
      4: Detroit, Michigan
      5: Houston, Texas
    Total distance: 16152 km


### English words
Another nice person posted the list of some 60,000 common English words: http://www.mieliestronk.com/corncob_lowercase.txt


```python
url = "http://www.mieliestronk.com/corncob_lowercase.txt"
filename = 'english-words.txt'
urllib.request.urlretrieve(url, filename)
```




    ('english-words.txt', <http.client.HTTPMessage at 0x7fa74d57b898>)



This is a simple txt file. You can just use the builtin Python methods to read it in.


```python
with open('english-words.txt') as f:
    words = f.read().splitlines()
```


```python
# pick a random word
random.choice(words)
```




    'foretell'



Here are some examples of word searches:


```python
# words that end in a a given ending
ending = 'teer'
for word in words:
    if word.endswith(ending):
        print(word)
```

    charioteer
    gazetteer
    marketeer
    musketeer
    pamphleteer
    privateer
    puppeteer
    steer
    volunteer



```python
# words that contain a specific substring
substring = 'niss'
for word in words:
    if substring in word:
        print(word)
```

    pianissimo
    unissued


## Comprehensions
Learn about comprehensions about Python
https://python101.pythonlibrary.org/chapter6_comprehensions.html

List comprehensions make it convenient to create a list out of some sequence using loops.

Without a list comprehension, one first creates an empty list and then adds elements to it inside the loop. For example


```python
def find_sorted_words(words, min_length=5, reverse=False):
    """
    :param words: list of words
    :min_length: only consider words of this length or longer
    :return: list of words whose letters are in reverse alphabetical order
    """    
    sorted_words = []
    for word in words:
        if len(word) >= min_length and list(word) == sorted(word, reverse=reverse):
            sorted_words.append(word)
    return sorted_words
```


```python
find_sorted_words(words, min_length=7)
```




    ['billowy']




```python
find_sorted_words(words, min_length=7, reverse=True)
```




    ['sniffed', 'sponged', 'spooked', 'spooled', 'spooned', 'wronged']



The same function can be implemented with a list comprehension:


```python
def find_sorted_words(words, min_length=5, reverse=False):
    """
    :param words: list of words
    :min_length: only consider words of this length or longer
    :return: list of words whose letters are in reverse alphabetical order
    """    
    return [word for word in words 
            if len(word) >= min_length and list(word) == sorted(word, reverse=reverse)]
```

Here is another function that makes a word list:


```python
def find_unique_letter_words(words, min_length=8):
    """
    :param words: list of words
    :min_length: only consider words of this length or longer
    :return: list of words whose letters are unique
    """    
    result = []
    for word in words:
        if min_length <= len(word) == len(set(word)): 
            result.append(word)
    return(result)
```


```python
find_unique_letter_words(words, 13)
```




    ['copyrightable', 'hydromagnetic', 'unpredictably', 'unproblematic']




```python
# words that start and end with the same four letters
[w for w in words if len(w)>=5 and w[:4] == w[-4:]]
```




    ['agaragar',
     'alfalfa',
     'couscous',
     'entente',
     'hushhush',
     'khoikhoi',
     'suchandsuch',
     'walltowall']




```python
# Cities that have their state in their name
["{city}, {state}".format(**c) for c in cities if c['state'] in c['city']]
```




    ['New York, New York',
     'Indianapolis, Indiana',
     'Oklahoma City, Oklahoma',
     'Virginia Beach, Virginia',
     'Colorado Springs, Colorado',
     'Kansas City, Kansas',
     'Iowa City, Iowa',
     'Idaho Falls, Idaho',
     'Texas City, Texas']




```python
# You can also do set comprehensions
states = set(c['state'] for c in cities)
states
```




    {'Alabama',
     'Alaska',
     'Arizona',
     'Arkansas',
     'California',
     'Colorado',
     'Connecticut',
     'Delaware',
     'District of Columbia',
     'Florida',
     'Georgia',
     'Hawaii',
     'Idaho',
     'Illinois',
     'Indiana',
     'Iowa',
     'Kansas',
     'Kentucky',
     'Louisiana',
     'Maine',
     'Maryland',
     'Massachusetts',
     'Michigan',
     'Minnesota',
     'Mississippi',
     'Missouri',
     'Montana',
     'Nebraska',
     'Nevada',
     'New Hampshire',
     'New Jersey',
     'New Mexico',
     'New York',
     'North Carolina',
     'North Dakota',
     'Ohio',
     'Oklahoma',
     'Oregon',
     'Pennsylvania',
     'Rhode Island',
     'South Carolina',
     'South Dakota',
     'Tennessee',
     'Texas',
     'Utah',
     'Vermont',
     'Virginia',
     'Washington',
     'West Virginia',
     'Wisconsin',
     'Wyoming'}



As a more complex example, here is a list comprehension with nested `for` loops


```python
# Cities whose names contain a state name other than its own
["{city}, {state}".format(**c) 
 for state in states 
 for c in cities 
 if state in c['city'] and state != c['state']]
```




    ['Missouri City, Texas',
     'Wyoming, Michigan',
     'West New York, New Jersey',
     'Washington, District of Columbia',
     'Kansas City, Missouri']



## Monte Carlo methods

Monte Carlo methods are calculations based on probabilistic computations. 

For example, to estimate the number $\pi$, we could generate random points with coordinates $(x, y)$ from the unifirm distribution in the interval $[-1, 1]$. This interval makes a square with area $S_0=4$. Now if we count what fraction of numbers fall within the distance $r = 1.0$ of the origin, we will effectivly estimate the area of the circle, which should be $S_1 = \pi r^2$. 

$$\pi = 4\frac{S_1}{S_0}\approx 4\frac{\text{number of points inside the circle}}{\text{total number of points}}$$

For more detail, here is a variation of this description: https://www.geeksforgeeks.org/estimating-value-pi-using-monte-carlo/


```python
import random
def estimate_pi(npoints=100_000):
    """etimate pi by throwing darts at a square"""
    counts = 0
    x = random.uniform(-1, 1)
    for i in range(npoints):
        y = x
        x = random.uniform(-1, 1)
        counts += (x * x + y * y < 1.0)
    return 4*counts/npoints
    
```


```python
estimate_pi(1_000_000)
```




    3.142608



Now implement the same thing as a comprehension in the sum function:


```python
import random
def estimate_pi(npoints=100_000):
    """etimate pi by throwing darts at a square"""
    return 4 * sum(random.uniform(-1, 1)**2 + random.uniform(-1, 1)**2 < 1.0 
                   for _ in range(npoints))/npoints
```

### More on sorting
The Python functions `sort`, `max`, and `min` accept the argument `key`. It must point to a function that is applied to every element, returning a number. That number is then used for sorting.

This `key` can be a function that you define.


```python
help(max)
```

    Help on built-in function max in module builtins:
    
    max(...)
        max(iterable, *[, default=obj, key=func]) -> value
        max(arg1, arg2, *args, *[, key=func]) -> value
        
        With a single iterable argument, return its biggest item. The
        default keyword-only argument specifies an object to return if
        the provided iterable is empty.
        With two or more arguments, return the largest argument.
    



```python
def count_vowels(word):
    return sum(word.count(c) for c in "aeuioy")

# word with most vowels
max(words, key=count_vowels)
```




    'counterrevolutionaries'




```python
def latitude(city):
    return city['latitude']

#southern-most city
min(cities, key=latitude)
```




    {'city': 'Honolulu',
     'growth_from_2000_to_2013': '-6.2%',
     'latitude': 21.3069444,
     'longitude': -157.8583333,
     'population': '347884',
     'rank': '54',
     'state': 'Hawaii'}




```python
def growth_rate(city):
    """
    :return: city relative growth rate, zero if missing
    """
    return float(city['growth_from_2000_to_2013'].rstrip('%') + '0')

# fastest-growing city (relative)
max(cities, key=growth_rate)
```




    {'city': 'Maricopa',
     'growth_from_2000_to_2013': '2503.4%',
     'latitude': 33.0581063,
     'longitude': -112.0476423,
     'population': '45508',
     'rank': '817',
     'state': 'Arizona'}




```python
def abs_growth_rate(city):
    """
    :return: city relative growth rate, zero if missing
    """
    return float(city['growth_from_2000_to_2013'].rstrip('%') + '0') * float(city['population'])

# top 3 fastest-growing cities (absolute)
sorted(cities, key=growth_rate, reverse=True)[:3]
```




    [{'city': 'Maricopa',
      'growth_from_2000_to_2013': '2503.4%',
      'latitude': 33.0581063,
      'longitude': -112.0476423,
      'population': '45508',
      'rank': '817',
      'state': 'Arizona'},
     {'city': 'Buckeye',
      'growth_from_2000_to_2013': '480.9%',
      'latitude': 33.3703197,
      'longitude': -112.5837766,
      'population': '56683',
      'rank': '641',
      'state': 'Arizona'},
     {'city': 'Frisco',
      'growth_from_2000_to_2013': '287.7%',
      'latitude': 33.1506744,
      'longitude': -96.82361159999999,
      'population': '136791',
      'rank': '186',
      'state': 'Texas'}]



# Problems 
The following problems may use the `cities` and `words` lists defined above. Use them as needed.

Assume that `cities` represent the entire US population, ignoring smaller cities. 

### Problem 1. Find all common English words that contain "zz", e.g. "pizza" 

### Problem 2: Find all common English words that have at least three Ys anywhere in the word, e.g. "synonymously".
**Hint:** Use the string `.count` method, e.g. `"sympathy".count("y")` will yield 2. Use the `words` lists defined above.

### Problem 3: Find the longest english word
Show your Python code

### Problem 4: Find the longest word whose only vowels are "a".
For example, the longest word with no vowels other than "e" is "defenselessness".




### Problem 5. Using our word list, confirm the spelling rule: "I before E except after C"
1. Count the number of words that contain "cie", e.g. "society"
2. Count the number of words that contain "cei", e.g. "receive"

which spelling is more common?

### Problem 6. Make compound words
Define the function `make_compound_word` that takes `n` words at random and concatenates them with a hyphen. This can be used to generate random memorable passwords. 

**Hint:** use the `random.choices`.

```python
def make_compound_word(words, n=3):
    """
    :param words: a list of words
    :param n: number of words
    :return: hyphenated compound word
    ...
```

**Example:**
```
>> make_compoud_word(n=4)
'wobblier-bloodshed-deepness-handpicked'
```



### Problem 7:  State population

Define the function `state_population` that adds up all people in a given state

```python
def state_population(cities, state):
    """
    :param cities: list of cities as dicts
    :param state: the name of a state
    :return: the total number of people in cities from that state
    """
    ...
```

### Problem 9.  Compute the average distance between two cities in the US. 
**Hint:** You can use a Monte Carlo method to pick pairs of cities with the `random.sample` function and the `route_length` function above to compute the distance between them. Pull 100,000 random pairs and average the result. 

Since we only have 1000 cities, then you can also compare all pairs. For 1000 cities, this would make $1000\times999/2 = 499,500$ unordered pairs. The random sampling may be easier to implement and faster to compute with sufficient accuracy.

### Problem 10.  Compute the average distance between two random people in the US. 
**Hint:** Use the same algorithm as for cities, but use `random.choices` to select pairs of cities with weights proportional to the population size. 

Explain the difference between the results of 9 and 10.

### Problem 11. Compute the average population of a city in which a US person lives. 

**Hint**: This is different from the average city population. Weigh the average by the population.

### Problem 12.  Calculate what fraction of the US population lives east of Houston. 
**Hint:** No need for Monte Carlo, just sum.

### Problem 13. Traveling Salesperson Problem
Select 10 cities from the `cities`. You may pick them yoursef or use `random.choices` weighted by population (duplicate cities are okay). Calculate the distance of the route between the cities, returning to the starting city. In what order should a traveling salesperson visit them.

Define the function `optimize_route` that takes the list of cities to visit and returns an optimized sequences of visits for the shortest overall distance. 

**Hint:** You can use `random.shuffle` to generate 10,000 random shuffles and select the one that produces the shortest route. 

```python
def optimize_route(route, nshuffles=100_000):
    """
    :param route: a list of dictionaries with fields 'city', 'state', 'latitude', and 'longitude'
    :nshuffles: number of random shuffles to try in search of the shortest route
    :return: the shortest route
    ...
```

### Problem 14. Re-write the function `find_unique_letter_words` above but using a list comprehension instead.

Enjoy!
