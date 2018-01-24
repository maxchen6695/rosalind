file1 = open("rosalind_hamm.txt")

seq1 = file1.readline().strip()
seq2 = file1.readline().strip()

count = 0
for i in range(len(seq1)):
	if seq1[i] != seq2[i]:
		count += 1

print count