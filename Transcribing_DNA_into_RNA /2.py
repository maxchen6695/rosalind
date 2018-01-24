sequence = ""

with open("rosalind_rna.txt") as file:
	for line in file:
		for ch in line:
			if ch == 'T':
				sequence += 'U'
			else:
				sequence += ch

print(sequence)