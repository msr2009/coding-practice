"""
nonsense-codons.py

Matt Rich, 08/2015
"""

from fasta_iter import fasta_iter #I'm using fasta_iter to read FASTAs

def main(fasta):
	
	nonsense_mutations = 0
	codon_counter = 1
	dna = set(["A", "C", "G", "T"])

	#read fasta file using fasta_iter
	for header, seq in fasta_iter(fasta):
		#loop over sequence and identify nonsense mutations
		#for each codon
		for i in range(0,len(seq),3):
			codon = seq[i:i+3]
			#for each base in codon
			for b in range(3):
				#what are the possible mutations at this
				#position?
				muts = dna.difference(set(codon[b]))
				#check each possible mutation
				for m in muts:
					#make the mutation to the codon
					tmp = list(codon)
					tmp[b] = m
					#translate and see if the mutation make a stop codon
					if translate_sequence("".join(tmp)) == "*" and \
					   translate_sequence(codon) != "*":
						#print the output
						print "\t".join([header, codon[b] + str(i+b+1) + m,
										 translate_sequence(codon) + \
										 str(codon_counter) + \
										 translate_sequence("".join(tmp))])
						#increment the number of nonsense mutations
						nonsense_mutations += 1
			#increment codon_counter				
			codon_counter += 1

		#finally, print the number of total possible mutations, possible
		#nonsense mutations, and proportion mutations
		print str(nonsense_mutations/float(len(seq)*3)), \
			  "(" + str(nonsense_mutations) + "/" + str(len(seq)*3) + ")"

# lookup table for codon translation
def lookup_codon(codon):
	lookup = { 'ttt': 'F', 'tct': 'S', 'tat': 'Y', 'tgt': 'C',
               'ttc': 'F', 'tcc': 'S', 'tac': 'Y', 'tgc': 'C',
               'tta': 'L', 'tca': 'S', 'taa': '*', 'tga': '*',
               'ttg': 'L', 'tcg': 'S', 'tag': '*', 'tgg': 'W',
               'ctt': 'L', 'cct': 'P', 'cat': 'H', 'cgt': 'R',
               'ctc': 'L', 'ccc': 'P', 'cac': 'H', 'cgc': 'R',
               'cta': 'L', 'cca': 'P', 'caa': 'Q', 'cga': 'R',
               'ctg': 'L', 'ccg': 'P', 'cag': 'Q', 'cgg': 'R',
               'att': 'I', 'act': 'T', 'aat': 'N', 'agt': 'S',
               'atc': 'I', 'acc': 'T', 'aac': 'N', 'agc': 'S',
               'ata': 'I', 'aca': 'T', 'aaa': 'K', 'aga': 'R',
               'atg': 'M', 'acg': 'T', 'aag': 'K', 'agg': 'R',
               'gtt': 'V', 'gct': 'A', 'gat': 'D', 'ggt': 'G',
               'gtc': 'V', 'gcc': 'A', 'gac': 'D', 'ggc': 'G',
               'gta': 'V', 'gca': 'A', 'gaa': 'E', 'gga': 'G',
               'gtg': 'V', 'gcg': 'A', 'gag': 'E', 'ggg': 'G' }
	return lookup[codon.lower()]

# translate DNA -> amino acid
def translate_sequence(seq):
    translated_seq = ''
    i = 0
    while i <= len(seq)-3:
           translated_seq += lookup_codon(seq[i:i+3])
           i += 3
    return translated_seq


if __name__ == "__main__":
	
	from argparse import ArgumentParser

	parser = ArgumentParser()
	parser.add_argument('--fasta', action = 'store', type = str, dest = 'fasta', 
		help = "FASTA file")
	args = parser.parse_args()
	
	main(args.fasta)	

