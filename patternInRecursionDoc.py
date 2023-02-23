'''
Writting the patterns of recursion
handling till now.
'''

# RECURSION - COUNTING ELEMENT
def count( string, i=0 ):
    '''
    For counting anything using recursion
    we can use the following recursion pattern

    return 1 + function()
    '''

    # Base Case
    try:
        string[i]
    except IndexError:
        return 0

    return 1 + count( string, i+1 )


# RECURSION - BACKTRACKING
def reverse( string, i=0 ):
    '''
    Take the advantage of backtracking
    Recursion goes forward from start to end
    Recursion comes backward from end to start
    '''

    # Base Case
    if i == len(string):
        return ''
    
    # Backtracking approach
    return reverse(string,i+1) + string[i]

# RECURSION - BREAK THE RECURSION FLOW AT MIDDLE
def counting1( number=10 ):
    '''It will run till end'''

    # Base Case
    if number == 0:
        return            # 1st Return

    counting1( number-1 )

# LEFT TO CODE
def counting2( number=10 ):
    '''It will break at the middle'''

    # Base Case
    if number == 0:
        return            # 1st Return

    counting2( number-1 )



string = 'shubhansh'
print( reverse( string ) )

