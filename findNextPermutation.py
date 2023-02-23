'''
Theory - Find NEXT permutation of given permutation
         ( Note : Permutations are in lexicographical order )

[ BRUTE FORCE Approach ]
Collect each and every permutation of given pair in a list data-structure
then return retrieve the permutation next to given permutation

Drawbacks - .) Unnecessarily collect all permutations. ( SPACE )
            .) Unnecessarily goes finding rest permutations after answer ( TIME )

[ OPTIMIZED APPROACH ]
Only finding those permutations whose starting with given one's first digit
and the next digit
Return the answer immediately using return statement

ADVANTAGES- .) Saves N!-(N!/N) steps in order to get the answer ( TIME )

APPROACH - We are using class's variable for maintaining the record
           through entire recursion calls
'''

def permutation( arr, record, givenPair, index, answer=[], ready=[False] ):
    '''Find next permutation of given pair'''

    # Base Case
    if len(arr) == len(answer):
        print( 'Pass-',answer )           # print complete permutation pair

        if ready[0]:
            return answer

        # Next pair will be the answer
        if answer == givenPair:
            ready[0] = [True]

        return

    for i in range( len(arr) ):

        # Only if digit not taken already
        if not record[i]:
            answer.append( arr[i] )            # add it to permutation
            record[i] = 1                      # now digit taken

            # Make permutation of givenPair's first and next digit
            try:
                # Only make certain permutations
                if answer[0] == arr[index] or answer[0] == arr[index+1]:
                    if permutation( arr, record, givenPair, index, answer, ready ):
                        return answer
            except IndexError:
                pass

            # RESET
            answer.pop()
            record[i] = 0


def specialCase( givenPair ):
    '''When we get the last pair of permutation'''

    arr = sorted( givenPair )        # sorted version
    
    # Given pair is last permutation
    if arr[::-1] == givenPair:
        return arr                   # first permutation
    
    # Get index of givenPair's first digit from sorted arr
    index = None
    for i in range( len(arr) ):
        if arr[i] == givenPair[0]:
            index = i
            break

    return permutation( arr, [0]*len(arr), givenPair, index )

givenPair = [3,4,2,1]
print( 'Next permutation - ',specialCase( givenPair ) )

