import re

file_codonTable = open("RNA_codon_table.txt")

# Parse codon table and create dictionary of single AA
codons = []
table = {}
for line in file_codonTable:
	#codons.append(re.findall('[ACGU]{3}',line))
	#codons.append(re.findall('^\w\w\w\s|\s\w\w\w\s',line))
	#codons = re.findall('[ACGU]{3}',line)
	codons = re.findall('(\w\w\w)\s(\w)\s|(\w\w\w)\s(Stop)\s',line)

	for item in codons:
		#if re.search('^\w\w\w,item')
		# codon = re.search('^(\w\w\w)\s+',item)
		# aa = re.search('\s+(\w)$',item)
		# print(codon)
		# print(aa)
		# table[codon] = aa
		codon = str(item[0]) + str(item[2])
		aa = str(item[1]) + str(item[3])
		table[codon] = aa
		# print('codon: ' + codon)
		# print('aa: ' + aa)

file_codonTable.close()
# Translate codons to aa

file = open("rosalind_prot.txt")

sequence = file.readline().strip()
peptide = ""
codons = {}


for i in range(len(sequence)/3):
	start = i*3
	end = start+3
	temp_codon = sequence[start:end]
	# print temp_codon
	if table[temp_codon] == 'Stop':
		break
	peptide += str(table[temp_codon])
	

print peptide
######TODO: how to access three characters at a time