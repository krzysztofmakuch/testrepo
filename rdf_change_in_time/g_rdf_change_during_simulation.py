import subprocess
import pdb
import create_image_from_xvg.py

def traj_run(XTC, TPR, index, XVG, begin, end, dt, atom):
    '''(str,str,str,str,int,int,int,str)
    Function runs subsequent SOLVATATION gmx rdf. The idea is
    to get RDFs OF WATER against some atoms for time evolution
    during some biochemical processess. Example of use:
    traj_run('LUT_BCL60_md_1ps_plus15_50fs.xtc','LUT_BCL60_md_1ps_plus15_50fs.tpr','index_RDF_27022.ndx', 'otuput.xvg', '1500', '1550', '5', '10')
    - xtc or trr trajectory: LUT_BCL60_md_1ps_plus15_50fs.xtc
    - tpr file: LUT_BCL60_md_1ps_plus15_50fs.tpr
    - ndx index file containing the indexes for atoms aroud
    which RDF is to be cunted: index_RDF_27022.ndx
    - output name: output.xvg
    - begning for the 1st RDF calculation: 1500 [ps]
    - end of the LAST RDF: 1550 [ps]
    - single RDF time. Also timestep between subsequen RDF
    calcultaions: 5 [ps]
    - group name or number in the ndx index file
    for RDF calcultaion: 10
    
    '''

    
    begin=int(begin)
    end=int(end)
    dt=int(dt)
    B = begin
    E = B + dt

    XVG=remove_xvg(XVG)

    while E<=end:
        print(E)
        XVG_changed = XVG+"_B"+str(B)+"_E"+str(E)+".xvg"
    #    print(XVG_zmienione) 
        
        p1 = subprocess.Popen(['echo', atom, '\n', 'SOL'], stdout=subprocess.PIPE)
#        pdb.set_trace()
        grdf= ' '.join(['g_rdf', '-f', XTC, '-s', TPR, '-n', index, '-b', str(B), '-e', str(E), '-o', XVG_changed])
        
        p2 = subprocess.Popen([grdf], stdin=p1.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell = True)
        p1.stdout.close()
        output = p2.communicate()[1]
    #    print(output)
        
        B = E
        E = E + dt

def remove_xvg(filename):
    '''(str)
    Cut-off the xvg extension for name change:
    - removes xvg at the end of the name
    - prints warning if it's not xvg file, but still ocntinues!
    '''
    if filename[-4:] == ".xvg":
        filename = filename[0:-4]
        return(filename)
    elif filename[-4] =="." and filename[-3:] != "xvg":
        return("wrong extension! program will still try to use the file, \
but errors may show up!")



if __name__ == '__main__':
    print('This program calculates solvatation RDF.')
    print('   XTC or TRR trajectory: ')
    XTC = input()

    print('   TPR file: ')
    TPR = int(input())
    
    print('   output XVG names. Give name for one file with xvg \
extension. Don\'t add numbering: ')
    XVG = input() 

    print('   Begin RDF time: ')
    begin = input()

    print('   End RDF time: ')
    end = input()

    print('   Single RDF time: ')
    dt = input()


    print('   Group to calculate solvatation RDF for: ')
    atom = input() 

    traj_run(XTC, TPR, index, XVG, begin, end, dt, atom)

    print('Do you want to create movie covering the RDF change - Y/N? ')
    movie = input()
    if movie == Y:
        create_image_from_xvg.line_graphs(XVG)
#        create_movie_from_png

    elif movie == N:
        print('cyu around Spark!')
        

