#! /usr/bin/env python3

import os

class Ctl(object):

    def __init__(self, file):
        self.file = file
        self.params = {}
        self.__load_params__()
    
    def __load_params__(self):
        """
        Searches the ctl file for matches to the search_params dict, and adds parameters that are found to self.params

        """
        # name of the param : thing to serach for in ctl file
        search_params = {
            'genome_path' : 'genome_path',
            'output_file' : 'output_file'
        }

        assert os.path.isfile(self.file), "ctl filepath is no good"

        with open(self.file, 'r') as f:
            for line in f.readlines():
                line = line.rstrip()
                line = line.split(':')
                if len(line) > 1:
                    if line[0] in search_params:
                        self.params[line[0]] = line[1]
        
def load_ctl(file):
    """
    Input:
        file - str that is a file path
    Returns:
        ctl object
    """

    return Ctl(file)