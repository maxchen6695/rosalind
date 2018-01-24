file = open("rosalind_revc.txt")

line = file.readline().strip()

sequence = ""

for ch in line:
	if ch == 'A':
		sequence += 'T'
	elif ch == 'C':
		sequence += 'G'
	elif ch == 'G':
		sequence += 'C'
	elif ch == 'T':
		sequence += 'A'
	else:
		break

reverse = sequence[::-1]

print(reverse)