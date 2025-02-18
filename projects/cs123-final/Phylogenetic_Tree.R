---
  title: "Phylogenetic_Tree"
author: "Ryder Sabale"
date: "`r Sys.Date()`"
output:
  pdf_document: default
word_document: default
---
  
  ```{r setup, include=FALSE}
knitr::opts_chunk$set(warning = FALSE, message = FALSE) 
```

```{r}
# Loading necessary packages
library(seqinr)
library(ape)
library(msa)
```

```{r}
# Function uses basic workflow between packages from: 
# Bryan Temogoh of Applied EPI
FASTA_to_Phylo_Tree <- function(file, sequence_type = c("DNA", "RNA", "AA", "Other"), name = file) {
  
  # Read the fasta files using msa package 
  if(sequence_type == "DNA") { 
    # If the sequence is in DNA nucleotides (A,C,G,T)
    sequences <- readDNAStringSet(file)
  } else if (sequence_type == "RNA") { 
    # If the sequence is in RNA nucleotides (A,C,G,U)
    sequences <- readRNAStringSet(file)
  } else if (sequence_type == "AA") { 
    # If the sequence is in amino acids
    sequences <- readAAStringSet(file)
  } else { 
    # The reader will just read each character for what it is, regardless of meaning
    sequences <- readBStringSet(file)
  }
  
  # Align and print the sequences using the msa package
  msa <- msa(sequences, method = "ClustalOmega")
  print(msa)
  
  # Convert the MSA object into a list usable by seqinr package
  alignment <- msaConvert(msa, type = "seqinr::alignment")
  
  # Compute a distance matrix from the alignment
  distance_matrix <- dist.alignment(alignment, matrix = "identity")
  
  # Construct a phylogenetic tree using neighbor joining
  tree <- bionj(distance_matrix)
  
  # Plot the tree
  plot(tree, main = name)
}
```

```{r}
mammal_sequences <- "C:/Users/ryder/CS-123A/mammalAA.fasta"
nonmammal_sequences <- "C:/Users/ryder/CS-123A/nonMammalAA.fasta"

FASTA_to_Phylo_Tree(mammal_sequences, sequence_type = "AA", name = "Mammal Phylogenetic Tree")
FASTA_to_Phylo_Tree(nonmammal_sequences, sequence_type = "AA", name = "Non-Mammal Phylogenetic Tree")

