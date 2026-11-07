def comp(sequence):
    complement = ''
    for x in sequence:
        if x == 'A':
            complement += 'T'
        elif x == 'T':
            complement += 'A'
        elif x == 'G':
            complement += 'C'
        else:
            complement += 'G'
    return complement

def revcomp(sequence):
    newString = comp(sequence)
    revcomplement = ''
    for i in range(len(newString) - 1, -1, -1):
        revcomplement += newString[i];
    return revcomplement

seq = input('Enter DNA Sequence: ').upper()
value = True
for x in seq:
    if len(seq) == 0 or x not in 'ATGC':
        value = False

if value == False:
    print("Error. Invalid DNA sequence.")
else:
    print('Complement: ', comp(seq))
    print('Reverse Complement: ', revcomp(seq))