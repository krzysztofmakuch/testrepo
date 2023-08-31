from . import angle_from_positions_v3
from . import graphs_from_angles

def run_module():
    """ As name says - runs all module parts in order """

    angle_from_positions_v3.run_module()

    graphs_from_angles.run_module()


if __name__ == '__main__':
    run_module()
