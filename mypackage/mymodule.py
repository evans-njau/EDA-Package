def top_n(items, n ):
    """
    Returns the top n elements in an array of items

    args:
        items(array): an array or a list of items
        n(int): number of items to return

    Return:
        array: top n items, in desc order 
        >>>> top_n([1,7,8,9,0,6], 3)
        [9,8,7]   
    """

    for i in range(n):
        for j in range(len(items)-1-i):
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]
    top_n = items[-n:]    
    return top_n[::-1]        
