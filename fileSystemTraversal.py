'''
File Traversal Algorithm based on recursion

Check if it's an directory if it is then call the func. again
and let the current folder execution wait for their time
( Since recursion will come back soon BACKTRACKING )

else just print the file name

'''

import os

def traversal( filepath=os.getcwd() ): 
    '''
    Using absolute file path to check weather it's dir or not
    '''


    print( 'DIRECTORY - ',filepath.split('/')[-1], end='\n\n' )

    # Directory is empty   ( Base Case )
    if not os.listdir(filepath):
        return

    for each in os.listdir(filepath):
        newPath = filepath + '/' + each    #creating full filepath

        # If it's an directory
        if os.path.isdir( newPath ):
            traversal( newPath )           #sending full filepath

        # If it's an file
        else:
            if not each.startswith('.'):
                print( each )


traversal()      # by default is current working directory
