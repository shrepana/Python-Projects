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

def find_codon(sequence, position):
    start = ((position - 1) //3) * 3
    return sequence[start:start + 3]

ref = input("\nEnter reference DNA sequence: ").upper()
samp = input("Enter sample DNA sequence: ").upper()

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

    if number != 0:
        print("Mutation positions: ", mutations)
        print("Number of mutations: ", number, "\n")

        position_record = []
        for position, original, changed in info:
            position_record.append(position)

        
        for position, original, changed in info:
            if position != position_record[0]:
                if (position - 1) // 3 == (position_record[position_record.index(position) - 1] - 1) // 3:
                    continue
            for item in range(len(position_record)):
                if (position_record[item] - 1) // 3 == (position - 1) // 3:
                    print("Change in nucleotide position", position_record[item], ":", ref[position_record[item] - 1], "->", samp[position_record[item] - 1])

            y = find_codon(samp, position)
            x = find_codon(ref, position)
            
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