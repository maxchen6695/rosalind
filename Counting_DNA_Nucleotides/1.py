A = 0
C = 0
G = 0
T = 0


with open("rosalind_dna.txt") as file:
	for line in file:
		for ch in line:
			if ch == 'A':
				A += 1
			elif ch == 'C':
				C += 1
			elif ch == 'G':
				G += 1
			elif ch == 'T':
				T += 1
			else:
				break

result = str(A) + " " + str(C) + " " + str(G) + " " + str(T)

print(result)