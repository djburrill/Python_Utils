'''
pyLines.py

Author: Daniel Burrill
Date Created: November 6, 2013
Date Last Modified: November 6, 2013

v1.00
- Initial Build. pyBlocks does not handle blocks within blocks, yet.

Description:
 Grabs lines from a file based on input keywords. Returns the lines
 in an ordered array
 
'''

## Imports

## Variables

## Functions

# pyLines
def pyLines(keywords, inFileName):
    ''' 
    DESCRIPTION
        Grabs lines from a file based on input keywords. Returns the lines in
        an ordered array.
    
    INPUT
        Keywords: Array of keywords to look for. Separate keyword lists by
        including multiple arrays.
        
        inFile: Name of file to parse.
        
    OUTPUT
        outArray: Array of lines matching with keywords. Placed in order in
        which the lines were located. 
    '''
    # Variables
    outArray = []    
    
    # Open input file
    inFile = open(inFileName,'r')
    
    # Parse lines of input file
    for line in inFile:
        # Format line for easy checking
        lineCheck = line.strip()
        lineCheck = lineCheck.split()
        
        # Check against keywords
        for query in keywords:
            for index,word in enumerate(query):
                # If word is not in line then move on to next query
                if (word not in lineCheck):
                    break
                # If word is in line and it is the last in the query,
                # add to outArray
                elif (word in lineCheck) and (index == len(query)-1):
                    outArray.append(line)
                    
    return outArray
    
# pyBlocks
def pyBlocks(keywords, inFileName):
    ''' 
    DESCRIPTION
        Grabs blocks of lines from a file based on input keywords. Returns the
        blocks as arrays within an ordered array.
    
    INPUT
        Keywords: Array of keywords to look for. Separate keyword lists by
        including multiple arrays. Each keyword list should consist of one
        header and one footer for the blocks.
        
        Ex. keywords = [[['header1','word'],['footer1','letter']],
                       [['header2','tree'],['footer2','leaf']]]
        
        inFile: Name of file to parse.
        
    OUTPUT
        outArray: Array of blocks lines matching with keywords. Placed in order
        in which the blocks were located. 
    '''
    # Variables
    outArray = []
    inBlock = False             # Boolean, gathering data from block
    tmpArray = []               # Temporary array for storing block lines

    # Open input file
    inFile = open(inFileName,'r')

    # Parse lines of input file
    for line in inFile:
        # Format line for easy checking
        lineCheck = line.strip()
        lineCheck = lineCheck.split()

        # Check against keywords
        for query in keywords:

            # Check for footer
            if (inBlock == True):
                for index,word in enumerate(query[1]):
                    # If word is not in line then move on to next query
                    if (word not in lineCheck):
                        break
                    # If word is in line and it is the last in the query,
                    # found footer
                    elif (word in lineCheck) and (index == len(query)-1):
                        inBlock = False

                        # Add tmpArray to outArray and clear tmpArray
                        outArray.append(tmpArray)
                        tmpArray = []

            # Check for header
            if (inBlock == False):
                for index,word in enumerate(query[0]):
                    # If word is not in line then move on to next query
                    if (word not in lineCheck):
                        break
                    # If word is in line and it is the last in the query,
                    # found header
                    elif (word in lineCheck) and (index == len(query)-1):
                        inBlock = True

        # Gather lines within blocks
        if (inBlock == True):
            tmpArray.append(line)                

    return outArray

'''
## Main Function
if (__name__ == '__main__'):
    # Nothing Here
'''