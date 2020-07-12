# print_structure

## Description
Print structure of any arbitrary python object.

## Installation

Run the following to install:
```
pip install print_structure
```

## Attributes
object : any type of python object

## print out
Structure of object.

Example:

|___0 [list] (14)
  |___1 [dict] (2)
  |___1 [list] (3)
  |___1 [pandas.core.frame.DataFrame] (3, 3)
  |___1 [list] (1)
    |___2 [pandas.core.series.Series] (4,)
  |___1 [numpy.ndarray] (2, 2)

## Usage
```
from print_structure import str

list = [1,2,3,["a","b","c"]]
str(object = list)
```
