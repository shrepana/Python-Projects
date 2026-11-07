def motif_finder(sequence, motif):
    seq_list = []
    for i in range(0, len(sequence) - len(motif) + 1):
        if sequence[i:i+len(motif)] == motif:
            seq_list.append(i + 1)
    return seq_list


seq = input('Enter DNA Sequence: ').upper()
motif = input('Enter Motif: ').upper()

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

if valid:
    print(results)
    print(len(results))
else:
    print('Invalid sequence/motif.')