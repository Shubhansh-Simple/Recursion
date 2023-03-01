'''
Print all the permutations of the given pairs
using an EXTRA DATA-STRUCTURE for storing taken/Non-taken
of the element
'''

#Without passing pre-defined record
def permutation1( arr, record={}, matrix=[] ):
    '''Permutation through maintaining record in DICTIONARY'''

    # Base Case
    if len(matrix) == len(arr):
        print( matrix )
        return                               # For immediately breaking before entering in loop

    for i in range( len(arr) ):

        # If that number is not taken
        if not record.get(i):                   # .get() returns None on key doesn't exist

            record[i] = 1                       # Now the number is taken
            matrix.append(arr[i])               # Add it to permutation
            permutation1( arr, record, matrix ) # Recursion

            # Recursion's BackTracking 
            record[i] = 0                    # Resetting while moving backward
            matrix.pop()                     # Removing


#Passing pre-defined record
def permutation2( arr, record, matrix=[] ):
    '''Permutation through maintaining the record in LIST'''

    # Base Case
    # Without 'return',function runs the for loop uselessly
    if len(matrix) == len(arr):
        print( matrix )
        return          # For immediately breaking before entering in loop

    for i in range( len(arr) ):

        # If that number is not taken
        if not record[i]:

            record[i] = 1                     # Now the number is taken
            matrix.append(arr[i])             # Add it to permutation
            permutation2( arr, record, matrix)# Recursion

            # Recursion's BackTracking 
            record[i] = 0                    # Resetting while moving backward
            matrix.pop()                     # Removing


'''
Alternate way with try-catch/len(arr) to check index
'''
#Without passing pre-defined record
def permutation3( arr, record=[], matrix=[] ):
    '''Using try-catch block to avoid pre-defined record'''

    # Base Case
    if len(matrix) == len(arr):
        print( matrix )
        return          # For immediately breaking before entering in loop

    for i in range(len(arr)):

        # Make record making on it's own
        try:
            record[i]
        except IndexError:
            record.append(0)

        # If that number is not taken
        if not record[i]:

            record[i] = 1                    # Now the number is taken
            matrix.append(arr[i])            # Add it to permutation
            permutation3( arr, record, matrix )

            # Recursion's BackTracking 
            record[i] = 0                    # Resetting while moving backward
            matrix.pop()                     # Removing


arr = [ x for x in range(1,4) ]
permutation1( arr )                # Using DICTIONARY->no need to pass record's value
#permutation2( arr, [0]*len(arr) )
#permutation3( arr )               # Using try-catch ->no need to pass record's value
