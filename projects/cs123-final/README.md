# TP53 Phylogenetic Analysis

## 📌 Overview
This project analyzes the **TP53 gene** across different species using **Multiple Sequence Alignment (MSA)** with the **Needleman-Wunsch algorithm** and **phylogenetic tree construction** to study its evolutionary relationships.

## 🔬 Features
- **MSA using Needleman-Wunsch algorithm**
- **Phylogenetic tree construction using R**
- **Translation of nucleotide sequences into amino acid sequences**
- **Analysis of TP53 sequence variations**

## 📂 Project Structure
```
cs123-final/
│── MSA_CS123.py                # Python script for MSA using Needleman-Wunsch algorithm
│── TranslationtoAA.py           # Python script for nucleotide to amino acid conversion
│── Phylogenetic_Tree.R         # R script for phylogenetic tree building
│── mammalAA.fasta              # Mammalian TP53 sequences (as Amino Acid)
│── nonMammalAA.fasta           # Non-Mammalian TP53 sequences (as Amino Acid)
│── mammal_tp53_nt.txt          # Mammalian TP53 sequences (as Nucleotide)
│── nonMammal_tp53_nt.txt       # Non-Mammalian TP53 sequences (as Nucleotide)
│── Project_Report_Sabale_SanchezCS123.pdf  # Written report of methodology & findings
│── TP53-Sabale&Sanchez.pdf     # Final project presentation (PowerPoint slides)
```

## 🛠️ How to Run the Analysis

### **Translation to Amino Acids**
1. Run the translation script:
   ```bash
   python TranslationtoAA.py
   ```
   *(Adjust line 62 per file location on local machine)*

### **Python MSA (Needleman-Wunsch Algorithm)**
1. Install dependencies:
   ```bash
   pip install numpy
   ```
2. Run the MSA program:
   ```bash
   python MSA_CS123.py
   ```

### **Phylogenetic Tree (R Version)**
1. Install necessary packages in R:
   ```r
   install.packages(c("seqinr", "ape", "msa"))
   ```
2. Open and run `Phylogenetic_Tree.R` in RStudio.

## 🔬 Validation & Accuracy

To ensure the accuracy of our results, we performed additional validation:

- **Clustal Omega**: Used for sequence alignment comparison.
- **Phylogeny.fr**: Used to generate an external phylogenetic tree for validation.

The findings in our **report and presentation** reflect insights from both our custom algorithms and external tools to ensure accuracy.

## 📝 References

- **NCBI Database for TP53 Sequences**: [NCBI](https://www.ncbi.nlm.nih.gov/)
- **Clustal Omega**: [Clustal Omega](https://www.ebi.ac.uk/Tools/msa/clustalo/)
- **Phylogeny.fr**: [Phylogeny.fr](http://www.phylogeny.fr/)
- **Phylogenetic Tree Basics**: [Washington University](https://evolution.gs.washington.edu/phylip/doc/main.html)

---
📌 *Maintained by Martin Sanchez & Ryder Sabale*

