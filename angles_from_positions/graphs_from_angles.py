import matplotlib.pyplot as plt
import pandas as pd

def read_file(filename):
    ''' (str) -> df
    reads the file into pandas dataframe
    with first column as index '''

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

    #column names:
    col_names = ['time']  
    name = lambda x: "mol%02d" %(x)
    for count, e in enumerate(firstline[1:]):
        col_names.append(name(count))
    #read data:
    df = pd.read_csv(filename, engine = 'python',
                     sep = "\t|\s",names = col_names,
                     index_col=0)

    #return number of columns and thedataframe
    return [len_1st, df]
        
def print_angles(data):
    '''(list)
    Takes a list from read_file function.
    Creates a graph from a dataframe.
    '''
    col_num = data[0]
    df = data[1]
    col_nam = df.columns

    for col in col_nam:
        plt.scatter(df.index, df[col])
        plt.title(col)
        plt.xlabel('time')
        plt.ylabel('angle [deg]')
        plt.ylim([0,360])
        plt.savefig(col, format = 'png')
        plt.close()


#print_angles(read_file('angles_example.txt'))

if __name__ == '__main__':
    print('Give a filename to create graphs: ')
    file = input()
    print_angles(read_file(file))
    print('You can find crude representations of the angle \
evolution in subsequent col## PNG files.')

    
