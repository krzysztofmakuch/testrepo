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
    
    weighted_files = files_weights(files_matching_pattern)

    out_name = input('Please select an output name: ')
    out_file = open(out_name, 'w')

    #adds legend and some prefix from one of the files
    legend(files_matching_pattern[0], out_file)
    
    array_of_arrays = content_of_all_files(files_matching_pattern)
    list_of_weights = [weighted_files[key] for key in weighted_files]
    print_array(weighted_array(array_of_arrays, list_of_weights), out_file)

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
    
def files_weights(filelist):
    '''(list) -> dict
    asks for weights for files in given list and creates dict
    '''

    filedict = {}
    
    for file in filelist:
        filedict[file] = float(input('Give file %s a weight: ' %(file)))

    print('You\'ve given the following weights to files: \n', filedict)
    return filedict
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
    

def print_array(array, outfile):
    '''(list, str)
    print an array (list of lists) to file
    '''
    #print(array)
    for line in array:
        i = 0
        for e in line:
            if i == 0:
                print('%11f' %(e), end = '', file = outfile)
                i = 1
            else:
                print('%9f' %(e), end = '', file = outfile)
        print('', file = outfile)

def weighted_array(array_of_arrays, list_of_weights):
    '''(list, list) -> list
    Creates a list of weighted values of RDF from values given in
    array_of_arrays
    '''
    A = array_of_arrays
    w = list_of_weights

    weighted = numpy.average(A, axis = 0, weights = w).tolist()
    return weighted


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

def fileread(file):
    ''' like readlines, but ommits certain lines'''
    lines_list = []
    for line in file:
        if line[0] not in ['#','@']:
            lines_list.append([float(x) for x in (line.split())])

    return lines_list

