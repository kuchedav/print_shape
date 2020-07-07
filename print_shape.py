from sty import fg, bg, ef, rs, Style, RgbFg

def print_shape(elem1,level=0):
    if isinstance(elem1, str) or isinstance(elem1, int) or isinstance(elem1, float):
        print_level_type(elem1,level)
    elif "pandas" in str(type(elem1)):
        print_level_type(elem1,level)
    elif(isinstance(elem1,list)):
        print_level_type(elem1,level)
        [print_shape(i,level+1) for i in elem1]
    elif(isinstance(elem1,dict)):
        print_level_type(elem1,level)
        elem1_in = list(elem1.values())
        [print_shape(i) for i in elem1_in]

def print_level_type(input_elem,level):
    # get shape
    shape_out = ""
    if isinstance(input_elem,list) or isinstance(input_elem,dict):
        shape_out = str(len(input_elem))
    elif "pandas" in str(type(input_elem)):
        shape_out = str(input_elem.shape)
    
    # create indentation
    level_indent = ""
    if level > 0:
        level_indent = "| " * level
    level_indent = level_indent + "|___"
    type_string = str(type(input_elem)).split("'")[1]

    # create color
    level_1_counter = 0
    RGB = [(200,100,0),(0,200,100),(0,150,200),(200,200,0),(0,200,200),(200,0,200)]
    fg.orange = Style(RgbFg(*RGB[level % len(RGB)]))
    print_color = f"{fg.orange}{level_indent}{level}[{type_string}]{shape_out}{fg.rs}"
    level_1_counter += 1
    
    print(print_color)

if __name__=="__main__":
    import pandas as pd
    import numpy as np
    df2 = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),columns=['a', 'b', 'c'])

    test1 = [{"a":1,"b":2}, 10, [1,2,[4,5,6,[1,2,3,["string","test",[1,[1,[1]]]]]]], df2]
    
    out = print_shape(test1)
    print(out)