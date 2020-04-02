# BlastCheck
A lightweight python program for checking the number of blast hits for some sequences.  
v 1.0  
jcooper036@gmail.com  

# Installation
## NCBI Blast
This package **does not** come with a distribution of NCBI blast. It expects that you can call `blast` from your command line. If you are on a Mac, Blast can be installed with [Homebrew](https://brew.sh/), using  
`brew install blast`  
  
NCBI maintains a [Blast command line resource doc](https://www.ncbi.nlm.nih.gov/books/NBK279690/).

## Setup
BlastCheck needs a .ctl file in order to know where to hunt for the genome. This is just a plain text file in the format:  
parameter:value  
  
This controls the genome file location and the location of the output file. There is a sample .ctl file in the repo. So:
- set the location of the .ctl file in `main.py`
- set the parameters in the .ctl file to point to the correct locations

# Using BlastCheck
Call blast check from `main.py` using the format:  
`main.py sequence1,sequence2,sequence3,...,sequenceN`