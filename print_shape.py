from sty import fg, Style, RgbFg
import numpy as np
import pandas as pd

def print_shape(elem1, print_elements = False, level = 0):
    if isinstance(elem1, (str,int,float,bool,complex)):
        if print_elements: print_level_type(elem1,level)
        else: return
    elif isinstance(elem1,(pd.core.frame.DataFrame,pd.core.series.Series)):
        print_level_type(elem1,level)
        if isinstance(elem1,pd.core.frame.DataFrame):
            if print_elements: [print_level_type(i,level+1,pandas_dtype=j) for i,j in zip(elem1.columns,elem1.dtypes)]
    elif isinstance(elem1,(list,tuple,range,set)):
        print_level_type(elem1,level)
        [print_shape(i,print_elements,level+1) for i in elem1]
    elif isinstance(elem1,dict):
        print_level_type(elem1,level)
        elem1_in = list(elem1.values())
        [print_shape(i,print_elements,level+1) for i in elem1_in]
    elif isinstance(elem1,np.ndarray):
        print_level_type(elem1,level)
    
def get_shape(input_elem):
    if isinstance(input_elem,(list,dict,tuple,set,range)):
        return str(len(input_elem))
    elif isinstance(input_elem,(pd.core.frame.DataFrame,pd.core.series.Series,np.ndarray)):
        return str(input_elem.shape)
    else:
        return ""

def print_level_type(input_elem,level,pandas_dtype = None):
    # get shape
    shape_out = get_shape(input_elem)
    
    # create indentation
    level_indent = ""
    if level > 0:
        level_indent = "| " * level
    level_indent = level_indent + "|___"
    type_string = str(type(input_elem)).split("'")[1]

    # create color
    level_1_counter = 0
    RGB = [(200,50,0),(0,180,100),(0,150,200),(200,200,0),(0,200,200),(150,100,200)]
    fg.orange = Style(RgbFg(*RGB[level % len(RGB)]))

    # if pandas columns are given
    if pandas_dtype:
        level = ""
        level_indent += "__"
        type_string = f"{input_elem} - {pandas_dtype}"

    # create print statement
    print_color = f"{fg.orange}{level_indent}{level}[{type_string}]{shape_out}{fg.rs}"
    level_1_counter += 1
    
    print(print_color)

if __name__=="__main__":
    import pandas as pd
    import numpy as np
    
    # pandas data
    df2 = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),columns=['a', 'b', 'c'])
    data = np.array(['a','b','c','d'])
    s = pd.Series(data)

    # numpy data
    np_array = np.array([[1, 2], [3, 4]])

    # complex numbers
    complex_n = 2+3j
    # boolean
    boolean_var = True
    # tuple
    tuple_var = (1,2,3,4)
    # set
    set_var = set((1,2,4,5,624,4357,3457,537))
    # range
    range_var = range(0,5)

    test1 = [{"a":1,"b":2}, 10, [1,2,[4,5,6,[1,2,3,["string","test",[1,[1,[1]]]]]]], df2, [s], np_array, complex_n, boolean_var, tuple_var, set_var, range_var]
    
    out = print_shape(test1, print_elements = False)
    print(out)