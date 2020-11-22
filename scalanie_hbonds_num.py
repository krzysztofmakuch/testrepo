'''
Program calculates the weighted average of RDF from given files.
Corresponding values from every line from various files are taken
and averaged with given weights.
'''

import os
import glob
import numpy

def main():
    ''' '''
    path = os.getcwd()
    print('You are currently in the following directory: ', path)
    pattern = input('Please insert a standard linux pattern for files: ')

    files_matching_pattern = list_of_files(path, pattern)
    if files_matching_pattern == 0:
        print('I\'m sorry, but I can\'t continue')
        return None
    
    out_name = input('Please select an output name: ')
    out_file = open(out_name, 'w')

    #adds legend and some prefix from one of the files
    legend(files_matching_pattern[0], out_file)

    write_to_file(files_matching_pattern, out_file)

    out_file.close()
    
    
def list_of_files(path, pattern):
    ''' (str, str) -> list
    creates a list of files from pattern
    '''

    files =  glob.glob(path +'/'+ pattern)
    if files != path:
        print('The following files match pattern: \n', files)
        return files
    else:
        print('No files matching pattern')
        return 0

    
def legend(input_file, output_file):
    '''(str, str)
    Adds some line to the begining of output file
    '''
    f = open(input_file, 'r')
    print('#This file was created by KMakuch\'s script', file = output_file)
    for line in f:
        if line[0] == '@':
            print(line, end = '', file = output_file)
    f.close()
    

def content_of_all_files(filelist):
    '''(list) -> list
    Creates a list of lists of lines from every file in filelist.
    Like readlines over several files.
    '''
    list_of_lines_all_files = []
    
    for file in filelist:
        f = open(file, 'r')
        list_of_lines_all_files.append(fileread(f))
        f.close()

    return list_of_lines_all_files


def write_to_file(files_matching_pattern, out_file):
    ''' (list, file)
    iterates over list of files matching pattern and writes their
    subsequent lines to output file
    '''
    for file in files_matching_pattern:
        f = open(file, 'r')
        file_read_write(f, out_file)
        f.close()
        

def file_read_write(file, outputfile):
    ''' like readlines, but ommits certain lines'''
    for line in file:
        if line[0] not in ['#','@']:
            print(line, file = outputfile)

