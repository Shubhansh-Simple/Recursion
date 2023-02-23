'''
Theory - Find kth permutation of given pair
         ( Note : Permutations are in lexicographical order )

[ BRUTE FORCE Approach ]
Collect each and every permutation of given pair in a list data-structure
then return retrieve (k-1)th element as answer

Drawbacks - .) Unnecessarily collect all permutations. ( SPACE )
            .) Unnecessarily goes finding rest permutations after finding answer ( TIME )

[ OPTIMIZED APPROACH ]
Return answer immediately finding it 

ADVANTAGES- .) Carry only single pair till finding answer sequentially( SPACE )
            .) Immediately return the answer which breaks unnecessary calls ( TIME )

APPROACH - We are using class's variable for maintaining the record
           through entire recursion calls
'''

# Class variable - It's shares through entire instance of the class 
#                  ClassName.classVariable += 1 if increment like this

class Solution:
    '''Using class variable for maintaining the record'''

    numbering = 0           # Class variable 

    def permutation( self, arr, record, k, answer=[] ):
        '''Return kth permutation of given pair'''

        # Base Case
        if len(answer) == len(arr):                
            print( answer )
            self.numbering += 1

            # Got the answer
            if self.numbering == k:
                return answer

            return                        # in order to break early


        for i in range( len(arr) ):

            if not record[i]:
                answer.append( arr[i] )   # digit added as permutation
                record[i] = 1             # digit is taken

                # Condition based returning
                if self.permutation( arr, record, k, ):
                    return answer

                # Reset On Moving Backward
                record[i] = 0
                answer.pop()

arr = [ x for x in range(1,5) ]
k   = 7                           # find 7th permutation of given pair
s = Solution()
print( 'Answer - ',s.permutation( arr, [0]*len(arr), k ) )      
print('Value of numbering from s - ', s.numbering)


