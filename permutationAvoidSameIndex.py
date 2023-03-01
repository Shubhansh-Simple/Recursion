'''
Generate all permutations of given pair except
those permutation whose number's index are same as given pair

for eg - INPUT [1,2,3] -> OUTPUT [2,1,3],[3,1,2]

BRUTE FORCE
Collect all permutations O(N!) as answer then check in answer's 
each pair whose number index are same as given pair O(N^2)

OPTIMIZED APPROACH
Don't even START also STOPS IMMEDIATELY those permutations
whose any number's index are same as given pair indexes

This way we don't even START generating such permutation 
or we can stop at MIDDLE
or at worst stop at the LAST
'''

def permutation1( arr, answer, index, record={}, permu=[] ):
    '''Extra data-structure approach'''

    # BASE CASE
    if len(permu) == len(arr):
        print( permu )
        return

    for i in range( len(arr) ):

        # If not taken already
        if not record.get(i):
            permu.append( arr[i] )   # new-element always at last of list
            record[i] = 1

            #If taken ele in permu,having same index in given array as in permu
            if len(permu)-1 != index[ arr[i] ]:
                permutation1( arr, answer, index, record, permu ) # recursion

            # RESET FOR NEXT
            permu.pop()
            record[i] = 0


def permutation2( arr, answer2, index, permu=[] ):
    '''Swapping Approach 
       ( since no need to maintain order ) 
       ( in this question )
    '''
    pass


# INPUTS
arr   = [ x for x in range(1,4) ]
index = {}         # for collecting indexes

# Binding indexes to their values
index = { arr[i] : i for i in range(len(arr)) }


answer1 = []                # act as a &pointer by default
permutation1( arr, answer1, index )

answer2 = []                # act as a &pointer by default 
permutation2( arr, answer2, index )




