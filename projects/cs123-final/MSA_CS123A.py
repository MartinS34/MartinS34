from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
# Scoring function:
match = 1
mismatch = -1
gap = -2

def needlemanWunsch(seq1, seq2):
    """
    Function to perform alignment using the Needleman-Wunsch algorithm.
    Arguments:
        seq1, seq2: The two sequences to align.
    Returns:
        Two aligned sequences with gaps introduced where necessary.
    References:
        https://stackoverflow.com/questions/63120727/needleman-wunsch-algorithm-for-two-sequences-of-different-length
    """
    s1Length = len(seq1)
    s2Length = len(seq2)

    # Scoring system
    match = 1
    mismatch = -1
    gap = -2

    # STEP 1: Create scoring matrix
    Matrix2D = [[0] * (s2Length + 1) for _ in range(s1Length + 1)]

    # STEP 2: Initialize first row and column with gap penalties
    for i in range(1, s1Length + 1):
        Matrix2D[i][0] = i * gap
    for j in range(1, s2Length + 1):
        Matrix2D[0][j] = j * gap

    # STEP 3: Fill in the matrix
    for i in range(1, s1Length + 1):
        for j in range(1, s2Length + 1):
            deletion = Matrix2D[i - 1][j] + gap  # Deletion (gap in seq2)
            insertion = Matrix2D[i][j - 1] + gap  # Insertion (gap in seq1)
            matchScore = Matrix2D[i - 1][j - 1] + (match if seq1[i - 1] == seq2[j - 1] else mismatch)
            Matrix2D[i][j] = max(deletion, matchScore, insertion)  # Pick the best score

    # STEP 4: Traceback to determine alignment
    align1 = []
    align2 = []
    i, j = s1Length, s2Length

    while i > 0 and j > 0:
        currScore = Matrix2D[i][j]
        # Match or mismatch
        if Matrix2D[i - 1][j - 1] + (match if seq1[i - 1] == seq2[j - 1] else mismatch) == currScore:
            align1.append(seq1[i - 1])
            align2.append(seq2[j - 1])
            i -= 1
            j -= 1
        # Gap in seq2
        elif Matrix2D[i - 1][j] + gap == currScore:
            align2.append("-")
            align1.append(seq1[i - 1])
            i -= 1
        # Gap in seq1
        else:
            align2.append(seq2[j - 1])
            align1.append("-")
            j -= 1

    # Fill remaining gaps if one sequence runs out
    while i > 0:
        align2.append("-")
        align1.append(seq1[i - 1])
        i -= 1
    while j > 0:
        align1.append("-")
        align2.append(seq2[j - 1])
        j -= 1

    # Reverse alignments for correct order
    align1 = ''.join(reversed(align1))
    align2 = ''.join(reversed(align2))

    return align1, align2



def commonMotifs(sequences):
    """
    identify the common motif sequence from list of aligned sequences.
    sequences(argument): List of aligned sequences with gaps.
    return value:
    A single consensus sequence based on the most common character at each position.
    """
    length = len(sequences[0])
    motifs = []
    #loop to extract the ith column across all seqs. find the commonly occurring chars
    for i in range(length):
        column = [seq[i] for seq in sequences]  
        mostCommon = max(set(column), key=column.count)  
        motifs.append(mostCommon)
    return ''.join(motifs)

def SeqGapping(sequences):
    """
    function serves to verify all sequences are of equal length.
    sequences(arg): lists of aligned sequences with varying lengths.
    return a List of sequences padded with gaps to match the longest sequence.
    """
    maxLength = max(len(seq) for seq in sequences)  #determine the max length of all seqs
    gappedSeqs = [seq.ljust(maxLength, "-") for seq in sequences]  # if seqs are less than max, then add gaps
    return gappedSeqs

def alignTheTails(sequences):
    """
    function to align the trailing egions of all sequences based on the longest motif.
    sequences(arg): List of aligned sequences with varying end gaps
    returns a list of sequences with the ends aligned to the longest motif.
    """
    longTail = max([seq.rstrip('-') for seq in sequences], key=len) 
    alignTails = []
    for seq in sequences:
        stripped_seq = seq.rstrip('-')  #remove trailing gaps
        aligned_seq = stripped_seq.ljust(len(longTail), '-')
        alignTails.append(aligned_seq)
    return SeqGapping(alignTails)  # add more gaps just in case.

def alignAlongMotifs(consensus, sequences,):
    """
    fucntion to align all sequences to the given common motif
    consensus(arg): The consensus sequence to align against.
    sequences(arg): List of sequences to align
    returns a list of sequences aligned to the consensus.
    """
    aligned_sequences = []
    for seq in sequences:
        _, aLIGNEDSEQ = needlemanWunsch(consensus, seq)
        aligned_sequences.append(aLIGNEDSEQ)
    return SeqGapping(aligned_sequences)


def MSA(sequences, iterations=30):
    """
    does multiple sequence alignmentiteratively.
    sequences(arg): List of sequences to align.
    iterations(arg): Number of refinement iterations to perform.
    RETURNS Final list of aligned sequences.
    """
    alignedSEQUENCES = [sequences[0]]  # begin with the first sequence 
    for seq in sequences[1:]:
        for alignedSeq in alignedSEQUENCES:
            alignedSeq, seq = needlemanWunsch(alignedSeq, seq)  # align each sequence progressively
        alignedSEQUENCES.append(seq)
    #refine alignment
    for _ in range(iterations):
        alignedSEQUENCES = SeqGapping(alignedSEQUENCES)  #add padding if necessary
        consensus = commonMotifs(alignedSEQUENCES)
        alignedSEQUENCES = alignAlongMotifs(consensus, sequences)  # realign
    alignedSEQUENCES = alignTheTails(alignedSEQUENCES)
    return alignedSEQUENCES

def format(alignedSEQs, blkSize=100):
    """
    fucntion to format the final alignment in a Clustal-like style for readability.
    alignedSEQa(args):list of aligned sequences.
    blksize(args): num of characters to display per block.

    prints the formatted alignment with a consensus line.
    """
    seqlen = len(alignedSEQs[0])  # length of the aligned sequences
    motif = commonMotifs(alignedSEQs)
    # print
    for start in range(0, seqlen-1, blkSize-1):
        end = start + blkSize
        print()  #new line
        for idx, seq in enumerate(alignedSEQs):
            print(f"Seq{idx+1:<3} {seq[start:end]}") 
        print(f"     {motif[start:end]}") 
# load sequences from local .FASTA file
fastaFile = "/Users/martiin/VSCode/2024JavaPersonal/MS2024/src/tp53sequences.fasta"
sequences = [str(record.seq) for record in SeqIO.parse(fastaFile, "fasta")]
#execute MSA with iterative refinement and tail alignment
finalAlignment = MSA(sequences)
# print the alignment in Clustal-like format
format(finalAlignment)
# save the aligned sequences to a new FASTA file
with open("alignedSequences-CS123.fasta", "w") as output:
    for idx, aligned_seq in enumerate(finalAlignment):
        record = SeqRecord(Seq(aligned_seq), id=f"Seq{idx+1}")
        SeqIO.write(record, output, "fasta")