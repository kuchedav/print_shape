# for_long

## Description
for_long facilitates iterating over long running loops.

following functionalities are implemented:
- save progress in folder
- start from last saved progress
- run over combination of input lists
- get show loading bar

## Installation

Run the following to install:
```
pip install forlong
```

## Attributes
iter_fun:       function to iterate over
iter_attr:      a dictionary of all attributes needed for iter_fun input.
                => {"attribute name 1":attribute_values1, "attribute name 2":attribute_values2, ...}
                for the loop to create a permutation you can enter one or more attributes as a list.
                => {"attribute name 1":[1,2,3,4], "attribute name 2":["EU","CH","AM"], ...}
                attributes with lists can be combined with attributes with a single value.
save_every_n:   save my progress every n iterations
path:           save my files under this path

## Usage
```

```