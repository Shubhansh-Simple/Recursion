'''
Create permutation of given pair using swapping approach

Advantage - Only auxiliary space not extra space
DRAWBACK  - Generated permutations are not in lexicographically order
'''

def permutation( arr, length, ans, index=0 ):
    '''Generate permutation using swapping approach'''

    # Base Case
    if index == length:
        ans.append( arr[:] )
        #print('Permu - ',arr)
        return

    for i in range( index, index+1 ):
        for j in range( i , length ):
            if i != j:
                arr[i], arr[j] = arr[j], arr[i]   # swap

            # Only those permutation whose starting with 4
            if arr[0] == 4:
                permutation( arr, length, ans, index+1 )   # recursion

            # RESET
            if i != j:
                #print('Before - ',arr)
                arr[i], arr[j] = arr[j], arr[i]   # swap
                #print('Reset - ',arr)


arr = [1,2,3,4]
# Initialize outside of function to 
# persist the value in it even functions ends
ans = []           # Passing the pointer
'''
If we initialize ans as default argument in function
we can't access it's value after functions ends
'''
permutation( arr, len(arr), ans )


[ print(x) for x in ans ]
print('After sorting')
ans.sort()         # Sort it to lexicographically order
[ print(x) for x in ans ]




