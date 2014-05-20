'''
pyCSV.py

Author: Daniel Burrill
Date Created: November 6, 2013
Date Last Modified: December 24, 2013

v1.02
- Added ability to handle columns of different lengths

v1.01
- Fixed infinite loop bug in column format

v1.00
- Initial Build.

Description:
 Outputs formatted arrays into csv format.
 
'''

## Imports

## Variables

## Functions

# arrayValToString
def arrValToStr(array1):
    
    for index,value in enumerate(array1):
        array1[index] = str(value)
        
    return array1
    
# uniArray
def uniArray(array1):
    
    # Variables
    maxLen = 0
    
    # Find maximum length
    for subArray in array1:
        if (len(subArray) > maxLen):
            maxLen = len(subArray)
            
    # Buffer all sub arrays to match maxLen in length
    for subArray in array1:
        while (len(subArray) < maxLen):
            subArray.append('')

# pyCSV
def pyCSV(data,outFileName='outFile.csv',row=True):
    ''' 
    DESCRIPTION
        Writes data array to csv. Since data can be written in either rows or columns
    
    INPUT
        data: Array containing row arrays
        
        Ex. data = [[1,2,3],[4,5,6]]
        
        outFileName: Name of output file.
        
        row: Specifies whether data is given in rows or columns
        
    OUTPUT
        None
    '''
    
    # Variables
    dmyString = ''
    
    # Create output file
    outFile = open(outFileName,'w')
    
    # Convert data to strings
    for index,dataArr in enumerate(data):
        data[index] = arrValToStr(dataArr)
        
    # Make data array uniform
    
    # Data Columns
    if (row == False):
        subArrayLen = len(data[0])
        iCounter = 0
        
        while (iCounter < subArrayLen):
            # Reset dummy string
            dmyString = ''
            
            # Populate dummy string
            for index,subArray in enumerate(data):
                # If Column does not contain enough data
                if (len(subArray) <= iCounter) and (index == len(data)-1):
                    dmyString += '' + '\n'
                elif (len(subArray) <= iCounter):
                    dmyString += '' + ','
                # If last index 
                elif (index == len(data)-1):
                    dmyString += subArray[iCounter] + '\n'
                # If not last index
                else:
                    dmyString += subArray[iCounter] + ','
                
            # Write dummy string to file
            outFile.write(dmyString)

            iCounter += 1
            
    # Data Rows
    else:            
        # Populate dummy string
        for subArray in data:
            
            # Reset dummy string
            dmyString = ''
        
            for index,val in enumerate(subArray):
                if (index == len(subArray)-1):
                    dmyString += val + '\n'
                else:
                    dmyString += val + ','
                        
            # Write dummy string to file
            outFile.write(dmyString)
            
    outFile.close()

'''
## Main Function
if (__name__ == '__main__'):
    testArray = [[1,10],[2,45],[3,67]]
    
    pyCSV(testArray)
'''
