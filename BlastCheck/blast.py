#! /usr/bin/env python3

import pandas as pd
import BlastCheck as blch


def blast_sequences(seqs, ctl):
    """
    Input:
        seqs : list of sequences
        ctl : control object
    Returns
        blastdata : pandas df of the blast data
    """
    data = {}
    
    for idx, seq in enumerate(seqs):
        blaststring = blast(seq, ctl)
        data[seq] = parse_blast(blaststring)
        print(f'Retrieved Blast data for sequence {idx+1} / {len(seqs)}')
    blastdata = format_blasts_results(data)

    return blastdata

def blast(seq, ctl):
    """
    Input:
        seq : str, DNA sequence
        ctl : control object
    Returns :
        sequence : str
        length of the sequence : int
        first_hit : evalue for the first hit
        second_hit : evalue for the second hit
    """
    genome = ctl.params['genome_path']
    command = 'blastn -task blastn-short -outfmt "6" -query <(echo ' + seq + ') -db ' + genome + ' | sort -k12 -n -r | head -5'

    out = str(blch.bash(command)).split('\n')
    return out

def parse_blast(blaststring):
    """
    Input:
        blaststring : list of strings, which are all blast results. Columns of blast results are tab sep
    Returns:
        modify this code to determine what is returned
    """
    evalues = []
    for s in blaststring:
        s = s.split('\t')
        # the last value is the E-value
        if len(s[-1])>0:
            evalues.append(float(s[-1]))
    evalues = sorted(evalues, reverse=True)
    if len(evalues) > 1:
        return {'first' : evalues[0], 'second' : evalues[1]}
    elif len(evalues) == 1:
        return {'first' : evalues[0], 'second' : 'NA'}
    else:
        return {'first' : 'NA', 'second' : 'NA'}

def format_blasts_results(data):
    """
    """
    blastdata = {
        'sequence' : [],
        'length' : [],
        'first_evalue' : [],
        'second_evalue' : [],
    }
    for key, val in data.items():
        blastdata['sequence'].append(key)
        blastdata['length'].append(len(key))
        blastdata['first_evalue'].append(val['first'])
        blastdata['second_evalue'].append(val['second'])
    blastdata = pd.DataFrame(blastdata)
    return blastdata