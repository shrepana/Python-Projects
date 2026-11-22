# This project takes a DNA sequence and returns 
# the GC Percentage, nucleotide counts, and
# sequence length.

# function that prints out sequence, length of 
# sequence, and GC content in sequence
def dna_analysis():
    print('Sequence:', seq)
    print('Length:', len(seq))

    a = g = c = t = 0
    for letter in seq:
        if letter == 'A':
            a+=1
        elif letter == 'G':
            g+=1
        elif letter == 'C':
            c+=1
        else:
            t+=1
    print('A:', a)
    print('G:', g)
    print('C:', c)
    print('T:', t)

    if len(seq) != 0:
       gcpercent = ((g + c)/len(seq)) * 100
       print(f'GC Content: {gcpercent:.2f}%')
    else:
        print('Invalid. Cannot compute.')

# uses user input to get DNA sequence
seq = input('Enter DNA Sequence: ').upper()
valid = True

# validates whether sequence is real based on 
# nucleotides that make up sequence
for x in seq:
    if x not in 'AGCT':
        valid = False

# executes analysis if valid and else gives an 
# error message
if valid:
    dna_analysis()
else:
    print('Error. Sequence cannot be analyzed.')