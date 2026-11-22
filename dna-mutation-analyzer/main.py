# This project finds the type of mutation present when
# given two strings of DNA sequences to compare. It also 
# tells the user the codon and amino acid change as a 
# result of this mutation.

# dictionary of all codons to amino acids
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

# function that compares the two DNA sequences and returns 
# where the mutation occured on 1-based index, mutation info 
# (which stores mutation position, original nucleotide, and 
# mutated nucleotide), and number of mutations
def comp(reference, sample):
    mutation = []
    number = 0
    mutationinfo = []
    for i in range(len(reference)):
        if reference[i] != sample[i]:
            mutation.append(i+1)
            mutationinfo.append((i+1, reference[i], sample[i]))
            number+=1
    return mutation, mutationinfo, number

# function returns codon with a given nucleotide position
def find_codon(sequence, position):
    start = ((position - 1) //3) * 3
    return sequence[start:start + 3]

# gets and saves user entered reference DNA sequence 
# and sample DNA sequence
ref = input("\nEnter reference DNA sequence: ").upper()
samp = input("Enter sample DNA sequence: ").upper()

# sees if both sequence inputs are valid sequences
valid = True
if len(ref) != len(samp) or len(ref) % 3 != 0:
    valid = False
else:
    for x in ref:
        if x not in "AGTC":
            valid = False   
    for i in samp:
        if i not in "AGTC":
            valid = False

if valid == False:
    print("Error. Sequence cannot be analyzed.")     
else:
    mutations, info, number = comp(ref, samp)

    # displays mutation positions and number of mutations
    if number != 0:
        print("Mutation positions: ", mutations)
        print("Number of mutations: ", number, "\n")

        #records positions for all mutations and saves them in list
        position_record = []
        for position, original, changed in info:
            position_record.append(position)

        # groups mutations within the same codon to avoid over-analysis
        # of codon more than once
        for position, original, changed in info:
            if position != position_record[0]:
                if (position - 1) // 3 == (position_record[position_record.index(position) - 1] - 1) // 3:
                    continue
            
            # displays all nucleotides changed within one codon
            for item in range(len(position_record)):
                if (position_record[item] - 1) // 3 == (position - 1) // 3:
                    print("Change in nucleotide position", position_record[item], ":", ref[position_record[item] - 1], "->", samp[position_record[item] - 1])

            # stores original and mutated codons
            y = find_codon(samp, position)
            x = find_codon(ref, position)

            # identifies type of mutation based on type of amino acid change
            if y in ["TAA", "TAG", "TGA"] and x not in ["TAA", "TAG", "TGA"]:
                print("Nonsense. Stop codon introduced.")
                print("Codon: ", x, "->", y)
                print("Amino Acid: ", dnadict[x], "->", dnadict[y], "\n")
            elif dnadict[x] != dnadict[y]:
                print("Missense. Amino acid change.")
                print("Codon: ", x, "->", y)
                print("Amino Acid: ", dnadict[x], "->", dnadict[y], "\n")
            else:
                print("Synonymous. No amino acid change.")
                print("Codon: ", x, "->", y)
                print("Amino Acid: ", dnadict[x], "->", dnadict[y], "\n")

    else:
        print("No mutations exist!")