#file = open("data.txt")

def calcGC(string):
	#print('calcGC: ')
	#print(string)
	gc = 0;
	total = 0;
	for char in string:
		if (char == 'C'):
			gc += 1
			total += 1
		elif char == 'G':
			gc += 1
			total += 1
		elif (char == 'A'):
			total += 1
		elif char == 'T':
			total += 1
		else:
			continue

	#print('gc: ' + str(gc))
	#print('total: ' + str(total))
	result = (float(gc) / float(total)) * 100
	#print('result: ' + str(result))
	return result

## Finds the max GC content item
# def highestGC(list):
# 	max = 0;
# 	for listKey in list:
# 		if list.get(listKey) > max:
# 			max = list.get(listKey)
# 	return max

dictionary = dict()
key = ""
value = ""

#line = file.readline().strip()

## Create dictionary of 
with open("rosalind_gc.txt") as file:
	for item in file:
		item = item.strip()
		#print(item)
		if item[0] == ">":
			value = ""
			key = item
			#print('key: ' + key)
		else:
			value += item
			dictionary[key] = value
			#print('value: ' + value)
	
#print('DICTIONARY: \n')
#print(dictionary.items())
## Copy Key and set value to GC content
content = dict()
for newKey in dictionary:
	#print('newKey: ')
	#print(newKey)
	content[newKey] = calcGC(dictionary.get(newKey))
	#print(dictionary.get(newKey))

#print('CONTENT: \n')
#print(content.items())
##maxGC = highestGC(content)

maxID = ""
maxValue = 0
for contentKey in content:
	if content.get(contentKey) > maxValue:
		maxID = contentKey
		maxValue = content.get(contentKey)

print(maxID[1:])
print(maxValue)