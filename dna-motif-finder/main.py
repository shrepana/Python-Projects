# This project finds every repetition of a motif 
# within a DNA Sequence and returns the number 
# of repetitions

# Records locations of each occurance using 1-based indexing
def motif_finder(sequence, motif):
    seq_list = []
    for i in range(0, len(sequence) - len(motif) + 1):
        if sequence[i:i+len(motif)] == motif:
            seq_list.append(i + 1)
    return seq_list

# User Input to record DNA Sequence and morif
seq = input('Enter DNA Sequence: ').upper()
motif = input('Enter Motif: ').upper()

# Determines which inputs will be taken and which won't
valid = True;
if len(motif) > 0 and len(seq) >= len(motif):
    for x in motif:
        if x not in 'ACTG':
            valid = False
    for y in seq:
        if y not in 'ACTG':
            valid = False
else:
    valid = False

results = motif_finder(seq, motif)

# Returns all locations of occurance and length of occurance
# if the sequence is valid.
if valid:
    print(results)
    print(len(results))
else:
    print('Invalid sequence/motif.')