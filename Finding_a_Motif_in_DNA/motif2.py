file = open("rosalind_subs.txt")

sequence = file.readline().strip()
motif = file.readline().strip()


print(sequence)
print(motif)

begin = 0
end = 0
count = 0

location = []

for i in range(len(sequence)-(len(motif)-1)):
	begin = i
	end = begin + len(motif)
	#print(sequence[begin:end])

	
	if motif == sequence[begin:end]:
		location.append(begin+1)
		# Uncomment if statment to print count
		#count += 1

#print(count)
result = ""
for item in location:
	result += str(item) + " "
print result