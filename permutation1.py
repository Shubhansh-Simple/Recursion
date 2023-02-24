'''
Print all the permutations of the given pairs
using an EXTRA DATA-STRUCTURE for storing taken/Non-taken
of the element
'''

def permutation( arr, record, matrix=[] ):
    '''Permutation through maintaining the record in DS'''

    # Base Case
    # Without 'return' function runs the for loop uselessly
    if len(matrix) == len(arr):
        print( matrix )
        return          # For immediately breaking

    for i in range( len(arr) ):

        # Since we don't want repeatition
        # If that number is not taken
        if not record[i]:

            record[i] = 1                    # Now the number is taken
            matrix.append(arr[i])            # Add it to permutation
            permutation( arr, record, matrix )

            # Recursion's BackTracking 
            record[i] = 0                    # Resetting while moving backward
            matrix.pop()                     # Removing


#arr = [ x for x in range(1,5) ]
arr = [ 1,1,2]
permutation( arr, [0]*len(arr) )


