fileCount = open("data.txt")
file = open("data.txt")
count = 0;

stringID = [] 
stringData = []

## Calculates GC content percentage
def calcGC(string):
	gc = 0;
	total = 0;
	for char in string:
		if char == 'C' | char == 'G':
			gc = gc + 1
			total = total+1
		elif char == 'A' | char == 'T':
			total = total+1
		else:
			continue
	return gc/total

## Finds the max GC content item
def highestGC(list):
	max = 0;
	for item in list:
		if item > max:
			max = item
	return max



##Count number of IDs and add IDs to list
lineCount = fileCount.readline().strip()
for item in lineCount:
	if item[0] == '>.+':
		count = count+1
		stringID.append(item[1:])
## Print out results
print(str('count: ') + str(count))

## find GC content
line = file.readline().strip()
for seq in line[1:]:
	if seq[0] != '>':
		sequence.append(seq)
	else:
		stringData.append(calcGC(sequence))
		sequence = ""


##get element with highest GC content
maxScore = highestGC(sequence)
print(maxScore)