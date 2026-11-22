# This project translates DNA sequence to an amino acid sequence, 
# using start and stop codons to determine where to start and 
# stop respectively.

dnadict = {
    "ATG": "M",
    "TAA": "stop", "TAG": "stop", "TGA": "stop",
    "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "TGT": "C", "TGC": "C",
    "GAT": "D", "GAC": "D",
    "GAA": "E", "GAG": "E",
    "TTT": "F", "TTC": "F",
    "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G",
    "CAT": "H", "CAC": "H",
    "ATA": "I", "ATT": "I", "ATC": "I",
    "AAA": "K", "AAG": "K",
    "TTA": "L", "TTG": "L", "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L",
    "AAT": "N", "AAC": "N",
    "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CAA": "Q", "CAG": "Q",
    "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R", "AGA": "R", "AGG": "R",
    "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S", "AGT": "S", "AGC": "S",
    "ACT": "T", "ACC": "T", "ACG": "T", "ACA": "T",
    "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V",
    "TGG": "W",
    "TAT": "Y", "TAC": "Y"
}

# function that returns position of starting point based on 
# where start codon is (0-base)
def find_start(sequence):
    for i in range(len(sequence)-2):
        if sequence[i:i+3] == "ATG":
            return i

# function that returns position of ending point based on 
# where stop codon is (0-base)
def find_end(sequence, startposition):
    for x in range(startposition, len(sequence)-2, 3):
        if sequence[x:x+3] in ["TAA", "TAG", "TGA"]:
            return x

# function that returns string of amino acid sequence from 
# start codon to stop codon, returning errors if sequence 
# cannot be analyzed due to lack of start codon or stop codon.
def translate_dna(sequence):
    amino_seq = ""
    start = find_start(sequence)
    if start != None:
        end = find_end(sequence, start)
        if end != None:
            for i in range(start, end, 3):
                if sequence[i:i+3] in dnadict:
                    amino_seq += dnadict[sequence[i:i+3]]
                else:
                    return "Error. Sequence cannot be analyzed."
            return amino_seq
        else:
            return "Error. Sequence cannot be analyzed."
    else:
        return "Error. Sequence cannot be analyzed."

# stores user input of DNA sequence
seq = input("Enter DNA Sequence: ").upper()

# validates if sequence can be analyzed and either executes 
# translate_dna function if it is valid or otherwise returns 
# an error message
valid = True
for letter in seq:
    if letter not in "AGTC":
       valid = False

if valid == False:
    print("Error. Sequence cannot be analyzed.")
else:
    print(translate_dna(seq))