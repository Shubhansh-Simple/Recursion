'''
Theory - Find kth permutation of given pair
         ( Note : Permutations are in lexicographical order )

[ BRUTE FORCE Approach ]
Collect each and every permutation of given pair in a list data-structure
then return by retrieving (k-1)th element as answer ( Index starts with 0 )

Drawbacks - .) Unnecessarily collect all permutations. ( SPACE )
            .) Unnecessarily goes finding rest permutations after answer ( TIME )

--------------------------------------------------
[ OPTIMIZED APPROACH ]
    Return answer immediately and breaks recursion through "return" statement

ADVANTAGES- .) Store single element ( in list ) replace it till finding answer ( SPACE )
            .) Immediately return the answer which breaks rest of recursion ( TIME )

--------------------------------------------------
[ MORE OPTIMIZED APPROACH ]
    Make only those permutations whose starting point containing the answer's starting point
    We can find out what is the starting point of Kth Permutation through formula


APPROACH - We are using class's variable for maintaining the record
           through entire recursion calls
'''

# Class variable - It's shares through entire instance of the class 
#                  ClassName.classVariable += 1 if increment like this

class Solution:
    '''Using class variable for maintaining the record across recursion'''

    numbering = 0           # Class variable 


    def mathematics( self, length, k, factorial ):
        '''Find starting number of the Kth permutation through below formula'''

        # Possible pairs
        totalPairs = factorial//length  # (N!//N) starts with each number
        # For Eg.- All Permutations starts with 1,2 or 3 is totalPairs

        # Finding starting number of Kth permutation by dividing
        remainder = k  % totalPairs
        quotient  = k // totalPairs

        if remainder == 0:
            targetIndex = quotient-1   # index starts with 0
            k           = totalPairs   # last element
        else:
            targetIndex = quotient     # index starts with 0
            k           = remainder    # numbering starts with 1
        
        return targetIndex,k           # returned updated k also


    def permutation( self, arr, record, targetIndex, k, answer=[],  ):
        '''
        Make only those permutatoins that starts with arr[ targetIndex ]
        '''

        # Base Case
        if len(answer) == len(arr):
            self.numbering += 1

            # we find what we searching for
            if self.numbering == k:
                return answer            # For boolean it's True
 
            return                       # For boolean it's False

        for i in range( len(arr) ):

            # if it's not taken already
            if not record[i]:

                answer.append( arr[i] )
                record[i] = 1

                # Make only those permutation whose starts with arr[ targetIndex ]
                if answer[0] == arr[ targetIndex ]:
                    if self.permutation( arr, record, targetIndex, k, answer ):
                        return answer             # EXIT POINT

                # RESET                           # Code Not Reached
                answer.pop()                      # if above return
                record[i] = 0                     # executed
    

    def solve( self, arr, k ):

        # Find no.of total permutations of given pair through Factorial
        factorial = 1
        for i in range( len(arr), 1,-1):
            factorial *= i
        
        # Special Case
        if factorial == k: return arr[::-1]

        targetIndex, k = self.mathematics( len(arr), k, factorial )
        record         = [0] * len(arr)

        return self.permutation( arr, record, targetIndex, k )
        

arr = [ x for x in range(1,5) ]
k   = 14                            # K <= len(arr)!  factorial
s = Solution()
print( s.solve( arr, k) )            

