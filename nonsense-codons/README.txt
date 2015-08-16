nonsense-codons 
08/2015

For this practice, you'll determine how what proportion of all possible  
mutations to a DNA coding sequence are nonsense mutations. To do this, you'll 
need to be able to do a couple things:

1) read a FASTA file containing the sequence to be analyzed
2) loop through sequence and identify possible nonsense mutations
3) output both proportion of mutations and a list of all nonsense mutations 
   in both dna and protein sequence in the following tab-delimited format:
		
		seq_name	dna_mutation	pro_mutation
		GAL4	A4T	K2*
		...
		0.0454774502394 (361/7938)

Notes:

a) reading a FASTA file isn't exactly a trivial task, so I usually use someone 
   else's code for it. I've added a python script, parse_fasta.py, which 
   contains the relevant function (as written by brent_p, who's currently a 
   member of Aaron Quinlan's lab at the University of Utah). Using biopython 
   or bioperl would be a perfect solution to this problem, as they have their 
   own sequence parsers.

b) For output, you'll need to translate the DNA sequence to a protein sequence
   -- what's the best way to store the codon table?

c) Don't count wildtype stop codons in the sequence in your calculation.
