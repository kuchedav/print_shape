# print_structure

## Description
Print structure of python object.
Most python object types are supported.
Please let me know if you would like some types added.

## Installation

Run the following to install:
```
pip install print_structure
```

## Attributes
object : any type of python object

## Output
There is no output for this function. It only prints the information in the terminal.

One line of print-out contains follwing information:
```
|___<level> [<obj_type>] (<obj_shape>)
```


## Usage

### small example
```python
from print_structure import print_str
test_obj = [1,2,3,["a","b",b"bytes",2+3j]]

print_str(object_atr = test_obj)
```
print-out
```python
|___0 [list] (4)
  |___1 [list] (4)
```
There is as well the possibility to look into every element by using "print_elements = True".
Careful with large object!
```python
print_str(object_atr = test_obj, print_elements = True)
```
print-out
```python
|___0 [list] (4)
  |___1 [int] 
  |___1 [int] 
  |___1 [int] 
  |___1 [list] (4)
    |___2 [str] 
    |___2 [str] 
    |___2 [bytes] 
    |___2 [complex] 
 ```


### large example

```python
from print_structure import print_str
import pandas as pd
import numpy as np

# pandas data
df2 = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),columns=['a', 'b', 'c'])
data = np.array(['a','b','c','d'])
s = pd.Series(data)

# numpy data
np_array = np.array([[1, 2], [3, 4]])

# dict
dict_varm = {"a":1,"b":2}
# complex numbers
complex_n = 2+3j
# boolean
boolean_var = True
# tuple
tuple_var = (1,3,4)
# set
set_var = set((1,2,4))
# range
range_var = range(0,3)

### bytes
simple_bytes_string = b"test_test"
string = "Pyth"
bytes_arr = bytearray(string, 'utf-8')
mem_var = memoryview(simple_bytes_string)

test_obj = [df2, [s], np_array, complex_n, boolean_var, tuple_var, set_var, range_var, \
            dict_varm, [simple_bytes_string, [bytes_arr, mem_var]]]

print_str(object_atr = test_obj)
```
print-out
```python
|___0 [list] (10)
  |___1 [pandas.core.frame.DataFrame] (3, 3)
  |___1 [list] (1)
    |___2 [pandas.core.series.Series] (4,)
  |___1 [numpy.ndarray] (2, 2)
  |___1 [tuple] (3)
  |___1 [set] (3)
  |___1 [range] (3)
  |___1 [dict] (2)
  |___1 [list] (2)
    |___2 [list] (2)
      |___3 [bytearray] (4)
```
