#import previously done files

from .rdf_change_in_time import g_rdf_change_during_simulation
from .angles_from_positions import run_angles_from_positions

def interf():
    '''
    sth sth

    '''

    print('What do you want to do?:\
          \n 0. HELP \
          \n 1. RDF change in time \
          \n 2. MSD & diffusion - work in progress\
          \n 3. angle vs axis \
          \n 4. xyz to volume  - work in progress\
          \n 5. average number of H-bonds  - work in progress\
          \n 5. unavailable: H-bond lifetime - work in progress')
    action = int(input()[0])

    #a0 = help_module
    a1 = g_rdf_change_during_simulation.run_rdf_change

    a3 = run_angles_from_positions.run_module


    actions = {
               1: a1,
               3: a3,
               }
    actions[action]()


if __name__ == '__main__':
    interf()
