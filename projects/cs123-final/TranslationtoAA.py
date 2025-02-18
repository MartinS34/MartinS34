# standard codon table for translation; used as a python dictionary
codonTable = {
    'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
    'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
    'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
    'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
    'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
    'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
    'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
    'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
    'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
    'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
    'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
    'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
    'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
    'TAC': 'Y', 'TAT': 'Y', 'TAA': '*', 'TAG': '*',
    'TGC': 'C', 'TGT': 'C', 'TGA': '*', 'TGG': 'W',
}
def translate(ntSeq):
    """
    this fucntion translates a nucleotide sequence into an amino acid sequence using the nromal codon table.
    nucleotide_seq (arg)(str): The nucleotide sequence.
    returns str: The translated amino acid sequence without stop codons.
    """
    proteins = []
    # translate current codon
    for i in range(0, len(ntSeq) - len(ntSeq) % 3, 3):
        current = ntSeq[i:i + 3]
        aa = codonTable.get(current, 'X')  # 'X' for unknown codons
        if aa == '*':  # skip the stop codons
            break
        proteins.append(aa)# append translated amino acid
    return ''.join(proteins)

def process_fasta(inputf, outputf):
    """
    processes a .fasta file and translates nucleotide sequences into amino acid sequences.
        input_fasta (args)(str): Path to the input FASTA file.
        output_fasta (args)(str): Path to save the output FASTA file.
    """
    with open(inputf, 'r') as infile, open(outputf, 'w') as outfile:
        currentID = None
        currentSEQ = []
        for line in infile:
            line = line.strip()
            if line.startswith(">"):  # FASTALINE
                # if we have a sequence collected, process and write it
                if currentID is not None:
                    translated_seq = translate(''.join(currentSEQ))
                    outfile.write(f"{currentID}\n{translated_seq}\n")
                #new seq
                currentID = line
                currentSEQ = []
            else:
                currentSEQ.append(line.upper())
        #last seq
        if currentID is not None:
            translated_seq = translate(''.join(currentSEQ))
            outfile.write(f"{currentID}\n{translated_seq}\n")

inputFILE = "/Users/martiin/VSCode/2024JavaPersonal/MS2024/src/nonMammal_tp53_nt.txt"  
outputFILE = "/Users/martiin/VSCode/2024JavaPersonal/MS2024/src/output.fasta"  
process_fasta(inputFILE, outputFILE)
print(f"Translation finished, saved to {outputFILE}")