'''
pySCFPlot.py

Author: Daniel Burrill
Date Created: November 6, 2013
Date Last Modified: November 6, 2013

v1.00
- Initial Build.

Description:
 Grabs SCF energy and outputs csv.
 
'''

## Imports
import pyLines
import pyCSV

## Variables
inFileName = 'output.out'
keywords = [['total','energy','=']]
energyData = []

## Functions

## Main Function
if (__name__ == '__main__'):
    # Grab relevant lines from file
    energyLines = pyLines.pyLines(keywords,inFileName)
    
    # Split & strip entries
    for index,entry in enumerate(energyLines):
        energyLines[index] = entry.strip().split()
    
    # Parse for data
    for index,energy in enumerate(energyLines):
        if (len(energy) == 5):
            energyData.append([index,energy[3]])
            
    print energyData
    
    # Output to csv format
    pyCSV.pyCSV(energyData)
    