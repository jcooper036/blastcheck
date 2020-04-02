#! /usr/bin/env python3

import sys

def read_sequences():
    """
    Check for the appropriate input
    Return a list of sequences
    """
    assert len(sys.argv) > 1, 'no input detected'
    #@todo add a warning for not nucleotide characters
    if ',' not in sys.argv[1]:
        return [sys.argv[1]]
    return [x.strip() for x in sys.argv[1].split(',')]