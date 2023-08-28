import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import re
import os


def read_file(filename):
    ''' (str) -> df
    reads the file into numpy array and converts to dataframe
    with first column as index '''

    '''
    #how many cols are there?
    with open(filename, 'r') as temp_f:
        read_1st = temp_f.readline()
    firstline = read_1st.split()

    #handling corrupted files:
    len_1st = len(firstline)
    if len_1st == 0:
        print('empty file!')
        return 0
    elif len_1st == 1:
        print('corrupted data! file contains only 1 column!')
        return 0
    '''

    #column names:
     
    '''
    name = lambda x: "rdf%02d" %(x)
    for count, e in enumerate(firstline[1:]):
        col_names.append(name(count))
    '''
    #read data:
    np_data = np.loadtxt(filename, comments = ['#','@'])
    np_data = np_data.astype(float)

    #numpy because pandas can't use multiple camments
    #change to pandas for consistency when available

    num_of_cols = np_data.shape[1]

    col_names = ['distance']
    if num_of_cols > 2:
        for i in range(1,num_of_cols):
            col_names.append('RDF_'+str(i))
    else:
        col_names.append('RDF')

    #print(np_data)
    #print(np_data.shape)
    #print(col_names)
    #print(np_data[0:,0])
    '''
    df = pd.read_csv(filename, engine = 'python',
                     sep = "\t|\s",comment = ['#','@'],
                     names = col_names,
                     index_col=0)
    '''

    df = pd.DataFrame(data = np_data,
                      columns = col_names)
    #print(df.head())
    df = df.set_index(col_names[0])
    #print(df.head())

    return df

        
def print_line_graph(df, filename, col_title = 'RDF',
                     xlabel = 'Distance', ylabel = 'RDF',
                     title = 'RDF', maxrdf = 3.0):
    '''(DataFrame, str, int, str, str, float)
    Takes data from read_file function.
    Creates a graph from a dataframe.
    - df - dataframe
    - filename - output
    '''
    #right now the script assumes it'll take the 1st column
    #should be changed, number of cols needed?:
    #df = data[1]
    col_names = df.columns
    #print(col_names)

    plt.plot(df.index, df.loc[:,col_title])
    #plt.plot(df.index, df['RDF'])
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.ylim(0, maxrdf)
    plt.savefig(filename, format = 'png')
    plt.close()


def list_of_xvg(pattern):
    '''(str) -> list
    The function will attempt to create a list based on
    the provided pattern. It is expected that a pattern will
    be 'ready to use'. However if it is found to end with
    .xvg the funtion will attemp to cut off the end with
    number. Assumption that the final number is separated.
    If no number is present, only .xvg will be removed.
    For example:
    - RDF_POPC_01.xvg will be cut to RDF_POPC
    - RDF_POPC.xvg will be cut to RDF_POPC
    Be aware, that it is not a goal to remove number from
    final PNG files - this function is only used to clean
    pattern and find all matching files.
    '''
    pattern = re.sub('_?[0-9]*(\.xvg)?$','',pattern)
    print('I\'m using pattern for XVG files: ', pattern)
    allfiles = os.listdir()
    rdf_files = list(filter(lambda fn: (pattern in fn) and fn.endswith('.xvg'),
                            allfiles))
    #print(rdf_files)

    return rdf_files



def line_graphs(xvg, xtit = 'distance', ytit = 'RDF', maxrdf = 1, cols = [0,1]):
    '''(str, str, str)
    Creates all line-graphs from an xvg file. You can change
    titles and columns used.
    '''
    xvg_files = list_of_xvg(xvg)
    #print(xvg_files)

    #no need to add number, it's assumed that xvg are already
    #numbered in previous steps
    #name_png = lambda name_xvg, i: (name_xvg[:-4] +'%04d'+'.png') %(i)
    name_png = lambda name_xvg: (name_xvg[:-4] +'.png')
    
    for iterator, file in enumerate(xvg_files):
        data = read_file(file)
        print_line_graph(data, name_png(file))


if __name__ == '__main__':
    print('Give a filename to create graphs: ')
    file = input()
    line_graphs(file)
    print('You can find crude representations of the angle \
evolution in subsequent PNG files.')


    

