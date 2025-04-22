def read_fasta(filename):
    with open (filename, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]

    sequences = []
    current_seq = ''
    for line in lines:
        if line.startswith('>'):
            if current_seq:
                sequences.append(current_seq)
                current_seq = ''
        else :
            current_seq += line
    sequences.append(current_seq)
    return sequences[0], sequences[1]

def calculate_ratio(s1, s2):
    transitions = 0
    transversions = 0

    transition_pairs = [('A', 'G'), ('G', 'A'), ('C', 'T'), ('T', 'C')]

    for base1, base2 in zip(s1, s2):
        if base1 != base2:
            if (base1, base2) in transition_pairs:
                transitions += 1
            else:
                transversions += 1

    return transitions / transversions if transversions != 0 else float('inf')

# Usage
if __name__ == "__main__":
    s1, s2 = read_fasta("dna_sequences.txt")
    ratio = calculate_ratio(s1, s2)
    print(f"{ratio}")
