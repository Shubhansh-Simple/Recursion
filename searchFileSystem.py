'''
Search in filesystem of computer
through recursion based algorithm.

What's New - Breaking the recursion flow if got the answer
'''

import os

def searchFile( search, filepath=os.getcwd() ):
    
    print(filepath)

    # if it's an folder ( Base Case )
    if filepath.split('/')[-1] == search:
        return True


    for each in os.listdir( filepath ):

        fullPath = filepath + '/' + each  #creating full filepath

        # If it's a directory
        if os.path.isdir( fullPath ):

            # Condition based recursion breaking/returning
            if searchFile( search, fullPath ):     # RECURSION
                return True                        # Got the answer

        # If it's a file
        else:
            if not each.startswith('.'):
                print( each )

                if each == search:
                    return True                 # Got the answer

print( searchFile('Yup','/home/shubhansh/Desktop') )


