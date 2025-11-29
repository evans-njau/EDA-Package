from mypackage import mymodule

def top_n():
    """
    make sure it works correctly
    """
    assert mymodule.top_n([8,1,2,4,7,9],2) == [9,8], 'incorrect'
    assert mymodule.top_n([18,10,20,4,7,9],3) == [20, 18, 10], 'incorrect'
    assert mymodule.top_n([8,1,2,4,7,9],3) == [9,8,7], 'incorrect'
