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

seq = input('Enter DNA Sequence: ').upper()
valid = True

for x in seq:
    if x not in 'AGCT':
        valid = False

if valid:
    dna_analysis()
else:
    print('Error. Sequence cannot be analyzed.')