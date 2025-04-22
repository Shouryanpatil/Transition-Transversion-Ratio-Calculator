# Transition/Transversion Ratio Calculator

This repository contains a Python script to compute the **transition/transversion ratio** between two DNA sequences of equal length.

## Problem Description
Given two DNA strings `s1` and `s2` of equal length (at most 1 kbp), the transition/transversion ratio \( R(s1, s2) \) is defined as:

[ R(s1, s2) = Number of transitions/ Number of transversions ]

### Definitions:
- **Transitions**: Substitutions between purines (A ↔ G) or pyrimidines (C ↔ T).
- **Transversions**: Substitutions between a purine and a pyrimidine (A ↔ C/T, G ↔ C/T).

---

## File Structure
```
.
├── dna_sequences.txt                # Input file with two DNA sequences in FASTA format
├── transition_transversion_ratio.py # Python script to calculate the ratio
└── README.md                        # This file
```

---

## Input Format
The input file (`dna_sequences.txt`) should be in **FASTA format**:
```txt
>Rosalind_0209
GCAACGCACAACGAAAACCCTTAGGGACTGGATTATTTCGTGATCGTTGTAGTTATTGGAAGTACGGGCATCAACCCAGTT
>Rosalind_2200
TTATCTGACAAAGAAAGCCGTCAACGGCTGGATAATTTCGCGATCGTGCTGGTTACTGGCGGTACGAGTGTTCCTTTGGGT
```

---

## Usage

### 1. Save Your Files
- Save your input file as `dna_sequences.txt`
- Save the script as `transition_transversion_ratio.py`

### 2. Run the Script
```bash
python transition_transversion_ratio.py
```

### 3. Output
The script will print:
```
1.2142857142857142
```

---
## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

