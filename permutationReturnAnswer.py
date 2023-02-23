'''
This code actually return the answer
without using class instance variable

Drawback it's takes extra loop for 
counting possible pairs permutation

'''

def permutation( arr, record, possiblePair, matrix=[], answer=[] ):

    # Base Case
    if len(matrix) == len(arr):

        # Collecting all permutations in answer list
        answer.append(matrix[:])
        #print( matrix )


        # When got all possible permutation N!
        if len(answer) == possiblePair:
            return True

        return

    for i in range( len(arr) ):

        if not record[i]:
            record[i] = 1
            matrix.append(arr[i])

            # Condition based returning
            if permutation( arr, record, possiblePair, matrix, answer ):
                return answer

            # Recursion's BackTracking 
            record[i] = 0
            matrix.pop()



#from math import prod
#possiblePair = prod( [ x for x in range(len(arr),1,-1) ] ) 

arr          = [1,2,3,4]
possiblePair = 1

# Possible permutation using formula i.e. N! ( factorial )
for i in range(len(arr),1,-1):   
    possiblePair *= i


print( 'Answer - ',permutation( arr, [0]*len(arr), possiblePair ) )


