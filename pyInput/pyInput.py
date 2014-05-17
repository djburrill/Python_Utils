# pyInput.py

## Imports

## Functions
def fKeyword(keyword,inFileName):
	'''
	Comments are '#'
	Splits at '='
	'''
	
	## Variables
	keyVar = []
	
	## Engine
	# Open File
	inFile = open(inFileName,'r')
	
	# Convert keyword to lowercase
	keyword = str(keyword).lower()
	
	# Search inFile for keyword
	for line in inFile:
		# Strip White Space Off Line
		line = line.strip()
		
		# If not Comment, split at '='
		if (len(line) != 0) and (line[0] != '#'):
			line = line.split('=')
			
			# If Keyword we are Searching For
			if (line[0].strip().lower() == keyword):
				# Set keyVar to the values of the keyword
				keyVar = line[1].split(',')
				
	# Clean keyVar by Removing White Spaces
	for index,value in enumerate(keyVar):
		keyVar[index] = value.strip()
	
	# Close File
	inFile.close()
	
	# Return Values
	return keyVar

## Main
if (__name__ == '__main__'):
	'''
	## Test Cases
	inFileName = 'format.dat'
	
	# Normal Input
	in1 = fKeyword('key1',inFileName)
	
	# Spaces
	in2 = fKeyword('key2',inFileName)
	
	# Doesn't grab comment
	in3 = fKeyword('# Comment',inFileName)
	
	# Can Skip Empty Lines
	in4 = fKeyword('key4',inFileName)
	
	print 'in1: ' + ','.join(in1) + '\n'
	print 'in2: ' + ','.join(in2) + '\n' 
	print 'in3: ' + ','.join(in3) + '\n'
	print 'in4: ' + ','.join(in4) + '\n'
	'''
	
