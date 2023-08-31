from setuptools import setup

setup(name='gromacs_tools',
      version='0.1',
      description='Data analysis tools for GROMACS Molecular Dynamics package',
      author='Krzysztof Makuch',
      author_email='krzysztof.makuch@gmail.com',
      packages=['gromacs_tools'],
      install_requires=['pandas',
                        'numpy',
                        'matplotlib']
      )
