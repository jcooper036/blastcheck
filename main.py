#! /usr/bin/env python3

"""
- general flow
    - read in a comma seperated string of squeces
    - for each of those sequences
        - blast it against a resource
        - does it have an exact match?
        - does it have more than one exact match?
        - what is the score of the second best match?
    - return a csv that has contains all this data
"""

import BlastCheck as blch

CTL_FILE = '/Users/jacob.cooper/blastcheck/control.ctl'

def main():
    # load in the sequences
    seqs = blch.read_sequences()
    
    # load in the control file
    ctl = blch.load_ctl(CTL_FILE)

    # send the sequences to blast
    df = blch.blast_sequences(seqs, ctl)

    # write the data frame to a csv
    df.to_csv(ctl.params['output_file'])

    print(f'Wrote .csv to {ctl.params["output_file"]}')


if __name__ == '__main__':
    main()
    