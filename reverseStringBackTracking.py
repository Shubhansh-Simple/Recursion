def reverse( string, i=0 ):

    # Base Case
    if i == len(string):
        return ''
    
    # Backtracking approach
    return reverse(string,i+1) + string[i]


string = 'shubhansh'
print( reverse( string ) )


ans = ''.join( list(reversed(string)) )

print('Correct Answer - ',ans)

